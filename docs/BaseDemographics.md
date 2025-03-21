# BaseDemographics

Basic properties about the character

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | **int** | the age of the character, omit if unknown | [optional] 
**sex** | [**DemographicSexEnum**](DemographicSexEnum.md) |  | 
**race** | [**RaceEnum**](RaceEnum.md) |  | 
**role** | [**CharacterRoleEnum**](CharacterRoleEnum.md) |  | [optional] 

## Example

```python
from swagger_client.models.base_demographics import BaseDemographics

# TODO update the JSON string below
json = "{}"
# create an instance of BaseDemographics from a JSON string
base_demographics_instance = BaseDemographics.from_json(json)
# print the JSON string representation of the object
print(BaseDemographics.to_json())

# convert the object into a dict
base_demographics_dict = base_demographics_instance.to_dict()
# create an instance of BaseDemographics from a dict
base_demographics_from_dict = BaseDemographics.from_dict(base_demographics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


