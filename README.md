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

 In order to hit a non-locally running server (localhost) set the below environment variables:
 - TA3_PORT (Default: 8080)
 - TA3_HOSTNAME (Default: 127.0.0.1)

### Running the ADM minimal runner

 To see additional details regarding modifying this minimal runner to be a TA2 client, see the comments at the top of `itm_minimal_runner.py`.
 These comments also describe how to configure the ADM minimal runner to choose pre-configured action paths.

 Run `itm_minimal_runner.py` in the root directory:

```
usage: itm_minimal_runner.py [-h] --adm_name ADM_NAME [--session [session_type [scenario_count ...]]] [--eval] [--kdma_training]

Runs ADM scenarios.

options:
  -h, --help            show this help message and exit
  --adm_name ADM_NAME   Specify the ADM name
  --session [session_type [scenario_count ...]]
                        Specify session type and scenario count. Session type can be test, adept, or soartech. If you want to run through all available scenarios without repeating do not use the scenario_count argument
  --eval                Run an evaluation session. Supercedes --session and is the default if nothing is specified.
  --kdma_training       Put the server in training mode in which it shows the kdma association for each action choice.
                        Not supported in eval sessions.
```
 
### Running the Human input simulator

The Human input simulator is used for testing specific action/parameter sequences or for otherwise simulating a human DM.

Inside the root directory, run `itm_human_input.py`:

```
usage: itm_human_input.py [-h] [--session [session_type [scenario_count ...]]] [--eval] [--kdma_training]

Runs Human input simulator.

options:
  -h, --help            show this help message and exit
  --session [session_type [scenario_count ...]]
                        Specify session type and scenario count. Session type can be eval, adept, or soartech. If you want to run through all available scenarios without repeating do not use the scenario_count argument. Default: eval
  --eval                Run an evaluation session. Supercedes --session and is the default if nothing is specified.
  --kdma_training       Put the server in training mode in which it shows the kdma association for each action choice.
                        Not supported in eval sessions.
```

### Available Actions

* `APPLY_TREATMENT`
* * requires `character_id`
* * requires parameter `treatment` with a value taken from the `SupplyType` enum object.
* * requires parameter `location` with a value taken from the `InjuryLocation` enum object.
* `CHECK_ALL_VITALS`
* * requires `character_id`
* `CHECK_PULSE`
* * requires `character_id`
* `CHECK_RESPIRATION`
* * requires `character_id`
* `DIRECT_MOBILE_CHARACTERS`
* * no further requirements
* `END_SCENE`
* * no further requirements
* `MOVE_TO_EVAC`
* * requires `character_id`
* `SEARCH`
* * no further requirements
* `SITREP`
* * accepts **optional** `character_id`
* `TAG_CHARACTER`
* * requires `character_id`
* * requires parameter `category` with a value taken from the `TagLabel` enum object.

## Updating models
This requires JDK 8 or higher to run the gradle tool.

The models in swagger_server/models are generated from swagger_server/swagger/swagger.yaml
If this file is updated the models will need to be re-generated and checked in.
Run `./gradlew` to do this.
