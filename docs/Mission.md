# Mission

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unstructured** | **str** | natural language description of current mission | 
**mission_type** | [**MissionTypeEnum**](MissionTypeEnum.md) |  | 
**character_importance** | **list[dict(str, MissionImportanceEnum)]** | A list of pairs of character ids with an indicator of how mission-critical the character is | [optional] 
**civilian_presence** | [**CivilianPresenceEnum**](CivilianPresenceEnum.md) |  | [optional] 
**communication_capability** | [**CommunicationCapabilityEnum**](CommunicationCapabilityEnum.md) |  | [optional] 
**roe** | **str** | rules of engagement to inform decision-making, but not to restrict decision space | [optional] 
**political_climate** | **str** | The political climate in a mission to inform decision-making | [optional] 
**medical_policies** | **str** | Medical policies in effect in a mission, to inform decision-making | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

