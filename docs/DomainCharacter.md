# DomainCharacter

a character in the scene, including injured patients, civilians, medics, etc.

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

## Example

```python
from swagger_client.models.domain_character import DomainCharacter

# TODO update the JSON string below
json = "{}"
# create an instance of DomainCharacter from a JSON string
domain_character_instance = DomainCharacter.from_json(json)
# print the JSON string representation of the object
print(DomainCharacter.to_json())

# convert the object into a dict
domain_character_dict = domain_character_instance.to_dict()
# create an instance of DomainCharacter from a dict
domain_character_from_dict = DomainCharacter.from_dict(domain_character_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


