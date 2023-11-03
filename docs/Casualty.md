# Casualty

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | string, globally unique casualty identifier | 
**unstructured** | **str** | natural language text description of the casualty | 
**name** | **str** | the name of the casualty, omit if unknown | [optional] 
**relationship** | [**CasualtyRelationship**](CasualtyRelationship.md) |  | [optional] 
**demographics** | [**Demographics**](Demographics.md) |  | [optional] 
**injuries** | [**list[Injury]**](Injury.md) | an array of casualty injuries | [optional] 
**vitals** | [**Vitals**](Vitals.md) |  | [optional] 
**visited** | **bool** | whether or not this casualty has been visited in the current scenario | [optional] [default to False]
**tag** | [**CasualtyTag**](CasualtyTag.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

