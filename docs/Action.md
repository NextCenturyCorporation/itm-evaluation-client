# Action

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **str** | A unique action ID within the scenario | 
**action_type** | [**ActionTypeEnum**](ActionTypeEnum.md) |  | 
**intent_action** | **bool** | Whether this action is to be taken or intended | [optional] [default to False]
**unstructured** | **str** | Natural language, plain text description of the action | [optional] 
**character_id** | **str** | The ID of the character being acted upon | [optional] 
**threat_state** | [**ThreatState**](ThreatState.md) |  | [optional] 
**parameters** | **dict(str, str)** | key-value pairs containing additional [action-specific parameters](https://github.com/NextCenturyCorporation/itm-evaluation-client?tab&#x3D;readme-ov-file#available-actions) | [optional] 
**justification** | **str** | A justification of the action taken | [optional] 
**kdma_association** | **dict(str, float)** | KDMA associations for this choice, if provided by TA1 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

