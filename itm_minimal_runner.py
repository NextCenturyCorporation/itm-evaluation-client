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

The kdma_training flag, when set to True, will put the server in training mode
in which it shows the kdma association for each action choice.

The config/*_action_path.json files provide sample canned responses for ADMs.
When these files have 'enabled' set to 'true', this script will choose the
pre-configured action. Each entry in the 'paths' array will be executed as
a separate session.  If a 'path' specifies an actionId that is not returned
by get_available_actions(), then this ADM runner will choose a random action.
This feature can be integrated into TA2 ADMs so that they may test canned
sequences of action paths.

Omitting max_scenarios or setting it to 0 will run only the available scenarios.
Any number higher than 0 (e.g. 1000) will repeat scenarios if there are not
enough unique scenarios available, but is ignored if --eval is specified.

Note: The --eval arg must be supported in the command line.

Note: The 'get_next_action' function chooses a random action from the list.
The implementation of this function should be replaced with decision-making logic.
"""

import argparse
import swagger_client
import random
from enum import Enum
from typing import List
import json
import os
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
                    actions: List[Action], paths, index: int, path_index: int):
        random_action = random.choice(actions)

        if (paths["enabled"]):
            for action in actions:
                # Adding a length check, if they keep asking for action outside of index, then we will just select random ones
                if (index < len(paths["paths"][path_index]["path"]) and action.action_id == paths["paths"][path_index]["path"][index]):
                    random_action = action

        available_locations = ["right forearm", "left forearm", "right calf", "left calf", "right thigh", "left thigh", "right stomach", "left stomach", "right bicep", "left bicep", "right shoulder", "left shoulder", "right side", "left side", "right calf", "left calf", "right wrist", "left wrist", "left face", "right face", "unspecified"]
        available_supplies = ["Tourniquet", "Pressure bandage", "Hemostatic gauze", "Decompression Needle", "Nasopharyngeal airway"]
        tag_labels = ["MINIMAL", "DELAYED", "IMMEDIATE", "EXPECTANT"]

        # Fill in any missing fields with random values
        if random_action.action_type != "DIRECT_MOBILE_CASUALTIES" and random_action.action_type != "SITREP":
            # All but Direct Mobile Casualties and SITREP require a casualty ID
            if random_action.casualty_id is None:
                random_action.casualty_id = get_random_casualty_id(state)
            if random_action.action_type == "APPLY_TREATMENT":
                if random_action.parameters is None:
                    random_action.parameters = {"location": random.choice(available_locations),"treatment": random.choice(available_supplies)}
                else :
                    if not random_action.parameters['location'] or random_action.parameters["location"] is None:
                        random_action.parameters["location"] = random.choice(available_locations)
                    if not random_action.parameters['treatment'] or random_action.parameters["treatment"] is None:
                        random_action.parameters["treatment"] = random.choice(available_supplies)
            elif random_action.action_type == "TAG_CASUALTY":
                if random_action.parameters is None:
                    random_action.parameters = {"category": random.choice(tag_labels)}
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
                        help='Put the server in training mode in which it shows the kdma '
                        'association for each action choice. True or False')

    args = parser.parse_args()
    iskdma_training=False
    if args.session:
        if args.session[0] not in ['soartech', 'adept', 'test']:
            parser.error("Invalid session type. It must be one of 'soartech', 'adept', or 'test'.")
        else:
            session_type = args.session[0]
    else:
        session_type = 'eval'
    if args.kdma_training:
        iskdma_training = args.kdma_training
    scenario_count = int(args.session[1]) if len(args.session) > 1 else 0

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
    action_path_index=0
    path_index=0

    with open("swagger_client/config/" + session_type + "_action_path.json", 'r') as json_file:
        paths = json.load(json_file)

    for current_path in paths["paths"]:
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
                action = get_next_action(scenario, state, alignment_target, actions, paths, action_path_index, path_index)
                print(f'Action type: {action.action_type}; Casualty ID: {action.casualty_id}')
                action_path_index+=1
                state = itm.take_action(session_id=session_id, body=action)
            print(f'Scenario: {scenario.id} complete')
        print(f'Session {session_id} complete')
        path_index+=1
        action_path_index=0
        #If path is not enabled then we are assuming random actions and don't want to loop configs
        if (not paths["enabled"]):
            break
        

if __name__ == "__main__":
    main()
