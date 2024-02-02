# Action

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **str** | A unique action ID within the scenario | 
**action_type** | [**ActionTypeEnum**](ActionTypeEnum.md) |  | 
**unstructured** | **str** | Natural language, plain text description of the action | 
**repeatable** | **bool** | Whether or not this action should remain after it&#x27;s selected by an ADM | [optional] [default to False]
**character_id** | **str** | The ID of the character being acted upon | [optional] 
**parameters** | **dict(str, str)** | key-value pairs containing additional [action-specific parameters](https://github.com/NextCenturyCorporation/itm-evaluation-client?tab&#x3D;readme-ov-file#available-actions) | [optional] 
**probe_id** | **str** | A valid probe_id from the appropriate TA1 | [optional] 
**choice** | **str** | A valid choice for the specified probe_id | [optional] 
**next_scene** | **int** | The next scene in the scenario, by index | [optional] 
**justification** | **str** | A justification of the action taken | [optional] 
**kdma_association** | **dict(str, float)** | KDMA associations for this choice, if provided by TA1 | [optional] 
**condition_semantics** | [**SemanticTypeEnum**](SemanticTypeEnum.md) |  | [optional] 
**conditions** | [**Conditions**](Conditions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

