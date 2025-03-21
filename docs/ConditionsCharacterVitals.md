# ConditionsCharacterVitals

True if all vitals values have been met by the specified character_id

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**character_id** | **str** | The ID of the character in question | 
**vitals** | [**Vitals**](Vitals.md) |  | 

## Example

```python
from swagger_client.models.conditions_character_vitals import ConditionsCharacterVitals

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionsCharacterVitals from a JSON string
conditions_character_vitals_instance = ConditionsCharacterVitals.from_json(json)
# print the JSON string representation of the object
print(ConditionsCharacterVitals.to_json())

# convert the object into a dict
conditions_character_vitals_dict = conditions_character_vitals_instance.to_dict()
# create an instance of ConditionsCharacterVitals from a dict
conditions_character_vitals_from_dict = ConditionsCharacterVitals.from_dict(conditions_character_vitals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


