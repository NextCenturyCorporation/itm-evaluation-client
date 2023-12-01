import argparse
from itm import ADMScenarioRunner

def main():
    parser = argparse.ArgumentParser(description='Runs ADM scenarios.')
    parser.add_argument('--save', action='store_true', default=False, help=\
                        'Tell the ADM server to save session history.')
    parser.add_argument('--session', nargs='*', default=[], metavar=('session_type', 'scenario_count'), help=\
                        'Specify session type and scenario count. '
                        'Session type can be eval, adept, or soartech. '
                        'If you want to run through all available scenarios without repeating do not use the scenario_count argument')
    parser.add_argument('--eval', action='store_true', default=False, help=\
                        'Run an eval session')

    args = parser.parse_args()

    if args.session:
        if args.session[0] not in ['soartech', 'adept', 'eval']:
            parser.error("Invalid session type. It must be one of 'soartech', 'adept', or 'eval'.")
        else:
            session_type = args.session[0]
    else:
        session_type = 'eval'
    if args.eval:
        session_type = 'eval'
    scenario_count = int(args.session[1]) if len(args.session) > 1 else 0

    adm = ADMScenarioRunner(session_type, args.save, scenario_count)
    adm.run()

if __name__ == "__main__":
    main()
