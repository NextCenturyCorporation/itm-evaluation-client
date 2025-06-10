# BaseConditions

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
from swagger_client.models.base_conditions import BaseConditions

# TODO update the JSON string below
json = "{}"
# create an instance of BaseConditions from a JSON string
base_conditions_instance = BaseConditions.from_json(json)
# print the JSON string representation of the object
print(BaseConditions.to_json())

# convert the object into a dict
base_conditions_dict = base_conditions_instance.to_dict()
# create an instance of BaseConditions from a dict
base_conditions_from_dict = BaseConditions.from_dict(base_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


