# DecisionEnvironment

Environmental elements that impact decision-making

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unstructured** | **str** | Natural language, plain text description of decision-impacting environmental factors | 
**aid** | [**List[Aid]**](Aid.md) | A list of available forms of aid | [optional] 
**movement_restriction** | [**MovementRestrictionEnum**](MovementRestrictionEnum.md) |  | [optional] 
**sound_restriction** | [**SoundRestrictionEnum**](SoundRestrictionEnum.md) |  | [optional] 
**oxygen_levels** | [**OxygenLevelsEnum**](OxygenLevelsEnum.md) |  | [optional] 
**population_density** | [**PopulationDensityEnum**](PopulationDensityEnum.md) |  | [optional] 
**injury_triggers** | [**InjuryTriggerEnum**](InjuryTriggerEnum.md) |  | [optional] 
**air_quality** | [**AirQualityEnum**](AirQualityEnum.md) |  | [optional] 
**city_infrastructure** | **str** | Refers to building/city infrastructure that should be noted and known (safe house, etc.) | [optional] 

## Example

```python
from swagger_client.models.decision_environment import DecisionEnvironment

# TODO update the JSON string below
json = "{}"
# create an instance of DecisionEnvironment from a JSON string
decision_environment_instance = DecisionEnvironment.from_json(json)
# print the JSON string representation of the object
print(DecisionEnvironment.to_json())

# convert the object into a dict
decision_environment_dict = decision_environment_instance.to_dict()
# create an instance of DecisionEnvironment from a dict
decision_environment_from_dict = DecisionEnvironment.from_dict(decision_environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


