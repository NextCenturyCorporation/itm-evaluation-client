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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from swagger_client.models.kde_data import KDEData
from typing import Optional, Set
from typing_extensions import Self

class KDMAValue(BaseModel):
    """
    Single KDMA value with value(s) between 0 and 1, or a kernel density estimate of the KDMA value.
    """ # noqa: E501
    kdma: StrictStr = Field(description="Name of KDMA")
    value: Optional[Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = Field(default=None, description="Numeric score for a given KDMA, 0-1 scale")
    scores: Optional[List[Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]]]] = Field(default=None, description="Ordered KDMA scores")
    kdes: Optional[Dict[str, KDEData]] = Field(default=None, description="KDE Objects representing a KDMA Measurement")
    __properties: ClassVar[List[str]] = ["kdma", "value", "scores", "kdes"]

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
        """Create an instance of KDMAValue from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in kdes (dict)
        _field_dict = {}
        if self.kdes:
            for _key_kdes in self.kdes:
                if self.kdes[_key_kdes]:
                    _field_dict[_key_kdes] = self.kdes[_key_kdes].to_dict()
            _dict['kdes'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KDMAValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "kdma": obj.get("kdma"),
            "value": obj.get("value"),
            "scores": obj.get("scores"),
            "kdes": dict(
                (_k, KDEData.from_dict(_v))
                for _k, _v in obj["kdes"].items()
            )
            if obj.get("kdes") is not None
            else None
        })
        return _obj


