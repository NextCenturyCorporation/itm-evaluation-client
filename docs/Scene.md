# Scene

the specification for a scene in the scenario

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The scene ID, unique throughout the scenario | 
**state** | [**State**](State.md) |  | [optional] 
**next_scene** | **str** | The ID of the default next scene in the scenario; if empty or missing, then by default this is the last scene. | [optional] 
**end_scene_allowed** | **bool** | Whether ADMs can explicitly end the scene | 
**persist_characters** | **bool** | Whether characters should persist from the previous scene | [optional] 
**removed_characters** | **List[str]** | List of character ids to be removed from the scene | [optional] 
**probe_config** | [**List[ProbeConfig]**](ProbeConfig.md) | TA1-provided probe configuration, ignored by TA3 | [optional] 
**action_mapping** | [**List[ActionMapping]**](ActionMapping.md) | List of actions with details of how those actions map to probe responses | 
**restricted_actions** | [**List[ActionTypeEnum]**](ActionTypeEnum.md) | List of actions that will be excluded from get_available_actions | [optional] 
**transition_semantics** | [**SemanticTypeEnum**](SemanticTypeEnum.md) |  | [optional] [default to SemanticTypeEnum.AND]
**transitions** | [**Conditions**](Conditions.md) |  | [optional] 

## Example

```python
from swagger_client.models.scene import Scene

# TODO update the JSON string below
json = "{}"
# create an instance of Scene from a JSON string
scene_instance = Scene.from_json(json)
# print the JSON string representation of the object
print(Scene.to_json())

# convert the object into a dict
scene_dict = scene_instance.to_dict()
# create an instance of Scene from a dict
scene_from_dict = Scene.from_dict(scene_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


