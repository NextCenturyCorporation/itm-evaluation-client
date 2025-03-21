# Injury

An injury on a character.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**InjuryTypeEnum**](InjuryTypeEnum.md) |  | 
**location** | [**InjuryLocationEnum**](InjuryLocationEnum.md) |  | 
**severity** | [**InjurySeverityEnum**](InjurySeverityEnum.md) |  | [optional] 
**status** | [**InjuryStatusEnum**](InjuryStatusEnum.md) |  | 
**source_character** | **str** | The character id of the person responsible for the injury, subject to the character&#39;s &#x60;directness_of_causality&#x60; | [optional] 
**treatments_required** | **int** | The number of successful treatments required to treat the injury fully, which sets &#x60;status&#x60; to &#x60;treated&#x60; | [optional] 
**treatments_applied** | **int** | The number of successful treatments applied to the injury | [optional] [default to 0]

## Example

```python
from swagger_client.models.injury import Injury

# TODO update the JSON string below
json = "{}"
# create an instance of Injury from a JSON string
injury_instance = Injury.from_json(json)
# print the JSON string representation of the object
print(Injury.to_json())

# convert the object into a dict
injury_dict = injury_instance.to_dict()
# create an instance of Injury from a dict
injury_from_dict = Injury.from_dict(injury_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


