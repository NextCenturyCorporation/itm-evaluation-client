# State

The complete state of the scene or scenario

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
from swagger_client.models.state import State

# TODO update the JSON string below
json = "{}"
# create an instance of State from a JSON string
state_instance = State.from_json(json)
# print the JSON string representation of the object
print(State.to_json())

# convert the object into a dict
state_dict = state_instance.to_dict()
# create an instance of State from a dict
state_from_dict = State.from_dict(state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


