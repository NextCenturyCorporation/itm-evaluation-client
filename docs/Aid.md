# Aid

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An identifier for the aid opportunity, unique within the scene | 
**delay** | **float** | Time until aid is available, in minutes; 0 means ready now | 
**type** | [**AidTypeEnum**](AidTypeEnum.md) |  | [optional] 
**level** | **int** | Refers to the kinds of resources/capabilities available in a trauma center; Level 1 has more resources than Level 5. See [amtrauma.org](https://www.amtrauma.org/page/traumalevels/)  | [optional] 
**patients_treated** | [**list[MilitaryDispositionEnum]**](MilitaryDispositionEnum.md) | A list of types of patients that can be helped; if omitted, then no restrictions or restrictions are irrelevant | [optional] 
**max_transport** | **int** | Maximum number of casualties that can be accommodated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

