# Event

a unit of structured communication from scenario to ADM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unstructured** | **str** | Natural language, plain text description of the event | 
**type** | [**EventTypeEnum**](EventTypeEnum.md) |  | 
**source** | **str** | The &#39;subject&#39; of the event; can be a character &#x60;id&#x60; or an &#x60;EntityTypeEnum&#x60; | [optional] 
**object** | **str** | The &#39;object&#39; of the event; can be a character &#x60;id&#x60; or an &#x60;EntityTypeEnum&#x60; | [optional] 
**when** | **float** | indicates when (in minutes) the event happened (negative value) or is expected to happen (positive value); omit if zero (event happens now) | [optional] 
**action_id** | **str** | An action ID from among the available actions | [optional] 
**relevant_state** | **List[str]** | An array of relevant state for the Event | [optional] 

## Example

```python
from swagger_client.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print(Event.to_json())

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_from_dict = Event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


