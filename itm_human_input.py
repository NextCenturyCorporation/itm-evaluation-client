import argparse
from itm import ITMHumanScenarioRunner

def main():

    parser = argparse.ArgumentParser(description='Runs Human input simulator.')
    parser.add_argument('--session', nargs='*', default=[], metavar=('session_type', 'scenario_count'), help=\
                        'Specify session type and scenario count. '
                        'Session type can be eval, adept, or soartech. '
                        'If you want to run through all available scenarios without repeating do not use the scenario_count argument')
    parser.add_argument('--eval', action='store_true', default=False, help=\
                        'Run an evaluation session. '
                        'Supercedes --session and is the default if nothing is specified. ')
    parser.add_argument('--kdma_training', action='store_true', default=False,
                        help='Put the server in training mode in which it shows the kdma '
                        'association for each action choice. Not supported in eval sessions.')
    parser.add_argument('--scenario', type=str,
                        help='Specify a scenario_id to run. Incompatible with scenario_count '
                        'and --eval')

    args = parser.parse_args()
    scenario_id = args.scenario
    if args.session:
        if args.session[0] not in ['soartech', 'adept', 'eval']:
            parser.error("Invalid session type. It must be one of 'soartech', 'adept', or 'eval'.")
        else:
            session_type = args.session[0]
    else:
        session_type = 'eval'
    if args.eval:
        session_type = 'eval'
    if session_type == 'eval' and scenario_id:
        parser.error("Specifying a scenario_id is not supported in eval sessions.")
    if args.kdma_training and session_type == 'eval':
            parser.error("Training mode is not supported in eval sessions.")
    scenario_count = int(args.session[1]) if len(args.session) > 1 else 0
    if scenario_count > 0 and scenario_id:
        parser.error("Specifying a scenario_id is incompatible with specifying a scenario_count.")

    if scenario_id:
        runner = ITMHumanScenarioRunner(session_type, args.kdma_training, scenario_count, scenario_id)
    else:
        runner = ITMHumanScenarioRunner(session_type, args.kdma_training, scenario_count)
    runner.run()

if __name__ == "__main__":
    main()
