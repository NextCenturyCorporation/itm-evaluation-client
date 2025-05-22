import swagger_client
from swagger_client.configuration import Configuration
from swagger_client.api_client import ApiClient
from swagger_client.models import Scenario
from abc import ABC, abstractmethod
import os
import random

def get_swagger_class_enum_values(klass):
    return [getattr(klass,i) for i in dir(klass) if not i.startswith("_") and isinstance(getattr(klass,i), str)]

# Some SoarTech individual targets
soartech_qol_alignment_targets = ['qol-human-8022671-SplitLowMulti-ph1', 'qol-human-7040555-SplitHighMulti-ph1', 'qol-synth-LowCluster-ph1']
soartech_vol_alignment_targets = ['vol-human-8478698-SplitLowMulti-ph1', 'vol-human-8022671-SplitHighMulti-ph1', 'vol-synth-LowCluster-ph1']
# SoarTech group targets
#soartech_qol_alignment_targets = ['qol-group-target-ph1-1', 'qol-group-target-ph1-2']
#soartech_vol_alignment_targets = ['vol-group-target-ph1-1', 'vol-group-target-ph1-2']
SOARTECH_QOL_ALIGNMENT = random.choice(soartech_qol_alignment_targets)
SOARTECH_VOL_ALIGNMENT = random.choice(soartech_vol_alignment_targets)

# Some ADEPT individual targets
adept_mj_alignment_targets = ['ADEPT-DryRun-Moral judgement-0.2', 'ADEPT-DryRun-Moral judgement-0.5', 'ADEPT-DryRun-Moral judgement-0.8']
adept_io_alignment_targets = ['ADEPT-DryRun-Ingroup Bias-0.2', 'ADEPT-DryRun-Ingroup Bias-0.5', 'ADEPT-DryRun-Ingroup Bias-0.8']
adept_mf_alignment_targets = ['ADEPT-June2025-merit-0.5', 'ADEPT-June2025-affiliation_merit-0.0_1.0']
adept_af_alignment_targets = ['ADEPT-June2025-affiliation-0.5', 'ADEPT-June2025-affiliation_merit-0.0_1.0']
adept_ss_alignment_targets = ['ADEPT-June2025-search-0.5', 'ADEPT-June2025-search-0.7']
adept_ps_alignment_targets = ['ADEPT-June2025-personal_safety-0.3', 'ADEPT-June2025-personal_safety-0.8']
# ADEPT group targets
#adept_mj_alignment_targets = ['ADEPT-DryRun-Moral judgement-Group-Low', 'ADEPT-DryRun-Moral judgement-Group-High']
#adept_io_alignment_targets = ['ADEPT-DryRun-Ingroup Bias-Group-Low', 'ADEPT-DryRun-Ingroup Bias-Group-High']
ADEPT_MJ_ALIGNMENT = random.choice(adept_mj_alignment_targets)
ADEPT_IO_ALIGNMENT = random.choice(adept_io_alignment_targets)
ADEPT_MF_ALIGNMENT = random.choice(adept_mf_alignment_targets)
ADEPT_AF_ALIGNMENT = random.choice(adept_af_alignment_targets)
ADEPT_SS_ALIGNMENT = random.choice(adept_ss_alignment_targets)
ADEPT_PS_ALIGNMENT = random.choice(adept_ps_alignment_targets)

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
