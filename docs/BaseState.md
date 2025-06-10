# BaseState

Base state for the scene or scenario

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unstructured** | **str** | Natural language, plain text description of a scene&#39;s state | 
**elapsed_time** | **int** | The simulated elapsed time (in seconds) since the scenario started | [optional] 
**meta_info** | [**MetaInfo**](MetaInfo.md) |  | [optional] 
**events** | [**List[Event]**](Event.md) | A list of scenario events to inform decision-making | [optional] 
**threat_state** | [**ThreatState**](ThreatState.md) |  | [optional] 
**characters** | [**List[Character]**](Character.md) | A list of characters in the scene | 
**scenario_complete** | **bool** | set to true if the scenario is complete; subsequent calls involving that scenario will return an error code | [optional] 

## Example

```python
from swagger_client.models.base_state import BaseState

# TODO update the JSON string below
json = "{}"
# create an instance of BaseState from a JSON string
base_state_instance = BaseState.from_json(json)
# print the JSON string representation of the object
print(BaseState.to_json())

# convert the object into a dict
base_state_dict = base_state_instance.to_dict()
# create an instance of BaseState from a dict
base_state_from_dict = BaseState.from_dict(base_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


