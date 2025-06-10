# AlignmentSource

Describes which session/probe responses were used to compute an alignment score, allowing for lots of flexibility.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scenario_id** | **str** | Unique ID for user session. | 
**probes** | **List[str]** | List of ID&#39;s of probes used to compute alignment. | 

## Example

```python
from swagger_client.models.alignment_source import AlignmentSource

# TODO update the JSON string below
json = "{}"
# create an instance of AlignmentSource from a JSON string
alignment_source_instance = AlignmentSource.from_json(json)
# print the JSON string representation of the object
print(AlignmentSource.to_json())

# convert the object into a dict
alignment_source_dict = alignment_source_instance.to_dict()
# create an instance of AlignmentSource from a dict
alignment_source_from_dict = AlignmentSource.from_dict(alignment_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


