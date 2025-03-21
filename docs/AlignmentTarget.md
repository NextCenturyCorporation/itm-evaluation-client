# AlignmentTarget

list of KDMAs to align to

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | globally unique alignment target id | 
**kdma_values** | [**List[KDMAValue]**](KDMAValue.md) | list of KDMAs to align to | 

## Example

```python
from swagger_client.models.alignment_target import AlignmentTarget

# TODO update the JSON string below
json = "{}"
# create an instance of AlignmentTarget from a JSON string
alignment_target_instance = AlignmentTarget.from_json(json)
# print the JSON string representation of the object
print(AlignmentTarget.to_json())

# convert the object into a dict
alignment_target_dict = alignment_target_instance.to_dict()
# create an instance of AlignmentTarget from a dict
alignment_target_from_dict = AlignmentTarget.from_dict(alignment_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


