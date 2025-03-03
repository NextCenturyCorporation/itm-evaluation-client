# Demographics

Basic properties about the character

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**military_disposition** | [**MilitaryDispositionEnum**](MilitaryDispositionEnum.md) |  | [optional] 
**military_branch** | [**MilitaryBranchEnum**](MilitaryBranchEnum.md) |  | [optional] 
**rank** | [**MilitaryRankEnum**](MilitaryRankEnum.md) |  | [optional] 
**rank_title** | [**MilitaryRankTitleEnum**](MilitaryRankTitleEnum.md) |  | [optional] 
**skills** | [**List[Skills]**](Skills.md) | A list of pairs of skill type and descriptive skill level | [optional] 
**mission_importance** | [**MissionImportanceEnum**](MissionImportanceEnum.md) |  | [optional] [default to MissionImportanceEnum.NORMAL]
**age** | **int** | the age of the character, omit if unknown | [optional] 
**sex** | [**DemographicSexEnum**](DemographicSexEnum.md) |  | 
**race** | [**RaceEnum**](RaceEnum.md) |  | 
**role** | [**CharacterRoleEnum**](CharacterRoleEnum.md) |  | [optional] 

## Example

```python
from swagger_client.models.demographics import Demographics

# TODO update the JSON string below
json = "{}"
# create an instance of Demographics from a JSON string
demographics_instance = Demographics.from_json(json)
# print the JSON string representation of the object
print(Demographics.to_json())

# convert the object into a dict
demographics_dict = demographics_instance.to_dict()
# create an instance of Demographics from a dict
demographics_from_dict = Demographics.from_dict(demographics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


