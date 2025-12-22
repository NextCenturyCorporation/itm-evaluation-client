# Scenario

a scenario requiring decisions by a decision-maker

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | a globally unique id for the scenario | 
**name** | **str** | human-readable scenario name, not necessarily unique | 
**alt_id** | **str** | an alternate unique id for the scenario; there is a 1-to-1 mapping from id to alt_id | [optional] 
**alt_name** | **str** | an alternate name for the scenario; there is a 1-to-1 mapping from name to alt_name | [optional] 
**first_scene** | **str** | indicates the first/opening scene ID in the scenario | [optional] 
**session_complete** | **bool** | set to true if the session is complete; that is, there are no more scenarios | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**scenes** | [**List[Scene]**](Scene.md) | A list of specification for all scenes in the scenario | [optional] 

## Example

```python
from swagger_client.models.scenario import Scenario

# TODO update the JSON string below
json = "{}"
# create an instance of Scenario from a JSON string
scenario_instance = Scenario.from_json(json)
# print the JSON string representation of the object
print(Scenario.to_json())

# convert the object into a dict
scenario_dict = scenario_instance.to_dict()
# create an instance of Scenario from a dict
scenario_from_dict = Scenario.from_dict(scenario_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


