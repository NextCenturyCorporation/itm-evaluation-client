# AlignmentResults

Computed KDMA profile and alignment score for a set of decisions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alignment_source** | [**List[AlignmentSource]**](AlignmentSource.md) |  | 
**alignment_target_id** | **str** | ID of desired profile to align responses to. | 
**score** | **float** | Measured alignment, negative infinity (completely unaligned) to 0 (completely aligned). | 
**kdma_values** | [**List[KDMAValue]**](KDMAValue.md) | Computed KDMA profile from results | [optional] 

## Example

```python
from swagger_client.models.alignment_results import AlignmentResults

# TODO update the JSON string below
json = "{}"
# create an instance of AlignmentResults from a JSON string
alignment_results_instance = AlignmentResults.from_json(json)
# print the JSON string representation of the object
print(AlignmentResults.to_json())

# convert the object into a dict
alignment_results_dict = alignment_results_instance.to_dict()
# create an instance of AlignmentResults from a dict
alignment_results_from_dict = AlignmentResults.from_dict(alignment_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


