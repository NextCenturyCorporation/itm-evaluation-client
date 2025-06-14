# Conditions

Conditions that specify whether to transition to the next scene or send a probe response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elapsed_time_lt** | **int** | True if the scenario elapsed time (in seconds) is less than the specified value | [optional] 
**elapsed_time_gt** | **int** | True if the scenario elapsed time (in seconds) is greater than the specified value | [optional] 
**actions** | **List[List[str]]** | True if any of the specified lists of actions have been taken; multiple action ID lists have \&quot;or\&quot; semantics; multiple action IDs within a list have \&quot;and\&quot; semantics | [optional] 
**probes** | **List[str]** | True if the specified list of probe_ids have been answered | [optional] 
**probe_responses** | **List[str]** | True if the specified list of probe responses (choice) have been sent | [optional] 

## Example

```python
from swagger_client.models.conditions import Conditions

# TODO update the JSON string below
json = "{}"
# create an instance of Conditions from a JSON string
conditions_instance = Conditions.from_json(json)
# print the JSON string representation of the object
print(Conditions.to_json())

# convert the object into a dict
conditions_dict = conditions_instance.to_dict()
# create an instance of Conditions from a dict
conditions_from_dict = Conditions.from_dict(conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


