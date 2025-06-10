# Action

An action taken by an ADM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **str** | A unique action ID within the scenario | 
**action_type** | [**ActionTypeEnum**](ActionTypeEnum.md) |  | 
**intent_action** | **bool** | Whether this action is to be taken or intended | [optional] [default to False]
**unstructured** | **str** | Natural language, plain text description of the action | [optional] 
**character_id** | **str** | The ID of the character being acted upon | [optional] 
**threat_state** | [**ThreatState**](ThreatState.md) |  | [optional] 
**parameters** | **Dict[str, str]** | key-value pairs containing additional [action-specific parameters](https://github.com/NextCenturyCorporation/itm-evaluation-client?tab&#x3D;readme-ov-file#available-actions) | [optional] 
**justification** | **str** | A justification of the action taken | [optional] 
**kdma_association** | **Dict[str, float]** | KDMA associations for this choice, if provided by TA1 | [optional] 

## Example

```python
from swagger_client.models.action import Action

# TODO update the JSON string below
json = "{}"
# create an instance of Action from a JSON string
action_instance = Action.from_json(json)
# print the JSON string representation of the object
print(Action.to_json())

# convert the object into a dict
action_dict = action_instance.to_dict()
# create an instance of Action from a dict
action_from_dict = Action.from_dict(action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


