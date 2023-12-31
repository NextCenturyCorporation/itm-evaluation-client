# State

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unstructured** | **str** | text description of current state | 
**elapsed_time** | **float** | the elapsed time (in minutes) since the scenario started | [optional] 
**scenario_complete** | **bool** | set to true if the scenario is complete; subsequent calls involving that scenario will return an error code | [optional] 
**mission** | [**Mission**](Mission.md) |  | [optional] 
**environment** | [**Environment**](Environment.md) |  | [optional] 
**threat_state** | [**ThreatState**](ThreatState.md) |  | [optional] 
**supplies** | [**list[Supplies]**](Supplies.md) | a list of medical supplies available to the DM | [optional] 
**characters** | [**list[Character]**](Character.md) | the list of characters in the scenario | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

