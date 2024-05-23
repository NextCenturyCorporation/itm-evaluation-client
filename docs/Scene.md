# Scene

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The scene ID, unique throughout the scenario | 
**state** | [**State**](State.md) |  | [optional] 
**next_scene** | **str** | The ID of the default next scene in the scenario; if empty or missing, then by default this is the last scene. | [optional] 
**end_scene_allowed** | **bool** | Whether ADMs can explicitly end the scene | 
**persist_characters** | **bool** | Whether characters should persist from the previous scene | [optional] 
**removed_characters** | **list** | List of character ids to be removed from the scene | [optional] 
**probe_config** | [**list[ProbeConfig]**](ProbeConfig.md) | TA1-provided probe configuration, ignored by TA3 | [optional] 
**tagging** | [**Tagging**](Tagging.md) |  | [optional] 
**action_mapping** | [**list[ActionMapping]**](ActionMapping.md) | List of actions with details of how those actions map to probe responses | 
**restricted_actions** | [**list[ActionTypeEnum]**](ActionTypeEnum.md) | List of actions that will be excluded from get_available_actions | [optional] 
**transition_semantics** | [**SemanticTypeEnum**](SemanticTypeEnum.md) |  | [optional] 
**transitions** | [**Conditions**](Conditions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

