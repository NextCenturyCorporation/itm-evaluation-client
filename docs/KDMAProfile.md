# KDMAProfile

KDMA Profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computed_kdma_profile** | [**List[KDMAValue]**](KDMAValue.md) |  | 

## Example

```python
from swagger_client.models.kdma_profile import KDMAProfile

# TODO update the JSON string below
json = "{}"
# create an instance of KDMAProfile from a JSON string
kdma_profile_instance = KDMAProfile.from_json(json)
# print the JSON string representation of the object
print(KDMAProfile.to_json())

# convert the object into a dict
kdma_profile_dict = kdma_profile_instance.to_dict()
# create an instance of KDMAProfile from a dict
kdma_profile_from_dict = KDMAProfile.from_dict(kdma_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


