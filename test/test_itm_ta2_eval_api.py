# coding: utf-8

"""
    ITM TA3 API

    This is the specification of the TA3 API for In The Moment (ITM).  Currently, the Evaluation API for TA2 supports functionality for the September milestone.  The API is based on the OpenAPI 3.0 specification.  # noqa: E501

    OpenAPI spec version: 0.2.0
    
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

    def test_apply_decompression_needle(self):
        """Test case for apply_decompression_needle

        Apply a decompression needle to a casualty  # noqa: E501
        """
        pass

    def test_apply_hemostatic_gauze(self):
        """Test case for apply_hemostatic_gauze

        Apply hemostatic gauze to a casualty  # noqa: E501
        """
        pass

    def test_apply_nasal_trumpet(self):
        """Test case for apply_nasal_trumpet

        Apply a nasal trumpet to a casualty  # noqa: E501
        """
        pass

    def test_apply_pressure_bandage(self):
        """Test case for apply_pressure_bandage

        Apply a pressure bandage to a casualty  # noqa: E501
        """
        pass

    def test_apply_tourniquet(self):
        """Test case for apply_tourniquet

        Apply a tourniquet to a casualty  # noqa: E501
        """
        pass

    def test_apply_treatment(self):
        """Test case for apply_treatment

        Apply a treatment to a casualty  # noqa: E501
        """
        pass

    def test_check_vital(self):
        """Test case for check_vital

        Assess and retrieve a vital sign  # noqa: E501
        """
        pass

    def test_check_vitals(self):
        """Test case for check_vitals

        Assess and retrieve all casualty vital signs  # noqa: E501
        """
        pass

    def test_direct_to_safezone(self):
        """Test case for direct_to_safezone

        Direct casualties to the safe zone  # noqa: E501
        """
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

    def test_get_available_actions2(self):
        """Test case for get_available_actions2

        Get a list of currently available ADM action types  # noqa: E501
        """
        pass

    def test_get_consciousness(self):
        """Test case for get_consciousness

        Check casualty consciousness  # noqa: E501
        """
        pass

    def test_get_heart_rate(self):
        """Test case for get_heart_rate

        Check casualty heart rate  # noqa: E501
        """
        pass

    def test_get_respiratory_rate(self):
        """Test case for get_respiratory_rate

        Check casualty respiratory rate  # noqa: E501
        """
        pass

    def test_get_scenario_state(self):
        """Test case for get_scenario_state

        Retrieve scenario state  # noqa: E501
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

    def test_tag_casualty(self):
        """Test case for tag_casualty

        Tag a casualty with a triage category  # noqa: E501
        """
        pass

    def test_take_action(self):
        """Test case for take_action

        Take an action within a scenario  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
