# coding: utf-8

"""
    ITM TA3 API

    This is the specification of the TA3 API for In The Moment (ITM).  Currently, the Evaluation API for TA2 supports functionality for the Phase 1 Evaluation.  The API is based on the OpenAPI 3.0.3 specification.

    The version of the OpenAPI document: 0.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from swagger_client.models.demographics import Demographics
from swagger_client.models.rapport_enum import RapportEnum
from typing import Optional, Set
from typing_extensions import Self

class Character(BaseModel):
    """
    a character in the scene
    """ # noqa: E501
    medical_condition: Optional[Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = Field(default=None, description="The treatment priority/urgency of a patient's medical condition, 0-1 scale")
    attribute_rating: Optional[Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = Field(default=None, description="A scenario-specific characteristic of the patient or situation regarding the patient, 0-1 scale:   Merit Focus (MF): degree of blame for a patient: 0.0 doesn't consider merit when deciding who to treat / always treats the medically favored patient; 1.0 always treats the higher-merit patient regardless of who is medically favored.   Affiliation Focus (AF): degree of closeness for a patient: 0.0 doesn't consider affiliation / always treats the medically favored patient; 1.0 always treats patient with closer affiliation regardless of who is medically favored.   Search vs. Stay (SS): urgency to search for/treat a patient: 0.0 always stays despite how urgent the need is to treat patient in next room; 1.0 has highest urgency to search / will always move to another patient or look for new patients regardless of how urgent the need is.   Personal Safety Focus (PS): amount of danger to reach a patient: 0.0 doesn't consider personal safety and always switches to the medically favored patient; 1.0 won't risk personal safety / always stays in safest place regardless of who is medically favored. ")
    id: StrictStr = Field(description="A unique character ID throughout the scenario")
    name: StrictStr = Field(description="display name, as in a dashboard")
    unstructured: StrictStr = Field(description="Natural language, plain text description of the character")
    demographics: Demographics
    rapport: Optional[RapportEnum] = None
    unseen: Optional[StrictBool] = Field(default=False, description="whether or not this character is visible in the scene or merely heard or reported about from a nearby location")
    __properties: ClassVar[List[str]] = ["medical_condition", "attribute_rating", "id", "name", "unstructured", "demographics", "rapport", "unseen"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Character from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of demographics
        if self.demographics:
            _dict['demographics'] = self.demographics.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Character from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "medical_condition": obj.get("medical_condition"),
            "attribute_rating": obj.get("attribute_rating"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "unstructured": obj.get("unstructured"),
            "demographics": Demographics.from_dict(obj["demographics"]) if obj.get("demographics") is not None else None,
            "rapport": obj.get("rapport"),
            "unseen": obj.get("unseen") if obj.get("unseen") is not None else False
        })
        return _obj


