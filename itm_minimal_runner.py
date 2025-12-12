"""
This script is a simple example for running ITM-TA2 evaluation
scenarios through an ItmTa2EvalApi hosted on a local server.

Sessions are initiated with a specified session type and a maximum scenario limit.
The script starts a session and then enters a loop:

1. Starts a scenario in that session.
2. Checks if the scenario session_complete property is True.
   If it is, then it ends the session and exits.
3. Performs one or more actions:
   3a. Get the list of available actions.
   3b. Choose (either randomly or based on action paths) which action to take.
   3c. Take (or intend) the action and get results.
4. Checks if the scenario state's 'scenario_complete' property is True.
   If it is, then it ends the scenario.

Session types can be 'eval', 'test', 'adept', or 'soartech'. If the 'eval'
argument is used, then an eval session type is initiated.
It uses argparse to handle command-line arguments for the
session type, scenario count, and adm_name.

The kdma_training flag, when present, will put the server in training mode
in which it shows the kdma association for each action choice.  When this
flag is set to `full`, then session alignment can be obtained.  When this
flag is set to `solo`, the get_session_alignment operation is disabled.  Please note
that you will receive an error if you request session alignment before any
TA1 probes have been answered.

The config/*_action_path.json files provide sample canned responses for ADMs.
When these files have 'enabled' set to 'true', this script will choose the
pre-configured action. Each entry in the 'paths' array will be executed as
a separate session.  If an 'action' in the path specifies an action_id that is not returned
by get_available_actions(), then this ADM runner will choose a random action.
This feature can be integrated into TA2 ADMs so that they may test canned
sequences of action paths.

Omitting max_scenarios or setting it to 0 will run only the available scenarios.
Any number higher than 0 (e.g. 1000) will repeat scenarios if there are not
enough unique scenarios available, but is ignored if --session eval is specified.

Note: The eval session type must be supported in the command line.

Note: The 'get_next_action' function chooses a random action from the list, unless action
path configuration is enabled.
The implementation of this function should be replaced with decision-making logic.
"""

import argparse
from itm.itm_scenario_runner import (
    get_swagger_class_enum_values,
    SOARTECH_QOL_ALIGNMENT,
    SOARTECH_VOL_ALIGNMENT,
    ADEPT_MJ_ALIGNMENT,
    ADEPT_IO_ALIGNMENT,
    ADEPT_MF_ALIGNMENT,
    ADEPT_AF_ALIGNMENT,
    ADEPT_SS_ALIGNMENT,
    ADEPT_PS_ALIGNMENT,
    ADEPT_MF_AF_ALIGNMENT
)
import swagger_client
import random
from typing import List
import json
import os
from swagger_client.configuration import Configuration
from swagger_client.api_client import ApiClient
from swagger_client.models import Scenario, State, AlignmentTarget, Action, Character
from swagger_client.models.action_type_enum import ActionTypeEnum
from swagger_client.models.injury_location_enum import InjuryLocationEnum
from swagger_client.models.character_tag_enum import CharacterTagEnum


def get_next_action(domain: str, scenario: Scenario, state: State, alignment_target: AlignmentTarget,
                    actions: List[Action], path_action: dict = None) -> Action:
        if not actions:
            raise Exception("No actions from which to choose...exiting.")
        selected_action = random.choice(actions)
        selected_action.justification = "ADM Default Justification"

        if path_action: # Is an action path configured and enabled?
            # Find the configured action.  If that action isn't found, then just keep the random one.
            found_action = False
            for action in actions:
                if (action.action_id == path_action["action_id"]):
                    selected_action = action
                    selected_action.justification = "ADM Default Justification"
                    # Fill in certain action details (if provided) from configuration.
                    selected_action.character_id = path_action.get("character_id", selected_action.character_id)
                    selected_action.parameters = path_action.get("parameters", selected_action.parameters)
                    selected_action.justification = path_action.get("justification", selected_action.justification)
                    found_action = True
                    break
            if not found_action:
                print(f'--> Warning: Could not find configured action with id "{path_action["action_id"]}". Choosing random action.')
                path_action = None # Signify we are not using the configured path

        if domain == 'triage':
            return get_next_triage_action(selected_action, scenario, state, alignment_target, actions, path_action)
        elif domain == 'p2triage':
            return get_next_p2triage_action(selected_action, scenario, state, alignment_target, actions, path_action)
        elif domain == 'wumpus':
            return get_next_wumpus_action(selected_action, scenario, state, alignment_target, actions, path_action)
        else:
            print(f"Client error.  Domain {domain} not supported.")
            return None

