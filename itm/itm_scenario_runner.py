import swagger_client
from swagger_client.configuration import Configuration
from swagger_client.api_client import ApiClient
from swagger_client.models import Scenario
from abc import ABC, abstractmethod
import os
import random

def get_swagger_class_enum_values(klass):
    return [getattr(klass,i) for i in dir(klass) if not i.startswith("_") and isinstance(getattr(klass,i), str)]

# TODO: ITM-229: Facilitate running against two eval alignment targets
soartech_alignment_targets = ['maximization_high', 'maximization_low']
SOARTECH_ALIGNMENT = random.choice(soartech_alignment_targets)
adept_alignment_targets = ['ADEPT-metrics_eval-alignment-target-train-HIGH', 'ADEPT-metrics_eval-alignment-target-train-LOW']
ADEPT_ALIGNMENT = random.choice(adept_alignment_targets)

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
        PORT = os.getenv('TA3_PORT')
        if (PORT == None or PORT == ""):
            PORT = "8080"
        config.host = f"http://{HOST}:{PORT}"
        api_client = ApiClient(configuration=config)
        return swagger_client.ItmTa2EvalApi(api_client=api_client)


    @abstractmethod
    def run(self):
        pass
