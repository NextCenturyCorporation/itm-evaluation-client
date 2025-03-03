# KDEData

KDE Objects representing a KDMA Measurement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kde** | **str** | sklearn.neighbors.KernelDensity serialized to base64 string | 
**label** | **str** | Label for this KDE | 

## Example

```python
from swagger_client.models.kde_data import KDEData

# TODO update the JSON string below
json = "{}"
# create an instance of KDEData from a JSON string
kde_data_instance = KDEData.from_json(json)
# print the JSON string representation of the object
print(KDEData.to_json())

# convert the object into a dict
kde_data_dict = kde_data_instance.to_dict()
# create an instance of KDEData from a dict
kde_data_from_dict = KDEData.from_dict(kde_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


