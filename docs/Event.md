# Event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unstructured** | **str** | Natural language, plain text description of the event | 
**type** | [**EventTypeEnum**](EventTypeEnum.md) |  | 
**source** | **str** | The &#x27;subject&#x27; of the event; can be a character &#x60;id&#x60; or an &#x60;EntityTypeEnum&#x60; | [optional] 
**object** | **str** | The &#x27;object&#x27; of the event; can be a character &#x60;id&#x60; or an &#x60;EntityTypeEnum&#x60; | [optional] 
**action_id** | **str** | An action ID from among the available actions | [optional] 
**relevant_state** | **list[str]** | An array of relevant state for the Event | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

