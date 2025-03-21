# Supplies

a single type of medical supply available to the medic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**SupplyTypeEnum**](SupplyTypeEnum.md) |  | 
**reusable** | **bool** | Whether or not item is consumable/reusable | [optional] [default to False]
**quantity** | **int** | Number of items available in the medical bag | 

## Example

```python
from swagger_client.models.supplies import Supplies

# TODO update the JSON string below
json = "{}"
# create an instance of Supplies from a JSON string
supplies_instance = Supplies.from_json(json)
# print the JSON string representation of the object
print(Supplies.to_json())

# convert the object into a dict
supplies_dict = supplies_instance.to_dict()
# create an instance of Supplies from a dict
supplies_from_dict = Supplies.from_dict(supplies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


