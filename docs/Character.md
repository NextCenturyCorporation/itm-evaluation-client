# Character

a character in the scene

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unstructured_postassess** | **str** | unstructured description updated after character assessment | [optional] 
**has_blanket** | **bool** | whether or not this character has a blanket (either wrapped around or underneath) | [optional] [default to False]
**intent** | [**IntentEnum**](IntentEnum.md) |  | [optional] 
**directness_of_causality** | [**DirectnessEnum**](DirectnessEnum.md) |  | [optional] 
**injuries** | [**List[Injury]**](Injury.md) | A list of Injuries for the character | [optional] 
**vitals** | [**Vitals**](Vitals.md) |  | [optional] 
**visited** | **bool** | whether or not this character has been visited by the ADM in the current scenario | [optional] [default to False]
**tag** | [**CharacterTagEnum**](CharacterTagEnum.md) |  | [optional] 
**id** | **str** | A unique character ID throughout the scenario | 
**name** | **str** | display name, as in a dashboard | 
**unstructured** | **str** | Natural language, plain text description of the character | 
**demographics** | [**Demographics**](Demographics.md) |  | 
**rapport** | [**RapportEnum**](RapportEnum.md) |  | [optional] 
**unseen** | **bool** | whether or not this character is visible in the scene or merely heard or reported about from a nearby location | [optional] [default to False]

## Example

```python
from swagger_client.models.character import Character

# TODO update the JSON string below
json = "{}"
# create an instance of Character from a JSON string
character_instance = Character.from_json(json)
# print the JSON string representation of the object
print(Character.to_json())

# convert the object into a dict
character_dict = character_instance.to_dict()
# create an instance of Character from a dict
character_from_dict = Character.from_dict(character_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


