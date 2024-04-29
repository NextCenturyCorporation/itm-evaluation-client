import argparse
from itm import ADMScenarioRunner

def main():
    parser = argparse.ArgumentParser(description='Runs ADM simulator.')
    parser.add_argument('--profile', metavar='adm_profile', required=False, 
                        help='Specify the ADM profile in terms of its alignment strategy')
    parser.add_argument('--session', required=True, metavar='session_type', help=\
                        'Specify session type. Session type must be `eval`, `adept`, or `soartech`. ')
    parser.add_argument('--count', type=int, metavar='scenario_count', help=\
                        'Run the specified number of scenarios. Otherwise, will run scenarios in '
                        'accordance with server defaults. Not supported in `eval` sessions.')
    parser.add_argument('--scenario', type=str, metavar='scenario_id',
                        help='Specify a scenario_id to run. Incompatible with count parameter '
                        'and `eval` sessions.')

    args = parser.parse_args()
    scenario_id = args.scenario
    scenario_count = args.count
    if args.session:
        if args.session not in ['soartech', 'adept', 'eval']:
            parser.error("Invalid session type. It must be one of 'soartech', 'adept', or 'eval'.")
        else:
            session_type = args.session

    if session_type == 'eval':
        if scenario_id:
            parser.error("Specifying a scenario_id is not supported in eval sessions.")
        if scenario_count is not None:
            parser.error("Scenario count is not supported in eval sessions.")

    if scenario_count is not None:
        if scenario_count < 1:
            parser.error("Scenario count must be a positive integer.")
    else:
        scenario_count = 0

    if scenario_count > 0 and scenario_id:
        parser.error("--scenario is incompatible with --count.")

    if scenario_id:
        adm = ADMScenarioRunner(session_type, args.profile, scenario_count, scenario_id)
    else:
        adm = ADMScenarioRunner(session_type, args.profile, scenario_count)
    adm.run()

if __name__ == "__main__":
    main()
