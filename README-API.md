# swagger-client
This is the specification of the TA3 API for In The Moment (ITM).  Currently, the Evaluation API for TA2 supports functionality for the Phase 1 Evaluation.  The API is based on the OpenAPI 3.0.3 specification.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.4.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmTa2EvalApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | a unique session_id, as returned by /ta2/startSession
scenario_id = 'scenario_id_example' # str | The ID of the scenario for which to retrieve alignment target

try:
    # Retrieve alignment target for the scenario
    api_response = api_instance.get_alignment_target(session_id, scenario_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->get_alignment_target: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.ItmTa2EvalApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | a unique session_id, as returned by /ta2/startSession
scenario_id = 'scenario_id_example' # str | The ID of the scenario for which to retrieve available actions

try:
    # Get a list of currently available ADM actions
    api_response = api_instance.get_available_actions(session_id, scenario_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->get_available_actions: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.ItmTa2EvalApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | a unique session_id, as returned by /ta2/startSession
scenario_id = 'scenario_id_example' # str | the ID of the scenario for which to retrieve status

try:
    # Retrieve scenario state
    api_response = api_instance.get_scenario_state(session_id, scenario_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->get_scenario_state: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.ItmTa2EvalApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | a unique session_id, as returned by /ta2/startSession
target_id = 'target_id_example' # str | alignment target id

try:
    # Retrieve session alignment from TA1
    api_response = api_instance.get_session_alignment(session_id, target_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->get_session_alignment: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.ItmTa2EvalApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | a unique session_id, as returned by /ta2/startSession
body = swagger_client.Action() # Action | Encapsulation of the intended action by a DM in the context of the scenario (optional)

try:
    # Express intent to take an action within a scenario
    api_response = api_instance.intend_action(session_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->intend_action: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.ItmTa2EvalApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | a unique session_id, as returned by /ta2/startSession
scenario_id = 'scenario_id_example' # str | the scenario id to run; incompatible with /ta2/startSession's max_scenarios parameter (optional)

try:
    # Get the next scenario
    api_response = api_instance.start_scenario(session_id, scenario_id=scenario_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->start_scenario: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.ItmTa2EvalApi(swagger_client.ApiClient(configuration))
adm_name = 'adm_name_example' # str | A self-assigned ADM name.
session_type = 'session_type_example' # str | the type of session to start (`eval`, `test`, or a TA1 name)
adm_profile = 'adm_profile_example' # str | a profile of the ADM in terms of its alignment strategy (optional)
kdma_training = 'kdma_training_example' # str | whether this is a `full`, `solo`, or non-training session with TA2 (optional)
max_scenarios = 56 # int | the maximum number of scenarios requested, not supported in `eval` sessions (optional)

try:
    # Start a new session
    api_response = api_instance.start_session(adm_name, session_type, adm_profile=adm_profile, kdma_training=kdma_training, max_scenarios=max_scenarios)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->start_session: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.ItmTa2EvalApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | a unique session_id, as returned by /ta2/startSession
body = swagger_client.Action() # Action | Encapsulation of an action taken by a DM in the context of the scenario (optional)

try:
    # Take an action within a scenario
    api_response = api_instance.take_action(session_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->take_action: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ItmTa2EvalApi* | [**get_alignment_target**](docs/ItmTa2EvalApi.md#get_alignment_target) | **GET** /ta2/getAlignmentTarget | Retrieve alignment target for the scenario
*ItmTa2EvalApi* | [**get_available_actions**](docs/ItmTa2EvalApi.md#get_available_actions) | **GET** /ta2/{scenario_id}/getAvailableActions | Get a list of currently available ADM actions
*ItmTa2EvalApi* | [**get_scenario_state**](docs/ItmTa2EvalApi.md#get_scenario_state) | **GET** /ta2/{scenario_id}/getState | Retrieve scenario state
*ItmTa2EvalApi* | [**get_session_alignment**](docs/ItmTa2EvalApi.md#get_session_alignment) | **GET** /ta2/getSessionAlignment | Retrieve session alignment from TA1
*ItmTa2EvalApi* | [**intend_action**](docs/ItmTa2EvalApi.md#intend_action) | **POST** /ta2/intendAction | Express intent to take an action within a scenario
*ItmTa2EvalApi* | [**start_scenario**](docs/ItmTa2EvalApi.md#start_scenario) | **GET** /ta2/scenario | Get the next scenario
*ItmTa2EvalApi* | [**start_session**](docs/ItmTa2EvalApi.md#start_session) | **GET** /ta2/startSession | Start a new session
*ItmTa2EvalApi* | [**take_action**](docs/ItmTa2EvalApi.md#take_action) | **POST** /ta2/takeAction | Take an action within a scenario

## Documentation For Models

 - [Action](docs/Action.md)
 - [ActionMapping](docs/ActionMapping.md)
 - [ActionTypeEnum](docs/ActionTypeEnum.md)
 - [Aid](docs/Aid.md)
 - [AidTypeEnum](docs/AidTypeEnum.md)
 - [AirQualityEnum](docs/AirQualityEnum.md)
 - [AlignmentResults](docs/AlignmentResults.md)
 - [AlignmentSource](docs/AlignmentSource.md)
 - [AlignmentTarget](docs/AlignmentTarget.md)
 - [AmbientNoiseEnum](docs/AmbientNoiseEnum.md)
 - [AvpuLevelEnum](docs/AvpuLevelEnum.md)
 - [BloodOxygenEnum](docs/BloodOxygenEnum.md)
 - [BreathingLevelEnum](docs/BreathingLevelEnum.md)
 - [Character](docs/Character.md)
 - [CharacterRoleEnum](docs/CharacterRoleEnum.md)
 - [CharacterTagEnum](docs/CharacterTagEnum.md)
 - [CivilianPresenceEnum](docs/CivilianPresenceEnum.md)
 - [CommunicationCapabilityEnum](docs/CommunicationCapabilityEnum.md)
 - [Conditions](docs/Conditions.md)
 - [ConditionsCharacterVitals](docs/ConditionsCharacterVitals.md)
 - [DecisionEnvironment](docs/DecisionEnvironment.md)
 - [DemographicSexEnum](docs/DemographicSexEnum.md)
 - [Demographics](docs/Demographics.md)
 - [DirectnessEnum](docs/DirectnessEnum.md)
 - [EntityTypeEnum](docs/EntityTypeEnum.md)
 - [Environment](docs/Environment.md)
 - [Event](docs/Event.md)
 - [EventTypeEnum](docs/EventTypeEnum.md)
 - [FaunaTypeEnum](docs/FaunaTypeEnum.md)
 - [FloraTypeEnum](docs/FloraTypeEnum.md)
 - [HeartRateEnum](docs/HeartRateEnum.md)
 - [Injury](docs/Injury.md)
 - [InjuryLocationEnum](docs/InjuryLocationEnum.md)
 - [InjurySeverityEnum](docs/InjurySeverityEnum.md)
 - [InjuryStatusEnum](docs/InjuryStatusEnum.md)
 - [InjuryTriggerEnum](docs/InjuryTriggerEnum.md)
 - [InjuryTypeEnum](docs/InjuryTypeEnum.md)
 - [IntentEnum](docs/IntentEnum.md)
 - [KDEData](docs/KDEData.md)
 - [KDMAProfile](docs/KDMAProfile.md)
 - [KDMAValue](docs/KDMAValue.md)
 - [LightingTypeEnum](docs/LightingTypeEnum.md)
 - [MedicalPoliciesEnum](docs/MedicalPoliciesEnum.md)
 - [MentalStatusEnum](docs/MentalStatusEnum.md)
 - [MessageTypeEnum](docs/MessageTypeEnum.md)
 - [MetaInfo](docs/MetaInfo.md)
 - [MilitaryBranchEnum](docs/MilitaryBranchEnum.md)
 - [MilitaryDispositionEnum](docs/MilitaryDispositionEnum.md)
 - [MilitaryRankEnum](docs/MilitaryRankEnum.md)
 - [MilitaryRankTitleEnum](docs/MilitaryRankTitleEnum.md)
 - [Mission](docs/Mission.md)
 - [MissionImportanceEnum](docs/MissionImportanceEnum.md)
 - [MissionTypeEnum](docs/MissionTypeEnum.md)
 - [MovementRestrictionEnum](docs/MovementRestrictionEnum.md)
 - [OxygenLevelsEnum](docs/OxygenLevelsEnum.md)
 - [PeakNoiseEnum](docs/PeakNoiseEnum.md)
 - [PopulationDensityEnum](docs/PopulationDensityEnum.md)
 - [ProbeConfig](docs/ProbeConfig.md)
 - [ProbeResponse](docs/ProbeResponse.md)
 - [ProbeResponses](docs/ProbeResponses.md)
 - [RaceEnum](docs/RaceEnum.md)
 - [RapportEnum](docs/RapportEnum.md)
 - [Scenario](docs/Scenario.md)
 - [Scene](docs/Scene.md)
 - [SemanticTypeEnum](docs/SemanticTypeEnum.md)
 - [SimEnvironment](docs/SimEnvironment.md)
 - [SimEnvironmentTypeEnum](docs/SimEnvironmentTypeEnum.md)
 - [SkillLevelEnum](docs/SkillLevelEnum.md)
 - [SkillTypeEnum](docs/SkillTypeEnum.md)
 - [Skills](docs/Skills.md)
 - [SoundRestrictionEnum](docs/SoundRestrictionEnum.md)
 - [State](docs/State.md)
 - [Supplies](docs/Supplies.md)
 - [SupplyTypeEnum](docs/SupplyTypeEnum.md)
 - [Tagging](docs/Tagging.md)
 - [TerrainTypeEnum](docs/TerrainTypeEnum.md)
 - [Threat](docs/Threat.md)
 - [ThreatSeverityEnum](docs/ThreatSeverityEnum.md)
 - [ThreatState](docs/ThreatState.md)
 - [ThreatTypeEnum](docs/ThreatTypeEnum.md)
 - [VisibilityTypeEnum](docs/VisibilityTypeEnum.md)
 - [Vitals](docs/Vitals.md)
 - [WeatherTypeEnum](docs/WeatherTypeEnum.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author


