# coding: utf-8

"""
    ITM TA3 API

    This is the specification of the TA3 API for In The Moment (ITM).  Currently, the Evaluation API for TA2 supports functionality for the September milestone.  The API is based on the OpenAPI 3.0 specification.  # noqa: E501

    OpenAPI spec version: 0.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Casualty(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'unstructured': 'str',
        'name': 'str',
        'demographics': 'Demographics',
        'injuries': 'list[Injury]',
        'vitals': 'Vitals',
        'assessed': 'bool',
        'tag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'unstructured': 'unstructured',
        'name': 'name',
        'demographics': 'demographics',
        'injuries': 'injuries',
        'vitals': 'vitals',
        'assessed': 'assessed',
        'tag': 'tag'
    }

    def __init__(self, id=None, unstructured=None, name=None, demographics=None, injuries=None, vitals=None, assessed=False, tag=None):  # noqa: E501
        """Casualty - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._unstructured = None
        self._name = None
        self._demographics = None
        self._injuries = None
        self._vitals = None
        self._assessed = None
        self._tag = None
        self.discriminator = None
        self.id = id
        self.unstructured = unstructured
        if name is not None:
            self.name = name
        if demographics is not None:
            self.demographics = demographics
        if injuries is not None:
            self.injuries = injuries
        if vitals is not None:
            self.vitals = vitals
        if assessed is not None:
            self.assessed = assessed
        if tag is not None:
            self.tag = tag

    @property
    def id(self):
        """Gets the id of this Casualty.  # noqa: E501

        string, globally unique casualty identifier  # noqa: E501

        :return: The id of this Casualty.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Casualty.

        string, globally unique casualty identifier  # noqa: E501

        :param id: The id of this Casualty.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def unstructured(self):
        """Gets the unstructured of this Casualty.  # noqa: E501

        natural language text description of the casualty  # noqa: E501

        :return: The unstructured of this Casualty.  # noqa: E501
        :rtype: str
        """
        return self._unstructured

    @unstructured.setter
    def unstructured(self, unstructured):
        """Sets the unstructured of this Casualty.

        natural language text description of the casualty  # noqa: E501

        :param unstructured: The unstructured of this Casualty.  # noqa: E501
        :type: str
        """
        if unstructured is None:
            raise ValueError("Invalid value for `unstructured`, must not be `None`")  # noqa: E501

        self._unstructured = unstructured

    @property
    def name(self):
        """Gets the name of this Casualty.  # noqa: E501

        the name of the casualty, omit if unknown  # noqa: E501

        :return: The name of this Casualty.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Casualty.

        the name of the casualty, omit if unknown  # noqa: E501

        :param name: The name of this Casualty.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def demographics(self):
        """Gets the demographics of this Casualty.  # noqa: E501


        :return: The demographics of this Casualty.  # noqa: E501
        :rtype: Demographics
        """
        return self._demographics

    @demographics.setter
    def demographics(self, demographics):
        """Sets the demographics of this Casualty.


        :param demographics: The demographics of this Casualty.  # noqa: E501
        :type: Demographics
        """

        self._demographics = demographics

    @property
    def injuries(self):
        """Gets the injuries of this Casualty.  # noqa: E501

        an array of casualty injuries  # noqa: E501

        :return: The injuries of this Casualty.  # noqa: E501
        :rtype: list[Injury]
        """
        return self._injuries

    @injuries.setter
    def injuries(self, injuries):
        """Sets the injuries of this Casualty.

        an array of casualty injuries  # noqa: E501

        :param injuries: The injuries of this Casualty.  # noqa: E501
        :type: list[Injury]
        """

        self._injuries = injuries

    @property
    def vitals(self):
        """Gets the vitals of this Casualty.  # noqa: E501


        :return: The vitals of this Casualty.  # noqa: E501
        :rtype: Vitals
        """
        return self._vitals

    @vitals.setter
    def vitals(self, vitals):
        """Sets the vitals of this Casualty.


        :param vitals: The vitals of this Casualty.  # noqa: E501
        :type: Vitals
        """

        self._vitals = vitals

    @property
    def assessed(self):
        """Gets the assessed of this Casualty.  # noqa: E501

        whether or not this casualty has been assessed in the current scenario  # noqa: E501

        :return: The assessed of this Casualty.  # noqa: E501
        :rtype: bool
        """
        return self._assessed

    @assessed.setter
    def assessed(self, assessed):
        """Sets the assessed of this Casualty.

        whether or not this casualty has been assessed in the current scenario  # noqa: E501

        :param assessed: The assessed of this Casualty.  # noqa: E501
        :type: bool
        """

        self._assessed = assessed

    @property
    def tag(self):
        """Gets the tag of this Casualty.  # noqa: E501

        the tag assigned to this casualty, omit if untagged  # noqa: E501

        :return: The tag of this Casualty.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Casualty.

        the tag assigned to this casualty, omit if untagged  # noqa: E501

        :param tag: The tag of this Casualty.  # noqa: E501
        :type: str
        """
        allowed_values = ["minimal", "delayed", "immediate", "expectant", "deceased"]  # noqa: E501
        if tag not in allowed_values:
            raise ValueError(
                "Invalid value for `tag` ({0}), must be one of {1}"  # noqa: E501
                .format(tag, allowed_values)
            )

        self._tag = tag

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Casualty, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Casualty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
