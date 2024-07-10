# Injury

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**InjuryTypeEnum**](InjuryTypeEnum.md) |  | 
**location** | [**InjuryLocationEnum**](InjuryLocationEnum.md) |  | 
**severity** | [**InjurySeverityEnum**](InjurySeverityEnum.md) |  | [optional] 
**status** | [**InjuryStatusEnum**](InjuryStatusEnum.md) |  | 
**source_character** | **str** | The character id of the person responsible for the injury, subject to the character&#x27;s &#x60;directness_of_causality&#x60; | [optional] 
**treatments_required** | **int** | The number of successful treatments required to treat the injury fully, which sets &#x60;status&#x60; to &#x60;treated&#x60; | [optional] 
**treatments_applied** | **int** | The number of successful treatments applied to the injury | [optional] [default to 0]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

