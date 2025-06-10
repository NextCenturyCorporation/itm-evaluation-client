# MetaInfo

Includes meta info to assist with debugging. Only provided during training sessions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scene_id** | **str** | The scene ID, unique throughout the scenario | [optional] 
**probe_response** | [**ProbeResponse**](ProbeResponse.md) |  | [optional] 

## Example

```python
from swagger_client.models.meta_info import MetaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MetaInfo from a JSON string
meta_info_instance = MetaInfo.from_json(json)
# print the JSON string representation of the object
print(MetaInfo.to_json())

# convert the object into a dict
meta_info_dict = meta_info_instance.to_dict()
# create an instance of MetaInfo from a dict
meta_info_from_dict = MetaInfo.from_dict(meta_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


