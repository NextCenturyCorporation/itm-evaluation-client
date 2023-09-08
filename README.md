# In the Moment (ITM) - TA3 Client

This README provides a guide to set up and run the TA3 ITM sample client applications.

## Prerequisites

Ensure you have Python 3.10 installed on your system. If you don't have it installed, you can download it from the [official Python website](https://www.python.org/downloads/).

## Setup

1. First, we need to setup a Python virtual environment. Navigate to the directory where you cloned the repository and run the following command to create a new virtual environment:

```
python -m venv venv
```

2. Activate the newly created virtual environment with:

```
source venv/bin/activate
```

On Windows, the method to activate depends on the shell:
- Git Bash: `source venv/Scripts/activate`
- PowerShell: `venv\Scripts\Activate.ps1`
- cmd.exe: `venv\Scripts\activate.bat`

## Running a TA3 Client

To run a client, you will need to connect to a server. Please ensure that the server is running before you start a client.
Then install the clients via:

```
pip3 install -r requirements.txt

```

### Running the ADM minimal runner

 To see additional details regarding modifying this minimal runner to be a TA2 client, see the comments at the top of `itm_minimal_runner.py`.
 These comments also describe how to configure the ADM minimal runner to choose pre-configured action paths.

 Run `itm_minimal_runner.py` in the root directory:

```
usage: itm_minimal_runner.py [-h] --adm_name ADM_NAME [--session [session_type [scenario_count ...]]] [--eval]

Runs ADM scenarios.

options:
  -h, --help            show this help message and exit
  --adm_name ADM_NAME   Specify the ADM name
  --session [session_type [scenario_count ...]]
                        Specify session type and scenario count. Session type can be test, adept, or soartech. If you want to run through all available scenarios without repeating do not use the scenario_count argument
  --eval                Run an evaluation session. Supercedes --session and is the default if nothing is specified. Implies --db.
  --kdma_training [KDMA_TRAINING]
                        Put the server in training mode in which it shows the kdma association for each action choice.  True or False.
```

### Running the Human input simulator (DEPRECATED)

The Human input simulator has not been updated since MVP.  It may be removed entirely in a future release.

Inside the root directory, run `itm_human_input.py`:

```
usage: itm_human_input.py [-h] [--db] [--session [session_type [scenario_count ...]]] [--eval]

Runs Human input simulator.

options:
  -h, --help            show this help message and exit
  --db                  Put the output in the MongoDB (ensure that the itm_dashboard docker container is running) and save a json output file locally inside itm_server/itm_mvp_local_output/
  --session [session_type [scenario_count ...]]
                        Specify session type and scenario count. Session type can be test, adept, or soartech. If you want to run through all available scenarios without repeating do not use the scenario_count argument
  --eval                Run an evaluation session. Supercedes --session and is the default if nothing is specified. Implies --db.
```

### Available Actions

* `APPLY_TREATMENT`
* * requires `casualty_id`
* * requires parameter `treatment` with a value taken from type enum in `Supplies` object.
* * requires parameter `location` with a value taken from location enum in `Injury` object.
* `CHECK_ALL_VITALS`
* * requires `casualty_id`
* `CHECK_PULSE`
* * requires `casualty_id`
* `CHECK_RESPIRATION`
* * requires `casualty_id`
* `DIRECT_MOBILE_CASUALTIES`
* * no further requirements
* `MOVE_TO_EVAC`
* * requires `casualty_id`
* `SITREP`
* * accepts **optional** `casualty_id`
* `TAG_CASUALTY`
* * requires `casualty_id`
* * requires parameter `category` with a value taken from `tagLabel` enum in `TriageCategory` object.

