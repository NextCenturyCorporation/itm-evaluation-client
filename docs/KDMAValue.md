# KDMAValue

Single KDMA value with value(s), or a kernel density estimate of the KDMA value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kdma** | **str** | Name of KDMA | 
**value** | **float** | Numeric score for a given KDMA | [optional] 
**scores** | **List[float]** | Ordered KDMA scores | [optional] 
**kdes** | [**Dict[str, KDEData]**](KDEData.md) | KDE Objects representing a KDMA Measurement | [optional] 
**parameters** | [**List[KDMAValueParametersInner]**](KDMAValueParametersInner.md) |  | [optional] 

## Example

```python
from swagger_client.models.kdma_value import KDMAValue

# TODO update the JSON string below
json = "{}"
# create an instance of KDMAValue from a JSON string
kdma_value_instance = KDMAValue.from_json(json)
# print the JSON string representation of the object
print(KDMAValue.to_json())

# convert the object into a dict
kdma_value_dict = kdma_value_instance.to_dict()
# create an instance of KDMAValue from a dict
kdma_value_from_dict = KDMAValue.from_dict(kdma_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


