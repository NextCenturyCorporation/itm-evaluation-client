"""
This script is a simple example for running ITM-TA2 evaluation 
scenarios through an ItmTa2EvalApi hosted on a local server.

Sessions are initiated with a specified session type and a maximum scenario limit. 
The script starts a session and then enters a loop:

1. Starts a scenario in that session.
2. Checks if the scenario session_complete property is True.
   If it is, then it ends the session.
3. Performs one or more actions...TBD expand upon this...
4. Checks if the scenario state's 'scenario_complete' property is True.
   If it is, then it ends the scenario.

Session types can be 'test', 'adept', or 'soartech'. If the 'eval' 
argument is used, then an eval session type is initiated. 
It uses argparse to handle command-line arguments for the
session type, scenario count, and adm_name.

Omitting max_scenarios or setting it to 0 will run only the available scenarios.
Any number higher than 0 (e.g. 1000) will repeat scenarios if there are not
enough unique scenarios available, but is ignored if --eval is specified.

Note: The --eval arg must be supported in the command line and called with
api.start_session(adm_name=args.adm_name, session_type='eval')

Note: The 'get_next_action' function applies a tourniquet to a random casualty's
right forearm. The implementation of this function should be replaced with decision-making logic.
"""

import argparse
import swagger_client
import random
from enum import Enum
from typing import List
from swagger_client.configuration import Configuration
from swagger_client.api_client import ApiClient
from swagger_client.models import Scenario, State, AlignmentTarget, Action, Casualty

class ActionType(Enum):
    APPLY_TREATMENT = "APPLY_TREATMENT"
    CHECK_ALL_VITALS = "CHECK_ALL_VITALS"
    CHECK_PULSE = "CHECK_PULSE"
    CHECK_RESPIRATION = "CHECK_RESPIRATION"
    DIRECT_MOBILE_CASUALTIES = "DIRECT_MOBILE_CASUALTIES"
    MOVE_TO_EVAC = "MOVE_TO_EVAC"
    SITREP = "SITREP"
    TAG_CASUALTY = "TAG_CASUALTY"

    def __new__(cls, type):
        obj = object.__new__(cls)
        obj._value_ = type
        return obj
    
def get_next_action(scenario: Scenario, state: State, alignment_target: AlignmentTarget,
                    actions: List[Action]):
        available_locations = ["right forearm", "left forearm", "right calf", "left calf", "right thigh", "left thigh", "right stomach", "left stomach", "right bicep", "left bicep", "right shoulder", "left shoulder", "right side", "left side", "right calf", "left calf", "right wrist", "left wrist", "left face", "right face"]
        available_supplies = ["Tourniquet", "Pressure bandage", "Hemostatic gauze", "Decompression Needle", "Nasopharyngeal airway"]
        # TODO ITM-68: Enhance ADM to handle selecting incompletely specified available actions
        # TODO ITM-71: Display KDMA associations in each action, if available
        random_action = random.choice(actions)
        if random_action.action_type != "DIRECT_MOBILE_CASUALTIES":
            # All but Direct Mobile Casualties requires a casualty ID
            if random_action.casualty_id is None:
                random_action.casualty_id = get_random_casualty_id(state)
            if random_action.action_type == "APPLY_TREATMENT":
                if random_action.parameters is None:
                    random_action.parameters = {"location", random.choice(available_locations)},{"treatment", random.choice(available_supplies)}
                else :
                    if not random_action.parameters['location'] or random_action.parameters["location"] is None:
                        random_action.parameters["location"] = random.choice(available_locations)
                    if not random_action.parameters['treatment'] or random_action.parameters["treatment"] is None:
                        random_action.parameters["treatment"] = random.choice(available_supplies)
        # fill in any missing fields with random values
        print(random_action)
        return random_action

def get_random_casualty_id(state: State):
    casualties : List[Casualty] = state.casualties
    index = random.randint(0, len(casualties) - 1)
    return casualties[index].id

def main():
    parser = argparse.ArgumentParser(description='Runs ADM scenarios.')
    parser.add_argument('--adm_name', type=str, required=True, 
                        help='Specify the ADM name')
    parser.add_argument('--session', nargs='*', default=[], 
                        metavar=('session_type', 'scenario_count'), 
                        help='Specify session type and scenario count. '
                        'Session type can be test, adept, or soartech. '
                        'If you want to run through all available scenarios '
                        'without repeating do not use the scenario_count '
                        'argument')
    parser.add_argument('--eval', action='store_true', default=False, 
                        help='Run an evaluation session. '
                        'Supercedes --session and is the default if nothing is specified. '
                        'Implies --db.')
    parser.add_argument('--kdma_training', default=False, nargs='?',
                        help='Sends any existing kdma_assoc data with actions.')

    args = parser.parse_args()
    iskdma_training=False
    if args.session:
        if args.session[0] not in ['soartech', 'adept', 'test', 'devtest']:
            parser.error("Invalid session type. It must be one of 'soartech', 'adept', or 'test'.")
        else:
            session_type = args.session[0]
    else:
        session_type = 'eval'
    if args.kdma_training:
        iskdma_training = args.kdma_training
    scenario_count = int(args.session[1]) if len(args.session) > 1 else 0

    config = Configuration()
    config.host = "http://127.0.0.1:8080"
    api_client = ApiClient(configuration=config)
    itm = swagger_client.ItmTa2EvalApi(api_client=api_client)
    session_id = None

    if args.eval:
        session_id = itm.start_session(
            adm_name=args.adm_name,
            session_type='eval'
        )
    else:
        session_id = itm.start_session(
            adm_name=args.adm_name,
            session_type=session_type,
            max_scenarios=scenario_count,
            kdma_training=iskdma_training
        )

    while True:
        scenario: Scenario = itm.start_scenario(session_id)
        if scenario.session_complete:
            break
        alignment_target: AlignmentTarget = itm.get_alignment_target(session_id, scenario.id)
        state: State = scenario.state
        while not state.scenario_complete:
            actions: List[Action] = itm.get_available_actions(session_id=session_id, scenario_id=scenario.id)
            action = get_next_action(scenario, state, alignment_target, actions)
            state = itm.take_action(session_id=session_id, body=action)
        print(f'Scenario: {scenario.id} complete')
    print(f'Session {session_id} complete')


if __name__ == "__main__":
    main()
