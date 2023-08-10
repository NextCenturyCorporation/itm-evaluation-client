# Action

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scenario_id** | **str** | scenario ID this probe is for | 
**action_type** | **str** | The action type taken from a controlled vocabulary | 
**casualty_id** | **str** | The ID of the casualty being acted upon | 
**unstructured** | **str** | a plain text unstructured description of the action | [optional] 
**justification** | **str** | A justification of the action taken | [optional] 
**parameter1** | **str** | Possible approach-- the first action-specific parameter; see action reference | [optional] 
**parameter2** | **str** | Possible approach-- the second action-specific parameter; see action reference | [optional] 
**parameters** | **list[dict(str, str)]** | Possible approach-- an array of parameters | [optional] 
**supplies** | [**list[Supplies]**](Supplies.md) | Possible approach-- a list of supplies used as part of the action | [optional] 
**timestamp** | **str** | The current time in the scenario as populated by TA3 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

