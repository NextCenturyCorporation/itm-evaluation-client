# Scenario

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | a globally unique id for the scenario | 
**name** | **str** | human-readable scenario name, not necessarily unique | 
**first_scene** | **str** | indicates the first/opening scene ID in the scenario | [optional] 
**session_complete** | **bool** | set to true if the session is complete; that is, there are no more scenarios | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**scenes** | [**list[Scene]**](Scene.md) | A list of specification for all scenes in the scenario | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

