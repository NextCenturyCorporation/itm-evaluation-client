# DomainConditions

Domain-specific conditions that specify whether to transition to the next scene or send a probe response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**character_vitals** | [**List[ConditionsCharacterVitals]**](ConditionsCharacterVitals.md) | True if any of the specified collection of vital values have been met for the specified character_id | [optional] 
**supplies** | [**List[Supplies]**](Supplies.md) | True if any of the specified supplies reach or go below the specified quantity | [optional] 

## Example

```python
from swagger_client.models.domain_conditions import DomainConditions

# TODO update the JSON string below
json = "{}"
# create an instance of DomainConditions from a JSON string
domain_conditions_instance = DomainConditions.from_json(json)
# print the JSON string representation of the object
print(DomainConditions.to_json())

# convert the object into a dict
domain_conditions_dict = domain_conditions_instance.to_dict()
# create an instance of DomainConditions from a dict
domain_conditions_from_dict = DomainConditions.from_dict(domain_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


