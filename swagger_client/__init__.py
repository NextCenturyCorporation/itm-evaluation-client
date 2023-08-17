# coding: utf-8

# flake8: noqa

"""
    ITM TA3 API

    This is the specification of the TA3 API for In The Moment (ITM).  Currently, the Evaluation API for TA2 supports functionality for the September milestone.  The API is based on the OpenAPI 3.0 specification.  # noqa: E501

    OpenAPI spec version: 0.2.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.itm_ta2_eval_api import ItmTa2EvalApi
# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.action import Action
from swagger_client.models.alignment_target import AlignmentTarget
from swagger_client.models.casualty import Casualty
from swagger_client.models.demographics import Demographics
from swagger_client.models.environment import Environment
from swagger_client.models.injury import Injury
from swagger_client.models.kdma_value import KDMAValue
from swagger_client.models.mission import Mission
from swagger_client.models.scenario import Scenario
from swagger_client.models.state import State
from swagger_client.models.supplies import Supplies
from swagger_client.models.threat import Threat
from swagger_client.models.threat_state import ThreatState
from swagger_client.models.triage_category import TriageCategory
from swagger_client.models.vitals import Vitals
