# swagger_client.ItmTa2EvalApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_alignment_target**](ItmTa2EvalApi.md#get_alignment_target) | **GET** /ta2/getAlignmentTarget | Retrieve alignment target for the scenario
[**get_available_actions**](ItmTa2EvalApi.md#get_available_actions) | **GET** /ta2/{scenario_id}/getAvailableActions | Get a list of currently available ADM actions
[**get_scenario_state**](ItmTa2EvalApi.md#get_scenario_state) | **GET** /ta2/{scenario_id}/getState | Retrieve scenario state
[**get_session_alignment**](ItmTa2EvalApi.md#get_session_alignment) | **GET** /ta2/getSessionAlignment | Retrieve session alignment from TA1
[**start_scenario**](ItmTa2EvalApi.md#start_scenario) | **GET** /ta2/scenario | Get the next scenario
[**start_session**](ItmTa2EvalApi.md#start_session) | **GET** /ta2/startSession | Start a new session
[**take_action**](ItmTa2EvalApi.md#take_action) | **POST** /ta2/takeAction | Take an action within a scenario

# **get_alignment_target**
> AlignmentTarget get_alignment_target(session_id, scenario_id)

Retrieve alignment target for the scenario

Retrieve alignment target for the scenario with the specified id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmTa2EvalApi()
session_id = 'session_id_example' # str | a unique session_id, as returned by /ta2/startSession
scenario_id = 'scenario_id_example' # str | The ID of the scenario for which to retrieve alignment target

try:
    # Retrieve alignment target for the scenario
    api_response = api_instance.get_alignment_target(session_id, scenario_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->get_alignment_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **scenario_id** | **str**| The ID of the scenario for which to retrieve alignment target | 

### Return type

[**AlignmentTarget**](AlignmentTarget.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_actions**
> list[Action] get_available_actions(session_id, scenario_id)

Get a list of currently available ADM actions

Retrieve a list of currently available actions in the scenario with the specified id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmTa2EvalApi()
session_id = 'session_id_example' # str | a unique session_id, as returned by /ta2/startSession
scenario_id = 'scenario_id_example' # str | The ID of the scenario for which to retrieve available actions

try:
    # Get a list of currently available ADM actions
    api_response = api_instance.get_available_actions(session_id, scenario_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->get_available_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **scenario_id** | **str**| The ID of the scenario for which to retrieve available actions | 

### Return type

[**list[Action]**](Action.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scenario_state**
> State get_scenario_state(session_id, scenario_id)

Retrieve scenario state

Retrieve state of the scenario with the specified id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmTa2EvalApi()
session_id = 'session_id_example' # str | a unique session_id, as returned by /ta2/startSession
scenario_id = 'scenario_id_example' # str | the ID of the scenario for which to retrieve status

try:
    # Retrieve scenario state
    api_response = api_instance.get_scenario_state(session_id, scenario_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->get_scenario_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **scenario_id** | **str**| the ID of the scenario for which to retrieve status | 

### Return type

[**State**](State.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session_alignment**
> AlignmentResults get_session_alignment(session_id, target_id)

Retrieve session alignment from TA1

Retrieve the current session alignment for the session with the specified id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmTa2EvalApi()
session_id = 'session_id_example' # str | a unique session_id, as returned by /ta2/startSession
target_id = 'target_id_example' # str | alignment target id

try:
    # Retrieve session alignment from TA1
    api_response = api_instance.get_session_alignment(session_id, target_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->get_session_alignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **target_id** | **str**| alignment target id | 

### Return type

[**AlignmentResults**](AlignmentResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_scenario**
> Scenario start_scenario(session_id, scenario_id=scenario_id)

Get the next scenario

Get the next scenario in a session with the specified ADM name, returning a Scenario object and unique id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmTa2EvalApi()
session_id = 'session_id_example' # str | a unique session_id, as returned by /ta2/startSession
scenario_id = 'scenario_id_example' # str | the scenario id to run; incompatible with /ta2/startSession's max_scenarios parameter (optional)

try:
    # Get the next scenario
    api_response = api_instance.start_scenario(session_id, scenario_id=scenario_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->start_scenario: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **scenario_id** | **str**| the scenario id to run; incompatible with /ta2/startSession&#x27;s max_scenarios parameter | [optional] 

### Return type

[**Scenario**](Scenario.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_session**
> str start_session(adm_name, session_type, adm_profile=adm_profile, kdma_training=kdma_training, max_scenarios=max_scenarios)

Start a new session

Get unique session id for grouping answers from a collection of scenarios together

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmTa2EvalApi()
adm_name = 'adm_name_example' # str | A self-assigned ADM name.  Can add authentication later.
session_type = 'session_type_example' # str | the type of session to start (`eval` or a TA1 name)
adm_profile = 'adm_profile_example' # str | a profile of the ADM in terms of its alignment strategy (optional)
kdma_training = false # bool | whether or not this is a training session with TA2 (optional) (default to false)
max_scenarios = 56 # int | the maximum number of scenarios requested, not supported in `eval` sessions (optional)

try:
    # Start a new session
    api_response = api_instance.start_session(adm_name, session_type, adm_profile=adm_profile, kdma_training=kdma_training, max_scenarios=max_scenarios)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->start_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adm_name** | **str**| A self-assigned ADM name.  Can add authentication later. | 
 **session_type** | **str**| the type of session to start (&#x60;eval&#x60; or a TA1 name) | 
 **adm_profile** | **str**| a profile of the ADM in terms of its alignment strategy | [optional] 
 **kdma_training** | **bool**| whether or not this is a training session with TA2 | [optional] [default to false]
 **max_scenarios** | **int**| the maximum number of scenarios requested, not supported in &#x60;eval&#x60; sessions | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **take_action**
> State take_action(session_id, body=body)

Take an action within a scenario

Take the specified Action within a scenario

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItmTa2EvalApi()
session_id = 'session_id_example' # str | a unique session_id, as returned by /ta2/startSession
body = swagger_client.Action() # Action | Encapsulation of an action taken by a DM in the context of the scenario (optional)

try:
    # Take an action within a scenario
    api_response = api_instance.take_action(session_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->take_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **body** | [**Action**](Action.md)| Encapsulation of an action taken by a DM in the context of the scenario | [optional] 

### Return type

[**State**](State.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

