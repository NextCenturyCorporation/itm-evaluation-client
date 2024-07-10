# Conditions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elapsed_time_lt** | **int** | True if the scenario elapsed time (in seconds) is less than the specified value | [optional] 
**elapsed_time_gt** | **int** | True if the scenario elapsed time (in seconds) is greater than the specified value | [optional] 
**actions** | **list[list[str]]** | True if any of the specified lists of actions have been taken; multiple action ID lists have \&quot;or\&quot; semantics; multiple action IDs within a list have \&quot;and\&quot; semantics | [optional] 
**probes** | **list[str]** | True if the specified list of probe_ids have been answered | [optional] 
**probe_responses** | **list[str]** | True if the specified list of probe responses (choice) have been sent | [optional] 
**character_vitals** | [**list[ConditionsCharacterVitals]**](ConditionsCharacterVitals.md) | True if any of the specified collection of vital values have been met for the specified character_id | [optional] 
**supplies** | [**list[Supplies]**](Supplies.md) | True if any of the specified supplies reach or go below the specified quantity | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

