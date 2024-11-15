# coding: utf-8

"""
    ITM TA3 API

    This is the specification of the TA3 API for In The Moment (ITM).  Currently, the Evaluation API for TA2 supports functionality for the Phase 1 Evaluation.  The API is based on the OpenAPI 3.0.3 specification.  # noqa: E501

    OpenAPI spec version: 0.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.itm_ta2_eval_api import ItmTa2EvalApi  # noqa: E501
from swagger_client.rest import ApiException


class TestItmTa2EvalApi(unittest.TestCase):
    """ItmTa2EvalApi unit test stubs"""

    def setUp(self):
        self.api = ItmTa2EvalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_alignment_target(self):
        """Test case for get_alignment_target

        Retrieve alignment target for the scenario  # noqa: E501
        """
        pass

    def test_get_available_actions(self):
        """Test case for get_available_actions

        Get a list of currently available ADM actions  # noqa: E501
        """
        pass

    def test_get_scenario_state(self):
        """Test case for get_scenario_state

        Retrieve scenario state  # noqa: E501
        """
        pass

    def test_get_session_alignment(self):
        """Test case for get_session_alignment

        Retrieve session alignment from TA1  # noqa: E501
        """
        pass

    def test_intend_action(self):
        """Test case for intend_action

        Express intent to take an action within a scenario  # noqa: E501
        """
        pass

    def test_start_scenario(self):
        """Test case for start_scenario

        Get the next scenario  # noqa: E501
        """
        pass

    def test_start_session(self):
        """Test case for start_session

        Start a new session  # noqa: E501
        """
        pass

    def test_take_action(self):
        """Test case for take_action

        Take an action within a scenario  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
