# KDMAValueParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** |  | [optional] 
**value** | **float** |  | 

## Example

```python
from swagger_client.owtriage.models.kdma_value_parameters import KDMAValueParameters

# TODO update the JSON string below
json = "{}"
# create an instance of KDMAValueParameters from a JSON string
kdma_value_parameters_instance = KDMAValueParameters.from_json(json)
# print the JSON string representation of the object
print(KDMAValueParameters.to_json())

# convert the object into a dict
kdma_value_parameters_dict = kdma_value_parameters_instance.to_dict()
# create an instance of KDMAValueParameters from a dict
kdma_value_parameters_from_dict = KDMAValueParameters.from_dict(kdma_value_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


