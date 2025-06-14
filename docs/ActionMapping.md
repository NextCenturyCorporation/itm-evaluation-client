# ActionMapping

Details for how a given action maps to a probe response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **str** | A unique action ID within the scenario | 
**action_type** | [**ActionTypeEnum**](ActionTypeEnum.md) |  | 
**unstructured** | **str** | Natural language, plain text description of the action | 
**repeatable** | **bool** | Whether or not this action should remain after it&#39;s selected by an ADM | [optional] [default to False]
**character_id** | **str** | The ID of the character being acted upon | [optional] 
**intent_action** | **bool** | Whether this mapping is to take an action or to intend one | [optional] [default to False]
**threat_state** | [**ThreatState**](ThreatState.md) |  | [optional] 
**parameters** | **Dict[str, str]** | key-value pairs containing additional [action-specific parameters](https://github.com/NextCenturyCorporation/itm-evaluation-client?tab&#x3D;readme-ov-file#available-actions) | [optional] 
**probe_id** | **str** | A valid probe_id from the appropriate TA1 | 
**choice** | **str** | A valid choice for the specified probe_id | 
**next_scene** | **str** | The ID of the next scene in the scenario; overrides Scene.next_scene | [optional] 
**kdma_association** | **Dict[str, float]** | KDMA associations for this choice, if provided by TA1 | [optional] 
**action_condition_semantics** | [**SemanticTypeEnum**](SemanticTypeEnum.md) |  | [optional] [default to SemanticTypeEnum.AND]
**action_conditions** | [**Conditions**](Conditions.md) |  | [optional] 
**probe_condition_semantics** | [**SemanticTypeEnum**](SemanticTypeEnum.md) |  | [optional] [default to SemanticTypeEnum.AND]
**probe_conditions** | [**Conditions**](Conditions.md) |  | [optional] 

## Example

```python
from swagger_client.models.action_mapping import ActionMapping

# TODO update the JSON string below
json = "{}"
# create an instance of ActionMapping from a JSON string
action_mapping_instance = ActionMapping.from_json(json)
# print the JSON string representation of the object
print(ActionMapping.to_json())

# convert the object into a dict
action_mapping_dict = action_mapping_instance.to_dict()
# create an instance of ActionMapping from a dict
action_mapping_from_dict = ActionMapping.from_dict(action_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


