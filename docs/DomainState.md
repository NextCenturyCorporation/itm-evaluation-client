# DomainState

the current tactical & environmental state of the scenario and of its characters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mission** | [**Mission**](Mission.md) |  | [optional] 
**environment** | [**Environment**](Environment.md) |  | 
**supplies** | [**List[Supplies]**](Supplies.md) | A list of supplies available to the medic | 

## Example

```python
from swagger_client.models.domain_state import DomainState

# TODO update the JSON string below
json = "{}"
# create an instance of DomainState from a JSON string
domain_state_instance = DomainState.from_json(json)
# print the JSON string representation of the object
print(DomainState.to_json())

# convert the object into a dict
domain_state_dict = domain_state_instance.to_dict()
# create an instance of DomainState from a dict
domain_state_from_dict = DomainState.from_dict(domain_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


