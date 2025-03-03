# ProbeConfig

Probe configuration for use by TA1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**probe_id** | **str** | A valid probe_id from the appropriate TA1 | [optional] 
**description** | **str** | A description of the probe for use by TA1 | [optional] 

## Example

```python
from swagger_client.models.probe_config import ProbeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ProbeConfig from a JSON string
probe_config_instance = ProbeConfig.from_json(json)
# print the JSON string representation of the object
print(ProbeConfig.to_json())

# convert the object into a dict
probe_config_dict = probe_config_instance.to_dict()
# create an instance of ProbeConfig from a dict
probe_config_from_dict = ProbeConfig.from_dict(probe_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


