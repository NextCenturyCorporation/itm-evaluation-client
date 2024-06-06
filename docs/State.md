# State

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unstructured** | **str** | Natural language, plain text description of a scene&#x27;s state | 
**meta_info** | [**MetaInfo**](MetaInfo.md) |  | [optional] 
**scenario_complete** | **bool** | set to true if the scenario is complete; subsequent calls involving that scenario will return an error code | [optional] 
**mission** | [**Mission**](Mission.md) |  | [optional] 
**environment** | [**Environment**](Environment.md) |  | 
**threat_state** | [**ThreatState**](ThreatState.md) |  | [optional] 
**supplies** | [**list[Supplies]**](Supplies.md) | A list of supplies available to the medic | 
**characters** | [**list[Character]**](Character.md) | A list of characters in the scene, including injured patients, civilians, medics, etc. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

