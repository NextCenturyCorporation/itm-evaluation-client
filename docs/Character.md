# Character

a character in the scene

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**medical_condition** | **float** | The treatment priority/urgency of a patient&#39;s medical condition, 0-1 scale | [optional] 
**attribute_rating** | **float** | A scenario-specific characteristic of the patient or situation regarding the patient, 0-1 scale:   Merit Focus (MF): degree of blame for a patient: 0.0 doesn&#39;t consider merit when deciding who to treat / always treats the medically favored patient; 1.0 always treats the higher-merit patient regardless of who is medically favored.   Affiliation Focus (AF): degree of closeness for a patient: 0.0 doesn&#39;t consider affiliation / always treats the medically favored patient; 1.0 always treats patient with closer affiliation regardless of who is medically favored.   Search vs. Stay (SS): urgency to search for/treat a patient: 0.0 always stays despite how urgent the need is to treat patient in next room; 1.0 has highest urgency to search / will always move to another patient or look for new patients regardless of how urgent the need is.   Personal Safety Focus (PS): amount of danger to reach a patient: 0.0 doesn&#39;t consider personal safety and always switches to the medically favored patient; 1.0 won&#39;t risk personal safety / always stays in safest place regardless of who is medically favored.  | [optional] 
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