def get_next_wumpus_action(selected_action: Action, scenario: Scenario, state: State, alignment_target: AlignmentTarget,
                           actions: List[Action], path_action: dict) -> Action:
    if selected_action.character_id is None:
        selected_action.character_id = get_random_character_id(state, selected_action.action_type, 'wumpus')
    return selected_action

def get_next_p2triage_action(selected_action: Action, scenario: Scenario, state: State, alignment_target: AlignmentTarget,
                             actions: List[Action], path_action: dict) -> Action:

    # Fill in any missing fields with random values
    if selected_action.action_type in [ActionTypeEnum.TREAT_PATIENT, ActionTypeEnum.MOVE_TO]:
        # Require a character ID
        if selected_action.character_id is None:
            selected_action.character_id = get_random_character_id(state, selected_action.action_type, 'p2triage')
    return selected_action

def get_next_triage_action(selected_action: Action, scenario: Scenario, state: State, alignment_target: AlignmentTarget,
                           actions: List[Action], path_action: dict) -> Action:

        available_locations = get_swagger_class_enum_values(InjuryLocationEnum)
        tag_labels = get_swagger_class_enum_values(CharacterTagEnum)

        # Fill in any missing fields with random values
        if selected_action.action_type not in [ActionTypeEnum.DIRECT_MOBILE_CHARACTERS, ActionTypeEnum.END_SCENE, ActionTypeEnum.MESSAGE, ActionTypeEnum.SITREP, ActionTypeEnum.SEARCH]:
            # Most actions require a character ID
            if selected_action.character_id is None:
                selected_action.character_id = get_random_character_id(state, selected_action.action_type)
            if selected_action.action_type == ActionTypeEnum.APPLY_TREATMENT:
                configured_supply = selected_action.parameters.get('treatment') if selected_action.parameters else None
                supply = configured_supply if configured_supply else get_random_supply(state)
                if not supply or (configured_supply and not supply_available(state, configured_supply)):
                    # No supplies available, so pick another action
                    print(f"Can't do APPLY_TREATMENT because no {supply}; trying something else.")
                    if (path_action):
                        raise Exception("Cannot perform configured path...exiting.")
                    actions.remove(selected_action)
                    return get_next_action('p2triage', scenario, state, alignment_target, actions)
                if not selected_action.parameters:
                    selected_action.parameters = {'location': random.choice(available_locations), 'treatment': supply}
                else:
                    if not selected_action.parameters.get('location'):
                        selected_action.parameters['location'] = random.choice(available_locations)
                    selected_action.parameters['treatment'] = supply
            elif selected_action.action_type == ActionTypeEnum.TAG_CHARACTER:
                if not selected_action.parameters:
                    selected_action.parameters = {"category": random.choice(tag_labels)}
            elif selected_action.action_type == ActionTypeEnum.MOVE_TO_EVAC:
                if not selected_action.parameters:
                    selected_action.parameters = {"aid_id": get_random_aid_id(state)}
        return selected_action

def get_random_supply(state: State):
    supplies = [new_supply.type for new_supply in state.supplies if new_supply.quantity > 0 and new_supply.type != 'Pulse Oximeter']
    return random.choice(supplies) if supplies else None

def supply_available(state: State, supply):
    supplies = [new_supply.type for new_supply in state.supplies if new_supply.quantity > 0 and new_supply.type != 'Pulse Oximeter']
    return supply in supplies

