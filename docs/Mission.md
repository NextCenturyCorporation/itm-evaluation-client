# Mission

Mission parameters that impact decision-making

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unstructured** | **str** | natural language description of current mission | 
**mission_type** | [**MissionTypeEnum**](MissionTypeEnum.md) |  | 
**character_importance** | **List[Dict[str, str]]** | A list of pairs of character ids with an indicator of how mission-critical the character is | [optional] 
**civilian_presence** | [**CivilianPresenceEnum**](CivilianPresenceEnum.md) |  | [optional] 
**communication_capability** | [**CommunicationCapabilityEnum**](CommunicationCapabilityEnum.md) |  | [optional] [default to CommunicationCapabilityEnum.BOTH]
**roe** | **str** | rules of engagement to inform decision-making, but not to restrict decision space | [optional] 
**political_climate** | **str** | The political climate in a mission to inform decision-making | [optional] 
**medical_policies** | [**List[MedicalPoliciesEnum]**](MedicalPoliciesEnum.md) | A list of medical policies; omit this property if no special policy is in place | [optional] 

## Example

```python
from swagger_client.models.mission import Mission

# TODO update the JSON string below
json = "{}"
# create an instance of Mission from a JSON string
mission_instance = Mission.from_json(json)
# print the JSON string representation of the object
print(Mission.to_json())

# convert the object into a dict
mission_dict = mission_instance.to_dict()
# create an instance of Mission from a dict
mission_from_dict = Mission.from_dict(mission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


