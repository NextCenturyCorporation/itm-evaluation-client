# Aid

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An identifier for the aid opportunity, unique within the scene | 
**delay** | **float** | Time until aid is available, in minutes; 0 means ready now | 
**type** | [**AidTypeEnum**](AidTypeEnum.md) |  | [optional] 
**role** | **int** | The characterization of health support for the distribution of medical resources and capabilities; Role 1 has higher capability than Role 4. See [health.mil](https://health.mil/Reference-Center/Glossary-Terms/2018/06/22/Roles-of-Medical-Care)  | [optional] 
**patients_treated** | [**list[MilitaryDispositionEnum]**](MilitaryDispositionEnum.md) | A list of types of patients that can be helped; if omitted, then no restrictions or restrictions are irrelevant | [optional] 
**max_transport** | **int** | Maximum number of casualties that can be accommodated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

