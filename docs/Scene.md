# Scene

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | The order the scene appears in the scenario | 
**state** | [**State**](State.md) |  | [optional] 
**end_scene_allowed** | **bool** | Whether ADMs can explicitly end the scene | 
**probe_config** | [**list[ProbeConfig]**](ProbeConfig.md) | TA1-provided probe configuration, ignored by TA3 | [optional] 
**tagging** | [**Tagging**](Tagging.md) |  | [optional] 
**action_mapping** | [**list[Action]**](Action.md) | List of actions with details of how those actions map to probe responses | 
**restricted_actions** | [**list[ActionTypeEnum]**](ActionTypeEnum.md) | List of actions that will be excluded from get_available_actions | [optional] 
**transition_semantics** | [**SemanticTypeEnum**](SemanticTypeEnum.md) |  | [optional] 
**transitions** | [**Conditions**](Conditions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
