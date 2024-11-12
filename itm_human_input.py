import argparse
from itm import ITMHumanScenarioRunner

def main():

    parser = argparse.ArgumentParser(description='Runs Human input simulator.')
    parser.add_argument('--session', required=True, metavar='session_type', help=\
                        'Specify session type. Session type must be `test`, `eval`, `adept`, or `soartech`.')
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

    if scenario_id:
        runner = ITMHumanScenarioRunner(session_type, args.training, scenario_count, scenario_id)
    else:
        runner = ITMHumanScenarioRunner(session_type, args.training, scenario_count)
    runner.run()

if __name__ == "__main__":
    main()
