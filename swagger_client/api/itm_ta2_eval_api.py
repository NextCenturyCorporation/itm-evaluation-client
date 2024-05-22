# coding: utf-8

"""
    ITM TA3 API

    This is the specification of the TA3 API for In The Moment (ITM).  Currently, the Evaluation API for TA2 supports functionality for the September milestone.  The API is based on the OpenAPI 3.0 specification.  # noqa: E501

    OpenAPI spec version: 0.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ItmTa2EvalApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_alignment_target(self, session_id, scenario_id, **kwargs):  # noqa: E501
        """Retrieve alignment target for the scenario  # noqa: E501

        Retrieve alignment target for the scenario with the specified id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alignment_target(session_id, scenario_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: a unique session_id, as returned by /ta2/startSession (required)
        :param str scenario_id: The ID of the scenario for which to retrieve alignment target (required)
        :return: AlignmentTarget
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_alignment_target_with_http_info(session_id, scenario_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_alignment_target_with_http_info(session_id, scenario_id, **kwargs)  # noqa: E501
            return data

    def get_alignment_target_with_http_info(self, session_id, scenario_id, **kwargs):  # noqa: E501
        """Retrieve alignment target for the scenario  # noqa: E501

        Retrieve alignment target for the scenario with the specified id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alignment_target_with_http_info(session_id, scenario_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: a unique session_id, as returned by /ta2/startSession (required)
        :param str scenario_id: The ID of the scenario for which to retrieve alignment target (required)
        :return: AlignmentTarget
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session_id', 'scenario_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_alignment_target" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'session_id' is set
        if ('session_id' not in params or
                params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `get_alignment_target`")  # noqa: E501
        # verify the required parameter 'scenario_id' is set
        if ('scenario_id' not in params or
                params['scenario_id'] is None):
            raise ValueError("Missing the required parameter `scenario_id` when calling `get_alignment_target`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'session_id' in params:
            query_params.append(('session_id', params['session_id']))  # noqa: E501
        if 'scenario_id' in params:
            query_params.append(('scenario_id', params['scenario_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ta2/getAlignmentTarget', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AlignmentTarget',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_available_actions(self, session_id, scenario_id, **kwargs):  # noqa: E501
        """Get a list of currently available ADM actions  # noqa: E501

        Retrieve a list of currently available actions in the scenario with the specified id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_available_actions(session_id, scenario_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: a unique session_id, as returned by /ta2/startSession (required)
        :param str scenario_id: The ID of the scenario for which to retrieve available actions (required)
        :return: list[Action]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_available_actions_with_http_info(session_id, scenario_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_available_actions_with_http_info(session_id, scenario_id, **kwargs)  # noqa: E501
            return data

    def get_available_actions_with_http_info(self, session_id, scenario_id, **kwargs):  # noqa: E501
        """Get a list of currently available ADM actions  # noqa: E501

        Retrieve a list of currently available actions in the scenario with the specified id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_available_actions_with_http_info(session_id, scenario_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: a unique session_id, as returned by /ta2/startSession (required)
        :param str scenario_id: The ID of the scenario for which to retrieve available actions (required)
        :return: list[Action]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session_id', 'scenario_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_available_actions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'session_id' is set
        if ('session_id' not in params or
                params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `get_available_actions`")  # noqa: E501
        # verify the required parameter 'scenario_id' is set
        if ('scenario_id' not in params or
                params['scenario_id'] is None):
            raise ValueError("Missing the required parameter `scenario_id` when calling `get_available_actions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scenario_id' in params:
            path_params['scenario_id'] = params['scenario_id']  # noqa: E501

        query_params = []
        if 'session_id' in params:
            query_params.append(('session_id', params['session_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ta2/{scenario_id}/getAvailableActions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Action]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_scenario_state(self, session_id, scenario_id, **kwargs):  # noqa: E501
        """Retrieve scenario state  # noqa: E501

        Retrieve state of the scenario with the specified id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scenario_state(session_id, scenario_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: a unique session_id, as returned by /ta2/startSession (required)
        :param str scenario_id: the ID of the scenario for which to retrieve status (required)
        :return: State
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_scenario_state_with_http_info(session_id, scenario_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_scenario_state_with_http_info(session_id, scenario_id, **kwargs)  # noqa: E501
            return data

    def get_scenario_state_with_http_info(self, session_id, scenario_id, **kwargs):  # noqa: E501
        """Retrieve scenario state  # noqa: E501

        Retrieve state of the scenario with the specified id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scenario_state_with_http_info(session_id, scenario_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: a unique session_id, as returned by /ta2/startSession (required)
        :param str scenario_id: the ID of the scenario for which to retrieve status (required)
        :return: State
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session_id', 'scenario_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_scenario_state" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'session_id' is set
        if ('session_id' not in params or
                params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `get_scenario_state`")  # noqa: E501
        # verify the required parameter 'scenario_id' is set
        if ('scenario_id' not in params or
                params['scenario_id'] is None):
            raise ValueError("Missing the required parameter `scenario_id` when calling `get_scenario_state`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scenario_id' in params:
            path_params['scenario_id'] = params['scenario_id']  # noqa: E501

        query_params = []
        if 'session_id' in params:
            query_params.append(('session_id', params['session_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ta2/{scenario_id}/getState', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='State',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_session_alignment(self, session_id, target_id, **kwargs):  # noqa: E501
        """Retrieve session alignment from TA1  # noqa: E501

        Retrieve the current session alignment for the session with the specified id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_session_alignment(session_id, target_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: a unique session_id, as returned by /ta2/startSession (required)
        :param str target_id: alignment target id (required)
        :return: AlignmentResults
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_session_alignment_with_http_info(session_id, target_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_session_alignment_with_http_info(session_id, target_id, **kwargs)  # noqa: E501
            return data

    def get_session_alignment_with_http_info(self, session_id, target_id, **kwargs):  # noqa: E501
        """Retrieve session alignment from TA1  # noqa: E501

        Retrieve the current session alignment for the session with the specified id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_session_alignment_with_http_info(session_id, target_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: a unique session_id, as returned by /ta2/startSession (required)
        :param str target_id: alignment target id (required)
        :return: AlignmentResults
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session_id', 'target_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_session_alignment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'session_id' is set
        if ('session_id' not in params or
                params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `get_session_alignment`")  # noqa: E501
        # verify the required parameter 'target_id' is set
        if ('target_id' not in params or
                params['target_id'] is None):
            raise ValueError("Missing the required parameter `target_id` when calling `get_session_alignment`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'session_id' in params:
            query_params.append(('session_id', params['session_id']))  # noqa: E501
        if 'target_id' in params:
            query_params.append(('target_id', params['target_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ta2/getSessionAlignment', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AlignmentResults',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def intend_action(self, session_id, **kwargs):  # noqa: E501
        """Express intent to take an action within a scenario  # noqa: E501

        Express intent to take the specified Action within a scenario  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.intend_action(session_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: a unique session_id, as returned by /ta2/startSession (required)
        :param Action body: Encapsulation of the intended action by a DM in the context of the scenario
        :return: State
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.intend_action_with_http_info(session_id, **kwargs)  # noqa: E501
        else:
            (data) = self.intend_action_with_http_info(session_id, **kwargs)  # noqa: E501
            return data

    def intend_action_with_http_info(self, session_id, **kwargs):  # noqa: E501
        """Express intent to take an action within a scenario  # noqa: E501

        Express intent to take the specified Action within a scenario  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.intend_action_with_http_info(session_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: a unique session_id, as returned by /ta2/startSession (required)
        :param Action body: Encapsulation of the intended action by a DM in the context of the scenario
        :return: State
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method intend_action" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'session_id' is set
        if ('session_id' not in params or
                params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `intend_action`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'session_id' in params:
            query_params.append(('session_id', params['session_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ta2/intendAction', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='State',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def start_scenario(self, session_id, **kwargs):  # noqa: E501
        """Get the next scenario  # noqa: E501

        Get the next scenario in a session with the specified ADM name, returning a Scenario object and unique id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.start_scenario(session_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: a unique session_id, as returned by /ta2/startSession (required)
        :param str scenario_id: the scenario id to run; incompatible with /ta2/startSession's max_scenarios parameter
        :return: Scenario
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.start_scenario_with_http_info(session_id, **kwargs)  # noqa: E501
        else:
            (data) = self.start_scenario_with_http_info(session_id, **kwargs)  # noqa: E501
            return data

    def start_scenario_with_http_info(self, session_id, **kwargs):  # noqa: E501
        """Get the next scenario  # noqa: E501

        Get the next scenario in a session with the specified ADM name, returning a Scenario object and unique id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.start_scenario_with_http_info(session_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: a unique session_id, as returned by /ta2/startSession (required)
        :param str scenario_id: the scenario id to run; incompatible with /ta2/startSession's max_scenarios parameter
        :return: Scenario
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session_id', 'scenario_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method start_scenario" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'session_id' is set
        if ('session_id' not in params or
                params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `start_scenario`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'session_id' in params:
            query_params.append(('session_id', params['session_id']))  # noqa: E501
        if 'scenario_id' in params:
            query_params.append(('scenario_id', params['scenario_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ta2/scenario', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Scenario',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def start_session(self, adm_name, session_type, **kwargs):  # noqa: E501
        """Start a new session  # noqa: E501

        Get unique session id for grouping answers from a collection of scenarios together  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.start_session(adm_name, session_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str adm_name: A self-assigned ADM name. (required)
        :param str session_type: the type of session to start (`eval` or a TA1 name) (required)
        :param str adm_profile: a profile of the ADM in terms of its alignment strategy
        :param bool kdma_training: whether or not this is a training session with TA2
        :param int max_scenarios: the maximum number of scenarios requested, not supported in `eval` sessions
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.start_session_with_http_info(adm_name, session_type, **kwargs)  # noqa: E501
        else:
            (data) = self.start_session_with_http_info(adm_name, session_type, **kwargs)  # noqa: E501
            return data

    def start_session_with_http_info(self, adm_name, session_type, **kwargs):  # noqa: E501
        """Start a new session  # noqa: E501

        Get unique session id for grouping answers from a collection of scenarios together  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.start_session_with_http_info(adm_name, session_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str adm_name: A self-assigned ADM name. (required)
        :param str session_type: the type of session to start (`eval` or a TA1 name) (required)
        :param str adm_profile: a profile of the ADM in terms of its alignment strategy
        :param bool kdma_training: whether or not this is a training session with TA2
        :param int max_scenarios: the maximum number of scenarios requested, not supported in `eval` sessions
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['adm_name', 'session_type', 'adm_profile', 'kdma_training', 'max_scenarios']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method start_session" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'adm_name' is set
        if ('adm_name' not in params or
                params['adm_name'] is None):
            raise ValueError("Missing the required parameter `adm_name` when calling `start_session`")  # noqa: E501
        # verify the required parameter 'session_type' is set
        if ('session_type' not in params or
                params['session_type'] is None):
            raise ValueError("Missing the required parameter `session_type` when calling `start_session`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'adm_name' in params:
            query_params.append(('adm_name', params['adm_name']))  # noqa: E501
        if 'adm_profile' in params:
            query_params.append(('adm_profile', params['adm_profile']))  # noqa: E501
        if 'session_type' in params:
            query_params.append(('session_type', params['session_type']))  # noqa: E501
        if 'kdma_training' in params:
            query_params.append(('kdma_training', params['kdma_training']))  # noqa: E501
        if 'max_scenarios' in params:
            query_params.append(('max_scenarios', params['max_scenarios']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ta2/startSession', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def take_action(self, session_id, **kwargs):  # noqa: E501
        """Take an action within a scenario  # noqa: E501

        Take the specified Action within a scenario  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.take_action(session_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: a unique session_id, as returned by /ta2/startSession (required)
        :param Action body: Encapsulation of an action taken by a DM in the context of the scenario
        :return: State
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.take_action_with_http_info(session_id, **kwargs)  # noqa: E501
        else:
            (data) = self.take_action_with_http_info(session_id, **kwargs)  # noqa: E501
            return data

    def take_action_with_http_info(self, session_id, **kwargs):  # noqa: E501
        """Take an action within a scenario  # noqa: E501

        Take the specified Action within a scenario  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.take_action_with_http_info(session_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str session_id: a unique session_id, as returned by /ta2/startSession (required)
        :param Action body: Encapsulation of an action taken by a DM in the context of the scenario
        :return: State
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method take_action" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'session_id' is set
        if ('session_id' not in params or
                params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `take_action`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'session_id' in params:
            query_params.append(('session_id', params['session_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ta2/takeAction', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='State',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
