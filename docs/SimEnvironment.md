# SimEnvironment

Environmental elements that impact simulation configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unstructured** | **str** | Natural language, plain text description of the environment | [optional] 
**type** | [**SimEnvironmentTypeEnum**](SimEnvironmentTypeEnum.md) |  | 
**weather** | [**WeatherTypeEnum**](WeatherTypeEnum.md) |  | [optional] 
**terrain** | [**TerrainTypeEnum**](TerrainTypeEnum.md) |  | [optional] 
**flora** | [**FloraTypeEnum**](FloraTypeEnum.md) |  | [optional] 
**fauna** | [**FaunaTypeEnum**](FaunaTypeEnum.md) |  | [optional] 
**temperature** | **float** | numerical temperature in degrees Fahrenheit | [optional] 
**humidity** | **float** | Numerical relative humidity, in percentage | [optional] 
**lighting** | [**LightingTypeEnum**](LightingTypeEnum.md) |  | [optional] 
**visibility** | [**VisibilityTypeEnum**](VisibilityTypeEnum.md) |  | [optional] 
**noise_ambient** | [**AmbientNoiseEnum**](AmbientNoiseEnum.md) |  | [optional] 
**noise_peak** | [**PeakNoiseEnum**](PeakNoiseEnum.md) |  | [optional] 

## Example

```python
from swagger_client.models.sim_environment import SimEnvironment

# TODO update the JSON string below
json = "{}"
# create an instance of SimEnvironment from a JSON string
sim_environment_instance = SimEnvironment.from_json(json)
# print the JSON string representation of the object
print(SimEnvironment.to_json())

# convert the object into a dict
sim_environment_dict = sim_environment_instance.to_dict()
# create an instance of SimEnvironment from a dict
sim_environment_from_dict = SimEnvironment.from_dict(sim_environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


