# Character

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | string, globally unique character identifier | 
**unstructured** | **str** | natural language text description of the character | 
**name** | **str** | the name of the character, omit if unknown | [optional] 
**relationship** | [**CharacterRelationship**](CharacterRelationship.md) |  | [optional] 
**demographics** | [**Demographics**](Demographics.md) |  | [optional] 
**injuries** | [**list[Injury]**](Injury.md) | an array of character injuries | [optional] 
**vitals** | [**Vitals**](Vitals.md) |  | [optional] 
**visited** | **bool** | whether or not this character has been visited in the current scenario | [optional] [default to False]
**tag** | [**CharacterTag**](CharacterTag.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

