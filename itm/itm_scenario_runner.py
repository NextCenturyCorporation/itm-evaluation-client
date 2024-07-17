import swagger_client
from swagger_client.configuration import Configuration
from swagger_client.api_client import ApiClient
from swagger_client.models import Scenario
from abc import ABC, abstractmethod
import os
import random

def get_swagger_class_enum_values(klass):
    return [getattr(klass,i) for i in dir(klass) if not i.startswith("_") and isinstance(getattr(klass,i), str)]

soartech_qol_alignment_targets = ['qol_1', 'qol_5', 'qol_9']
soartech_vol_alignment_targets = ['vol_1', 'vol_5', 'vol_9']
SOARTECH_QOL_ALIGNMENT = random.choice(soartech_qol_alignment_targets)
SOARTECH_VOL_ALIGNMENT = random.choice(soartech_vol_alignment_targets)
adept_mj_alignment_targets = ['ADEPT-DryRun-Moral judgement-0.1', 'ADEPT-DryRun-Moral judgement-0.5', 'ADEPT-DryRun-Moral judgement-0.9']
adept_io_alignment_targets = ['ADEPT-DryRun-Ingroup Bias-0.1', 'ADEPT-DryRun-Ingroup Bias-0.5', 'ADEPT-DryRun-Ingroup Bias-0.9']
ADEPT_MJ_ALIGNMENT = random.choice(adept_mj_alignment_targets)
ADEPT_IO_ALIGNMENT = random.choice(adept_io_alignment_targets)

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
