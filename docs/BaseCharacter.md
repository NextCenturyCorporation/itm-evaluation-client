# BaseCharacter

a character in the scene

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique character ID throughout the scenario | 
**name** | **str** | display name, as in a dashboard | 
**unstructured** | **str** | Natural language, plain text description of the character | 
**demographics** | [**Demographics**](Demographics.md) |  | 
**rapport** | [**RapportEnum**](RapportEnum.md) |  | [optional] 
**unseen** | **bool** | whether or not this character is visible in the scene or merely heard or reported about from a nearby location | [optional] [default to False]

## Example

```python
from swagger_client.models.base_character import BaseCharacter

# TODO update the JSON string below
json = "{}"
# create an instance of BaseCharacter from a JSON string
base_character_instance = BaseCharacter.from_json(json)
# print the JSON string representation of the object
print(BaseCharacter.to_json())

# convert the object into a dict
base_character_dict = base_character_instance.to_dict()
# create an instance of BaseCharacter from a dict
base_character_from_dict = BaseCharacter.from_dict(base_character_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


