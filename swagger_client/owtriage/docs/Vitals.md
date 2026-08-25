# Vitals

Vital levels and other indications of health

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avpu** | [**AvpuLevelEnum**](AvpuLevelEnum.md) |  | [optional] 
**breathing** | [**BreathingLevelEnum**](BreathingLevelEnum.md) |  | [optional] 
**heart_rate** | [**HeartRateEnum**](HeartRateEnum.md) |  | [optional] 

## Example

```python
from swagger_client.owtriage.models.vitals import Vitals

# TODO update the JSON string below
json = "{}"
# create an instance of Vitals from a JSON string
vitals_instance = Vitals.from_json(json)
# print the JSON string representation of the object
print(Vitals.to_json())

# convert the object into a dict
vitals_dict = vitals_instance.to_dict()
# create an instance of Vitals from a dict
vitals_from_dict = Vitals.from_dict(vitals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


