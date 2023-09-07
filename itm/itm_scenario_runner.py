import swagger_client
from swagger_client.configuration import Configuration
from swagger_client.api_client import ApiClient
from swagger_client.models import Scenario
from abc import ABC, abstractmethod
import os


class ScenarioRunner(ABC):
    def __init__(self):
        self.itm = self.setup_itm_session()
        self.username = ""
        self.scenario: Scenario = None

    def setup_itm_session(self):
        config = Configuration()
        HOST = os.getenv('TA3_HOSTNAME')
        if (HOST == None or HOST == ""):
            HOST = "127.0.0.1"
        config.host = "http://{HOST}:8080"
        api_client = ApiClient(configuration=config)
        return swagger_client.ItmTa2EvalApi(api_client=api_client)


    @abstractmethod
    def run(self):
        pass
