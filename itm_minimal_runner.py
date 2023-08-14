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
right forearm.The implementation of this function should be replaced with decision-making logic.
"""

import argparse
import swagger_client
import random
from typing import List
from swagger_client.configuration import Configuration
from swagger_client.api_client import ApiClient
from swagger_client.models import Scenario, State, AlignmentTarget, Action, Casualty

def get_next_action(scenario: Scenario, state: State, alignment_target: AlignmentTarget):
    return Action(scenario_id=scenario.id, action_type="APPLY_TREATMENT",
                  casualty_id=get_random_casualty_id(state),
                  parameters=[{"treatment": "Tourniquet"}, {"location": "right forearm"}],
                  justification=f"Justifcation {random.randint(0, 1000)}"
                  )

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

    args = parser.parse_args()
    if args.session:
        if args.session[0] not in ['soartech', 'adept', 'test']:
            parser.error("Invalid session type. It must be one of 'soartech', 'adept', or 'test'.")
        else:
            session_type = args.session[0]
    else:
        session_type = 'eval'
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
            max_scenarios=scenario_count
        )

    while True:
        scenario: Scenario = itm.start_scenario(session_id)
        if scenario.session_complete:
            break

        alignment_target: AlignmentTarget = itm.get_alignment_target(session_id, scenario.id)
        state: State = scenario.state
        while not state.scenario_complete:
            action = get_next_action(scenario, state, alignment_target)
            state = itm.take_action(session_id=session_id, body=action)
        print(f'scenario: {scenario.id} complete')
    print(f'Session complete')


if __name__ == "__main__":
    main()
