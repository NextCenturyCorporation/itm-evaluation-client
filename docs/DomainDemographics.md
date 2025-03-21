# DomainDemographics

Basic domain-specific properties about the character

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**military_disposition** | [**MilitaryDispositionEnum**](MilitaryDispositionEnum.md) |  | [optional] 
**military_branch** | [**MilitaryBranchEnum**](MilitaryBranchEnum.md) |  | [optional] 
**rank** | [**MilitaryRankEnum**](MilitaryRankEnum.md) |  | [optional] 
**rank_title** | [**MilitaryRankTitleEnum**](MilitaryRankTitleEnum.md) |  | [optional] 
**skills** | [**List[Skills]**](Skills.md) | A list of pairs of skill type and descriptive skill level | [optional] 
**mission_importance** | [**MissionImportanceEnum**](MissionImportanceEnum.md) |  | [optional] [default to MissionImportanceEnum.NORMAL]

## Example

```python
from swagger_client.models.domain_demographics import DomainDemographics

# TODO update the JSON string below
json = "{}"
# create an instance of DomainDemographics from a JSON string
domain_demographics_instance = DomainDemographics.from_json(json)
# print the JSON string representation of the object
print(DomainDemographics.to_json())

# convert the object into a dict
domain_demographics_dict = domain_demographics_instance.to_dict()
# create an instance of DomainDemographics from a dict
domain_demographics_from_dict = DomainDemographics.from_dict(domain_demographics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


