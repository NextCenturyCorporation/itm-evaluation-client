# BasicState

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unstructured** | **str** | Natural language, plain text description of a scene&#x27;s state | 
**elapsed_time** | **int** | The simulated elapsed time (in seconds) since the scenario started | [optional] 
**meta_info** | [**MetaInfo**](MetaInfo.md) |  | [optional] 
**events** | [**list[Event]**](Event.md) | A list of scenario events to inform decision-making | [optional] 
**threat_state** | [**ThreatState**](ThreatState.md) |  | [optional] 
**characters** | [**list[Character]**](Character.md) | A list of characters in the scene | 
**scenario_complete** | **bool** | set to true if the scenario is complete; subsequent calls involving that scenario will return an error code | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

