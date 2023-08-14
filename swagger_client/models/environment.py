# coding: utf-8

"""
    ITM TA3 API

    This is the specification of the TA3 API for In The Moment (ITM).  Currently, the Evaluation API for TA2 supports functionality for the September milestone.  The API is based on the OpenAPI 3.0 specification.  # noqa: E501

    OpenAPI spec version: 0.2.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Environment(object):
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
        'unstructured': 'str',
        'weather': 'str',
        'location': 'str',
        'terrain': 'str',
        'flora': 'str',
        'fauna': 'str',
        'soundscape': 'str',
        'aid_delay': 'float',
        'temperature': 'float',
        'humidity': 'float',
        'lighting': 'float',
        'visibility': 'float',
        'noise_ambient': 'float',
        'noise_peak': 'float'
    }

    attribute_map = {
        'unstructured': 'unstructured',
        'weather': 'weather',
        'location': 'location',
        'terrain': 'terrain',
        'flora': 'flora',
        'fauna': 'fauna',
        'soundscape': 'soundscape',
        'aid_delay': 'aidDelay',
        'temperature': 'temperature',
        'humidity': 'humidity',
        'lighting': 'lighting',
        'visibility': 'visibility',
        'noise_ambient': 'noise_ambient',
        'noise_peak': 'noise_peak'
    }

    def __init__(self, unstructured=None, weather=None, location=None, terrain=None, flora=None, fauna=None, soundscape=None, aid_delay=None, temperature=None, humidity=None, lighting=None, visibility=None, noise_ambient=None, noise_peak=None):  # noqa: E501
        """Environment - a model defined in Swagger"""  # noqa: E501
        self._unstructured = None
        self._weather = None
        self._location = None
        self._terrain = None
        self._flora = None
        self._fauna = None
        self._soundscape = None
        self._aid_delay = None
        self._temperature = None
        self._humidity = None
        self._lighting = None
        self._visibility = None
        self._noise_ambient = None
        self._noise_peak = None
        self.discriminator = None
        self.unstructured = unstructured
        if weather is not None:
            self.weather = weather
        if location is not None:
            self.location = location
        if terrain is not None:
            self.terrain = terrain
        if flora is not None:
            self.flora = flora
        if fauna is not None:
            self.fauna = fauna
        if soundscape is not None:
            self.soundscape = soundscape
        if aid_delay is not None:
            self.aid_delay = aid_delay
        if temperature is not None:
            self.temperature = temperature
        if humidity is not None:
            self.humidity = humidity
        if lighting is not None:
            self.lighting = lighting
        if visibility is not None:
            self.visibility = visibility
        if noise_ambient is not None:
            self.noise_ambient = noise_ambient
        if noise_peak is not None:
            self.noise_peak = noise_peak

    @property
    def unstructured(self):
        """Gets the unstructured of this Environment.  # noqa: E501

        a natural language description of the environment  # noqa: E501

        :return: The unstructured of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._unstructured

    @unstructured.setter
    def unstructured(self, unstructured):
        """Sets the unstructured of this Environment.

        a natural language description of the environment  # noqa: E501

        :param unstructured: The unstructured of this Environment.  # noqa: E501
        :type: str
        """
        if unstructured is None:
            raise ValueError("Invalid value for `unstructured`, must not be `None`")  # noqa: E501

        self._unstructured = unstructured

    @property
    def weather(self):
        """Gets the weather of this Environment.  # noqa: E501

        a natural language description of local weather conditions  # noqa: E501

        :return: The weather of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._weather

    @weather.setter
    def weather(self, weather):
        """Sets the weather of this Environment.

        a natural language description of local weather conditions  # noqa: E501

        :param weather: The weather of this Environment.  # noqa: E501
        :type: str
        """

        self._weather = weather

    @property
    def location(self):
        """Gets the location of this Environment.  # noqa: E501

        a natural language description of where the scenario takes place  # noqa: E501

        :return: The location of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Environment.

        a natural language description of where the scenario takes place  # noqa: E501

        :param location: The location of this Environment.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def terrain(self):
        """Gets the terrain of this Environment.  # noqa: E501

        a natural language description of the local terrain  # noqa: E501

        :return: The terrain of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._terrain

    @terrain.setter
    def terrain(self, terrain):
        """Sets the terrain of this Environment.

        a natural language description of the local terrain  # noqa: E501

        :param terrain: The terrain of this Environment.  # noqa: E501
        :type: str
        """

        self._terrain = terrain

    @property
    def flora(self):
        """Gets the flora of this Environment.  # noqa: E501

        a natural language description of the local flora  # noqa: E501

        :return: The flora of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._flora

    @flora.setter
    def flora(self, flora):
        """Sets the flora of this Environment.

        a natural language description of the local flora  # noqa: E501

        :param flora: The flora of this Environment.  # noqa: E501
        :type: str
        """

        self._flora = flora

    @property
    def fauna(self):
        """Gets the fauna of this Environment.  # noqa: E501

        a natural language description of the local fauna  # noqa: E501

        :return: The fauna of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._fauna

    @fauna.setter
    def fauna(self, fauna):
        """Sets the fauna of this Environment.

        a natural language description of the local fauna  # noqa: E501

        :param fauna: The fauna of this Environment.  # noqa: E501
        :type: str
        """

        self._fauna = fauna

    @property
    def soundscape(self):
        """Gets the soundscape of this Environment.  # noqa: E501

        a natural language description of the local soundscape  # noqa: E501

        :return: The soundscape of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._soundscape

    @soundscape.setter
    def soundscape(self, soundscape):
        """Sets the soundscape of this Environment.

        a natural language description of the local soundscape  # noqa: E501

        :param soundscape: The soundscape of this Environment.  # noqa: E501
        :type: str
        """

        self._soundscape = soundscape

    @property
    def aid_delay(self):
        """Gets the aid_delay of this Environment.  # noqa: E501

        time until tactical evacuation or exfiltration, in minutes  # noqa: E501

        :return: The aid_delay of this Environment.  # noqa: E501
        :rtype: float
        """
        return self._aid_delay

    @aid_delay.setter
    def aid_delay(self, aid_delay):
        """Sets the aid_delay of this Environment.

        time until tactical evacuation or exfiltration, in minutes  # noqa: E501

        :param aid_delay: The aid_delay of this Environment.  # noqa: E501
        :type: float
        """

        self._aid_delay = aid_delay

    @property
    def temperature(self):
        """Gets the temperature of this Environment.  # noqa: E501

        numerical temperature in degrees Fahrenheit  # noqa: E501

        :return: The temperature of this Environment.  # noqa: E501
        :rtype: float
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this Environment.

        numerical temperature in degrees Fahrenheit  # noqa: E501

        :param temperature: The temperature of this Environment.  # noqa: E501
        :type: float
        """

        self._temperature = temperature

    @property
    def humidity(self):
        """Gets the humidity of this Environment.  # noqa: E501

        percentage of relative humidity  # noqa: E501

        :return: The humidity of this Environment.  # noqa: E501
        :rtype: float
        """
        return self._humidity

    @humidity.setter
    def humidity(self, humidity):
        """Sets the humidity of this Environment.

        percentage of relative humidity  # noqa: E501

        :param humidity: The humidity of this Environment.  # noqa: E501
        :type: float
        """

        self._humidity = humidity

    @property
    def lighting(self):
        """Gets the lighting of this Environment.  # noqa: E501

        an numeric indicator (0-1) of current lighting conditions (natural or man-made); lower is darker  # noqa: E501

        :return: The lighting of this Environment.  # noqa: E501
        :rtype: float
        """
        return self._lighting

    @lighting.setter
    def lighting(self, lighting):
        """Sets the lighting of this Environment.

        an numeric indicator (0-1) of current lighting conditions (natural or man-made); lower is darker  # noqa: E501

        :param lighting: The lighting of this Environment.  # noqa: E501
        :type: float
        """

        self._lighting = lighting

    @property
    def visibility(self):
        """Gets the visibility of this Environment.  # noqa: E501

        an numeric indicator (0-1) of current visibility conditions; lower is darker. Affected by time of day, lighting, weather, terrain, etc.  # noqa: E501

        :return: The visibility of this Environment.  # noqa: E501
        :rtype: float
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this Environment.

        an numeric indicator (0-1) of current visibility conditions; lower is darker. Affected by time of day, lighting, weather, terrain, etc.  # noqa: E501

        :param visibility: The visibility of this Environment.  # noqa: E501
        :type: float
        """

        self._visibility = visibility

    @property
    def noise_ambient(self):
        """Gets the noise_ambient of this Environment.  # noqa: E501

        an numeric indicator (0-1) of ambient noise at the scenario location; higher is louder  # noqa: E501

        :return: The noise_ambient of this Environment.  # noqa: E501
        :rtype: float
        """
        return self._noise_ambient

    @noise_ambient.setter
    def noise_ambient(self, noise_ambient):
        """Sets the noise_ambient of this Environment.

        an numeric indicator (0-1) of ambient noise at the scenario location; higher is louder  # noqa: E501

        :param noise_ambient: The noise_ambient of this Environment.  # noqa: E501
        :type: float
        """

        self._noise_ambient = noise_ambient

    @property
    def noise_peak(self):
        """Gets the noise_peak of this Environment.  # noqa: E501

        an numeric indicator (0-1) of peak noise at the scenario location; higher is louder  # noqa: E501

        :return: The noise_peak of this Environment.  # noqa: E501
        :rtype: float
        """
        return self._noise_peak

    @noise_peak.setter
    def noise_peak(self, noise_peak):
        """Sets the noise_peak of this Environment.

        an numeric indicator (0-1) of peak noise at the scenario location; higher is louder  # noqa: E501

        :param noise_peak: The noise_peak of this Environment.  # noqa: E501
        :type: float
        """

        self._noise_peak = noise_peak

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
        if issubclass(Environment, dict):
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
        if not isinstance(other, Environment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
