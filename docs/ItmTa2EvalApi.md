# swagger_client.ItmTa2EvalApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_decompression_needle**](ItmTa2EvalApi.md#apply_decompression_needle) | **POST** /ta2/casualty/{casualty_id}/applyDecompressionNeedle | Apply a decompression needle to a casualty
[**apply_hemostatic_gauze**](ItmTa2EvalApi.md#apply_hemostatic_gauze) | **POST** /ta2/casualty/{casualty_id}/applyHemostaticGauze | Apply hemostatic gauze to a casualty
[**apply_nasal_trumpet**](ItmTa2EvalApi.md#apply_nasal_trumpet) | **POST** /ta2/casualty/{casualty_id}/applyNasalTrumpet | Apply a nasal trumpet to a casualty
[**apply_pressure_bandage**](ItmTa2EvalApi.md#apply_pressure_bandage) | **POST** /ta2/casualty/{casualty_id}/applyPressureBandage | Apply a pressure bandage to a casualty
[**apply_tourniquet**](ItmTa2EvalApi.md#apply_tourniquet) | **POST** /ta2/casualty/{casualty_id}/applyTourniquet | Apply a tourniquet to a casualty
[**apply_treatment**](ItmTa2EvalApi.md#apply_treatment) | **POST** /ta2/casualty/{casualty_id}/applyTreatment | Apply a treatment to a casualty
[**check_vital**](ItmTa2EvalApi.md#check_vital) | **GET** /ta2/casualty/{casualty_id}/checkVital | Assess and retrieve a vital sign
[**check_vitals**](ItmTa2EvalApi.md#check_vitals) | **GET** /ta2/casualty/{casualty_id}/checkVitals | Assess and retrieve all casualty vital signs
[**direct_to_safezone**](ItmTa2EvalApi.md#direct_to_safezone) | **POST** /ta2/{scenario_id}/directToSafezone | Direct casualties to the safe zone
[**get_alignment_target**](ItmTa2EvalApi.md#get_alignment_target) | **GET** /ta2/getAlignmentTarget | Retrieve alignment target for the scenario
[**get_available_actions**](ItmTa2EvalApi.md#get_available_actions) | **GET** /ta2/{scenario_id}/getAvailableActions | Get a list of currently available ADM actions
[**get_available_actions2**](ItmTa2EvalApi.md#get_available_actions2) | **GET** /ta2/{scenario_id}/getAvailableActionTypes | Get a list of currently available ADM action types
[**get_consciousness**](ItmTa2EvalApi.md#get_consciousness) | **GET** /ta2/casualty/{casualty_id}/checkConsciousness | Check casualty consciousness
[**get_heart_rate**](ItmTa2EvalApi.md#get_heart_rate) | **GET** /ta2/casualty/{casualty_id}/checkHeartRate | Check casualty heart rate
[**get_respiratory_rate**](ItmTa2EvalApi.md#get_respiratory_rate) | **GET** /ta2/casualty/{casualty_id}/checkRespiratoryRate | Check casualty respiratory rate
[**get_scenario_state**](ItmTa2EvalApi.md#get_scenario_state) | **GET** /ta2/{scenario_id}/getState | Retrieve scenario state
[**start_scenario**](ItmTa2EvalApi.md#start_scenario) | **GET** /ta2/scenario | Get the next scenario
[**start_session**](ItmTa2EvalApi.md#start_session) | **GET** /ta2/startSession | Start a new session
[**tag_casualty**](ItmTa2EvalApi.md#tag_casualty) | **POST** /ta2/casualty/{casualty_id}/tag | Tag a casualty with a triage category
[**take_action**](ItmTa2EvalApi.md#take_action) | **POST** /ta2/takeAction | Take an action within a scenario

# **apply_decompression_needle**
> State apply_decompression_needle(session_id, casualty_id, location)

Apply a decompression needle to a casualty

Treat the specified casualty with a decompression needle in the specified location

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
casualty_id = 'casualty_id_example' # str | The ID of the casualty to treat
location = 'location_example' # str | the injury location on the casualty's body (see Injury `location`)

try:
    # Apply a decompression needle to a casualty
    api_response = api_instance.apply_decompression_needle(session_id, casualty_id, location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->apply_decompression_needle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **casualty_id** | **str**| The ID of the casualty to treat | 
 **location** | **str**| the injury location on the casualty&#x27;s body (see Injury &#x60;location&#x60;) | 

### Return type

[**State**](State.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_hemostatic_gauze**
> State apply_hemostatic_gauze(session_id, casualty_id, location)

Apply hemostatic gauze to a casualty

Treat the specified casualty with hemostatic gauze in the specified location

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
casualty_id = 'casualty_id_example' # str | The ID of the casualty to treat
location = 'location_example' # str | the injury location on the casualty's body (see Injury `location`)

try:
    # Apply hemostatic gauze to a casualty
    api_response = api_instance.apply_hemostatic_gauze(session_id, casualty_id, location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->apply_hemostatic_gauze: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **casualty_id** | **str**| The ID of the casualty to treat | 
 **location** | **str**| the injury location on the casualty&#x27;s body (see Injury &#x60;location&#x60;) | 

### Return type

[**State**](State.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_nasal_trumpet**
> State apply_nasal_trumpet(session_id, casualty_id)

Apply a nasal trumpet to a casualty

Treat the specified casualty with a nasal trumpet in the specified location

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
casualty_id = 'casualty_id_example' # str | The ID of the casualty to treat

try:
    # Apply a nasal trumpet to a casualty
    api_response = api_instance.apply_nasal_trumpet(session_id, casualty_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->apply_nasal_trumpet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **casualty_id** | **str**| The ID of the casualty to treat | 

### Return type

[**State**](State.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_pressure_bandage**
> State apply_pressure_bandage(session_id, casualty_id, location)

Apply a pressure bandage to a casualty

Treat the specified casualty with a pressure bandage in the specified location

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
casualty_id = 'casualty_id_example' # str | The ID of the casualty to treat
location = 'location_example' # str | the injury location on the casualty's body (see Injury `location`)

try:
    # Apply a pressure bandage to a casualty
    api_response = api_instance.apply_pressure_bandage(session_id, casualty_id, location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->apply_pressure_bandage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **casualty_id** | **str**| The ID of the casualty to treat | 
 **location** | **str**| the injury location on the casualty&#x27;s body (see Injury &#x60;location&#x60;) | 

### Return type

[**State**](State.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_tourniquet**
> State apply_tourniquet(session_id, casualty_id, location)

Apply a tourniquet to a casualty

Treat the specified casualty with a tourniquet in the specified location

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
casualty_id = 'casualty_id_example' # str | The ID of the casualty to treat
location = 'location_example' # str | the injury location on the casualty's body (see Injury `location`)

try:
    # Apply a tourniquet to a casualty
    api_response = api_instance.apply_tourniquet(session_id, casualty_id, location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->apply_tourniquet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **casualty_id** | **str**| The ID of the casualty to treat | 
 **location** | **str**| the injury location on the casualty&#x27;s body (see Injury &#x60;location&#x60;) | 

### Return type

[**State**](State.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_treatment**
> State apply_treatment(session_id, casualty_id, tool, location=location)

Apply a treatment to a casualty

Treat the specified casualty with the specified tool in the specified location

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
casualty_id = 'casualty_id_example' # str | The ID of the casualty to tag
tool = 'tool_example' # str | The tool to use to apply treatment (see Supplies)
location = 'location_example' # str | the injury location on the casualty's body (see Injury `location`) (optional)

try:
    # Apply a treatment to a casualty
    api_response = api_instance.apply_treatment(session_id, casualty_id, tool, location=location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->apply_treatment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **casualty_id** | **str**| The ID of the casualty to tag | 
 **tool** | **str**| The tool to use to apply treatment (see Supplies) | 
 **location** | **str**| the injury location on the casualty&#x27;s body (see Injury &#x60;location&#x60;) | [optional] 

### Return type

[**State**](State.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_vital**
> Vitals check_vital(session_id, casualty_id, vital_sign)

Assess and retrieve a vital sign

Retrieve the specified vital sign of the specified casualty.

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
casualty_id = 'casualty_id_example' # str | The ID of the casualty to query
vital_sign = 'vital_sign_example' # str | The vital sign to retrieve, taken from controlled vocabulary

try:
    # Assess and retrieve a vital sign
    api_response = api_instance.check_vital(session_id, casualty_id, vital_sign)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->check_vital: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **casualty_id** | **str**| The ID of the casualty to query | 
 **vital_sign** | **str**| The vital sign to retrieve, taken from controlled vocabulary | 

### Return type

[**Vitals**](Vitals.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_vitals**
> Vitals check_vitals(session_id, casualty_id)

Assess and retrieve all casualty vital signs

Retrieve all vital signs of the specified casualty.

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
casualty_id = 'casualty_id_example' # str | The ID of the casualty to query

try:
    # Assess and retrieve all casualty vital signs
    api_response = api_instance.check_vitals(session_id, casualty_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->check_vitals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **casualty_id** | **str**| The ID of the casualty to query | 

### Return type

[**Vitals**](Vitals.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **direct_to_safezone**
> State direct_to_safezone(session_id, scenario_id)

Direct casualties to the safe zone

Verbally direct all mobile casualties to the safe zone

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
scenario_id = 'scenario_id_example' # str | The ID of the scenario to direct mobile casualties

try:
    # Direct casualties to the safe zone
    api_response = api_instance.direct_to_safezone(session_id, scenario_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->direct_to_safezone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **scenario_id** | **str**| The ID of the scenario to direct mobile casualties | 

### Return type

[**State**](State.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
scenario_id = 'scenario_id_example' # str | The ID of the scenario for which to retrieve avaialble actions

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
 **scenario_id** | **str**| The ID of the scenario for which to retrieve avaialble actions | 

### Return type

[**list[Action]**](Action.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_actions2**
> list[str] get_available_actions2(session_id, scenario_id)

Get a list of currently available ADM action types

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
scenario_id = 'scenario_id_example' # str | The ID of the scenario for which to retrieve avaialble actions

try:
    # Get a list of currently available ADM action types
    api_response = api_instance.get_available_actions2(session_id, scenario_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->get_available_actions2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **scenario_id** | **str**| The ID of the scenario for which to retrieve avaialble actions | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consciousness**
> bool get_consciousness(session_id, casualty_id)

Check casualty consciousness

Check the consciousness of the specified casualty

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
casualty_id = 'casualty_id_example' # str | The ID of the casualty to for which to check consciousness

try:
    # Check casualty consciousness
    api_response = api_instance.get_consciousness(session_id, casualty_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->get_consciousness: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **casualty_id** | **str**| The ID of the casualty to for which to check consciousness | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heart_rate**
> int get_heart_rate(session_id, casualty_id)

Check casualty heart rate

Check the heart rate of the specified casualty.

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
casualty_id = 'casualty_id_example' # str | The ID of the casualty to for which to request heart rate

try:
    # Check casualty heart rate
    api_response = api_instance.get_heart_rate(session_id, casualty_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->get_heart_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **casualty_id** | **str**| The ID of the casualty to for which to request heart rate | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_respiratory_rate**
> int get_respiratory_rate(session_id, casualty_id)

Check casualty respiratory rate

Check the respiratory rate of the specified casualty.

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
casualty_id = 'casualty_id_example' # str | The ID of the casualty to for which to request respiratory rate

try:
    # Check casualty respiratory rate
    api_response = api_instance.get_respiratory_rate(session_id, casualty_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->get_respiratory_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **casualty_id** | **str**| The ID of the casualty to for which to request respiratory rate | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

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
scenario_id = 'scenario_id_example' # str | The ID of the scenario for which to retrieve status

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
 **scenario_id** | **str**| The ID of the scenario for which to retrieve status | 

### Return type

[**State**](State.md)

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
scenario_id = 'scenario_id_example' # str | a scenario id to start, used internally by TA3 (optional)

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
 **scenario_id** | **str**| a scenario id to start, used internally by TA3 | [optional] 

### Return type

[**Scenario**](Scenario.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_session**
> str start_session(adm_name, session_type, max_scenarios=max_scenarios)

Start a new session

Get unique session id for grouping answers from a collection of scenarios/probes together

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
session_type = 'session_type_example' # str | the type of session to start (`test`, `eval`, or a TA1 name)
max_scenarios = 56 # int | the maximum number of scenarios requested, supported only in `test` sessions (optional)

try:
    # Start a new session
    api_response = api_instance.start_session(adm_name, session_type, max_scenarios=max_scenarios)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->start_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adm_name** | **str**| A self-assigned ADM name.  Can add authentication later. | 
 **session_type** | **str**| the type of session to start (&#x60;test&#x60;, &#x60;eval&#x60;, or a TA1 name) | 
 **max_scenarios** | **int**| the maximum number of scenarios requested, supported only in &#x60;test&#x60; sessions | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag_casualty**
> State tag_casualty(session_id, casualty_id, tag)

Tag a casualty with a triage category

Apply a triage tag to the specified casualty with the specified tag

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
casualty_id = 'casualty_id_example' # str | The ID of the casualty to tag
tag = 'tag_example' # str | The tag to apply to the casualty, chosen from triage categories

try:
    # Tag a casualty with a triage category
    api_response = api_instance.tag_casualty(session_id, casualty_id, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItmTa2EvalApi->tag_casualty: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| a unique session_id, as returned by /ta2/startSession | 
 **casualty_id** | **str**| The ID of the casualty to tag | 
 **tag** | **str**| The tag to apply to the casualty, chosen from triage categories | 

### Return type

[**State**](State.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **take_action**
> State take_action(session_id, body=body)

Take an action within a scenario

Take an action with

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

