# Environment

Environmental parameters that impact either decision-making, the simulation environment, or both

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sim_environment** | [**SimEnvironment**](SimEnvironment.md) |  | 
**decision_environment** | [**DecisionEnvironment**](DecisionEnvironment.md) |  | [optional] 

## Example

```python
from swagger_client.models.environment import Environment

# TODO update the JSON string below
json = "{}"
# create an instance of Environment from a JSON string
environment_instance = Environment.from_json(json)
# print the JSON string representation of the object
print(Environment.to_json())

# convert the object into a dict
environment_dict = environment_instance.to_dict()
# create an instance of Environment from a dict
environment_from_dict = Environment.from_dict(environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


