# Character

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unstructured_postassess** | **str** | unstructured description updated after character assessment | [optional] 
**has_blanket** | **bool** | whether or not this character has a blanket (either wrapped around or underneath) | [optional] [default to False]
**intent** | [**IntentEnum**](IntentEnum.md) |  | [optional] 
**directness_of_causality** | [**DirectnessEnum**](DirectnessEnum.md) |  | [optional] 
**injuries** | [**list[Injury]**](Injury.md) | A list of Injuries for the character | [optional] 
**vitals** | [**Vitals**](Vitals.md) |  | [optional] 
**visited** | **bool** | whether or not this character has been visited by the ADM in the current scenario | [optional] [default to False]
**tag** | [**CharacterTagEnum**](CharacterTagEnum.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