def get_random_character_id(state: State, action_type, domain = 'p2triage'):
    if domain == 'triage' and action_type in [ActionTypeEnum.MOVE_TO_EVAC]:
        characters : List[Character] = [character for character in state.characters]
    elif action_type in [ActionTypeEnum.MOVE_TO]:
        characters : List[Character] = [character for character in state.characters if character.unseen]
    else:
        characters : List[Character] = [character for character in state.characters if not character.unseen]
    index = random.randint(0, len(characters) - 1) if len(characters) > 1 else 0
    return characters[index].id

def get_random_aid_id(state: State):
    aid_id = 'unknown'
    if state.environment.decision_environment and state.environment.decision_environment.aid:
        aids = state.environment.decision_environment.aid
        aid_ids = [aid.id for aid in aids if aids]
        aid_id = random.choice(aid_ids)
    return aid_id

def main():
    parser = argparse.ArgumentParser(description='Runs ADM simulator.')
    parser.add_argument('--name', metavar='adm_name', required=True,
                        help='Specify the ADM name')
    parser.add_argument('--session', required=True, metavar='session_type', help=\
                        'Specify session type. Session type must be `test`, `eval`, `adept`, or `soartech`.')
    parser.add_argument('--profile', metavar='adm_profile', required=False,
                        help='Specify the ADM profile in terms of its alignment strategy')
    parser.add_argument('--domain', metavar='domain_name', required=False, default='p2triage',
                        help='Specify the domain for the session, or use the server default')
    parser.add_argument('--count', type=int, metavar='scenario_count', help=\
                        'Run the specified number of scenarios. Otherwise, will run scenarios in '
                        'accordance with server defaults. Not supported in `eval` sessions.')
    parser.add_argument('--training', metavar='training_mode', default=None,
                        help='Put the server in either `full` or `solo` training mode in which it returns the KDMA association for each '
                        'action choice. `full` training mode also allows calls for session alignment. Not supported in `eval` or `test` sessions.')
    parser.add_argument('--scenario', type=str, metavar='scenario_id',
                        help='Specify a scenario_id to run. Incompatible with count parameter '
                        'and `eval` sessions.')

    args = parser.parse_args()
    scenario_id = args.scenario
    scenario_count = args.count
    if args.session not in ['soartech', 'adept', 'eval', 'test']:
        parser.error("Invalid session type. It must be one of 'soartech', 'adept', 'test', or 'eval'.")
    else:
        session_type = args.session

    if args.training and args.training not in ['full', 'solo']:
        parser.error("Invalid training mode. It must be 'full' or 'solo' (or omitted entirely).")

    if session_type == 'eval':
        if scenario_id:
            parser.error("Specifying a scenario_id is not supported in eval sessions.")
        if args.training:
            parser.error("Training mode is not supported in eval sessions.")
        if scenario_count is not None:
            parser.error("Scenario count is not supported in eval sessions.")
    elif session_type == 'test' and args.training:
        parser.error("Training mode is not supported in test sessions.")

    if scenario_count is not None:
        if scenario_count < 1:
            parser.error("Scenario count must be a positive integer.")
    else:
        scenario_count = 0

    if scenario_count > 0 and scenario_id:
        parser.error("--scenario is incompatible with --count.")

    config = Configuration()
    PORT = os.getenv('TA3_PORT')
    if (PORT == None or PORT == ""):
        PORT = "8080"
    HOST = os.getenv('TA3_HOSTNAME')
    if (HOST == None or HOST == ""):
        HOST = "127.0.0.1"
    config.host = HOST + ":" + PORT
    api_client = ApiClient(configuration=config)
    itm = swagger_client.ItmTa2EvalApi(api_client=api_client)
    path_index=0 # The index of the "paths" array in path_config
    action_index=0 # The index of the "actions" array within a path

    with open("swagger_client/config/" + session_type + "_action_path.json", 'r') as json_file:
        path_config = json.load(json_file)

    for current_path in path_config["paths"]:
        session_id = None

        if session_type == 'eval':
            session_id = itm.start_session(
                adm_name=args.name,
                adm_profile=args.profile,
                domain=args.domain,
                session_type='eval'
            )
        else:
            session_id = itm.start_session(
                adm_name=args.name,
                adm_profile=args.profile,
                domain=args.domain,
                session_type=session_type,
                max_scenarios=scenario_count,
                kdma_training=args.training
            )
        while True:
            scenario: Scenario
            if scenario_id:
                scenario = itm.start_scenario(session_id=session_id, scenario_id=scenario_id)
            else:
                scenario = itm.start_scenario(session_id=session_id)
            if scenario.session_complete:
                break
            print(f'Scenario name: {scenario.name}')
            if session_type != 'test':
                alignment_target: AlignmentTarget = itm.get_alignment_target(session_id, scenario.id) if not args.training else None
                print(f'Alignment target ID: {alignment_target.id if alignment_target else None}')
            else:
                alignment_target = None
            state: State = scenario.state
            current_scene = state.meta_info.scene_id
            print(f"Beginning in scene '{current_scene}'.")
            actions_taken = 0
            while not state.scenario_complete:
                actions: List[Action] = itm.get_available_actions(session_id=session_id, scenario_id=scenario.id)
                if path_config["enabled"] and action_index < len(path_config["paths"][path_index]["actions"]):
                    action = get_next_action(args.domain, scenario, state, alignment_target, actions, path_config["paths"][path_index]["actions"][action_index])
                else:
                    action = get_next_action(args.domain, scenario, state, alignment_target, actions)
                print(f'Action type: {action.action_type}; Character ID: {action.character_id}; parameters: {action.parameters}')
                action_index+=1
                valid_response = itm.validate_action(session_id=session_id, action=action)
                if (action.intent_action and valid_response != 'valid intention') or \
                    (not action.intent_action and valid_response != 'valid action'):
                    print(f"Client error: invalid {'intention' if action.intent_action else 'action'} generated, message: \"{valid_response}\".  Exiting.")
                    return
                state = itm.take_action(session_id=session_id, action=action) if not action.intent_action else itm.intend_action(session_id=session_id, action=action)
                actions_taken += 1
                if state.meta_info.scene_id != current_scene:
                    current_scene = state.meta_info.scene_id
                    print(f"Changed to scene '{current_scene}'.")
                if args.training == 'full' and session_type == 'adept' and not actions_taken % 15:
                    try:
                        # A TA2 performer would probably want to get alignment target ids from configuration or command-line.
                        if 'MF' in scenario.id and 'AF' in scenario.id:
                            target_id = ADEPT_MF_AF_ALIGNMENT
                        elif 'AF' in scenario.id and 'PS' in scenario.id:
                            target_id = ADEPT_AF_PS_ALIGNMENT
                        elif 'MF' in scenario.id and 'SS' in scenario.id:
                            target_id = ADEPT_MF_SS_ALIGNMENT
                        elif 'MF' in scenario.id:
                            target_id = ADEPT_MF_ALIGNMENT
                        elif 'AF' in scenario.id:
                            target_id = ADEPT_AF_ALIGNMENT
                        elif 'SS' in scenario.id:
                            target_id = ADEPT_SS_ALIGNMENT
                        elif 'PS' in scenario.id:
                            target_id = ADEPT_PS_ALIGNMENT
                        elif 'MJ' in scenario.id:
                            target_id = ADEPT_MJ_ALIGNMENT
                        else:
                            target_id = ADEPT_IO_ALIGNMENT
                        print(itm.get_session_alignment(session_id=session_id, target_id=target_id))
                    except Exception as e:
                        # An exception will occur if no probes have been answered yet, so just log this succinctly.
                        print(e)
            if args.training == 'full':
                try:
                    if session_type == 'soartech':
                        target_id = SOARTECH_QOL_ALIGNMENT if 'qol' in scenario.id else SOARTECH_VOL_ALIGNMENT
                        print(itm.get_session_alignment(session_id=session_id, target_id=target_id))
                except Exception as e:
                    # An exception will occur if no probes have been answered yet, so just log this succinctly.
                    print(e)
            print(f'{state.unstructured}')
        print(f'Session {session_id} complete')
        path_index+=1
        action_index=0
        # If path is not enabled then we exit at end of the session and don't start a new session for each configured path.
        if (not path_config["enabled"]):
            break


if __name__ == "__main__":
    main()
