# coding: utf-8

"""
    ITM TA3 API

    This is the specification of the TA3 API for In The Moment (ITM).  Currently, the Evaluation API for TA2 supports functionality for the Phase 1 Evaluation.  The API is based on the OpenAPI 3.0.3 specification.

    The version of the OpenAPI document: 0.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from swagger_client.models.scenario import Scenario

class TestScenario(unittest.TestCase):
    """Scenario unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Scenario:
        """Test Scenario
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Scenario`
        """
        model = Scenario()
        if include_optional:
            return Scenario(
                id = '',
                name = '',
                first_scene = '',
                session_complete = True,
                state = swagger_client.models.state.State(),
                scenes = [
                    swagger_client.models.scene.Scene(
                        id = '', 
                        state = swagger_client.models.state.State(), 
                        next_scene = '', 
                        end_scene_allowed = True, 
                        persist_characters = True, 
                        removed_characters = [
                            ''
                            ], 
                        probe_config = [
                            swagger_client.models.probe_config.ProbeConfig(
                                probe_id = '', 
                                description = '', )
                            ], 
                        action_mapping = [
                            swagger_client.models.action_mapping.ActionMapping(
                                action_id = 'action_01', 
                                action_type = 'END_SCENE', 
                                unstructured = '', 
                                repeatable = True, 
                                character_id = '', 
                                intent_action = True, 
                                threat_state = {"unstructured":"Gunshots have been reported in the surrounding area","threats":[{"type":"gunfire","severity":"moderate"}]}, 
                                parameters = [{"character_id":"Mike"}], 
                                probe_id = '', 
                                choice = '', 
                                next_scene = '', 
                                kdma_association = {
                                    'key' : 0.0
                                    }, 
                                action_condition_semantics = 'and', 
                                action_conditions = swagger_client.models.conditions.Conditions(), 
                                probe_condition_semantics = 'and', 
                                probe_conditions = swagger_client.models.conditions.Conditions(), )
                            ], 
                        restricted_actions = ["SEARCH"], 
                        transition_semantics = 'and', 
                        transitions = swagger_client.models.conditions.Conditions(), )
                    ]
            )
        else:
            return Scenario(
                id = '',
                name = '',
        )
        """

    def testScenario(self):
        """Test Scenario"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
