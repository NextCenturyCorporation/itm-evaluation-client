import random
from enum import Enum
from dataclasses import dataclass
from typing import List
from swagger_client.models import (
    Scenario,
    State,
    Casualty,
    Supplies,
    Environment,
    Action,
    AlignmentTarget
)
from .itm_scenario_runner import ScenarioRunner


class TagTypeAndPriority(Enum):
    MINIMAL = ("MINIMAL", 1)
    DELAYED = ("DELAYED", 2)
    IMMEDIATE = ("IMMEDIATE", 3)
    EXPECTANT = ("EXPECTANT", 4)

    def __new__(cls, tag_type, priority):
        obj = object.__new__(cls)
        obj._value_ = tag_type
        obj.priority = priority
        return obj

    @classmethod
    def get_enum_by_priority(cls, priority):
        for tag_type in cls:
            if tag_type.priority == priority:
                return tag_type
        raise ValueError("Invalid priority")

@dataclass
class ADMKnowledge:
    """
    What the ADM keeps track of throughout the scenario.
    """
    # Scenario
    scenario_id: str = None
    scenario: Scenario = None
    scenario_complete: bool = False

    # Info
    description: str = None
    environment: Environment = None

    # casualties
    casualties: List[Casualty] = None
    all_casualty_ids: List[str] = None
    treated_casualty_ids: List[str] = None

    # Actions
    scenario_actions_taken = 0
    action_choices: List[str] = None

    # Supplies
    supplies: List[Supplies] = None

    alignment_target: AlignmentTarget = None


class ADMScenarioRunner(ScenarioRunner):

    def __init__(self, save_to_db, scene_type, session_type=None,
                 max_scenarios=0, eval_mode=False):
        super().__init__()
        self.session_id = None
        self.adm_name = scene_type + "ITM ADM4" + save_to_db
        self.adm_knowledge: ADMKnowledge = None
        self.session_type = session_type
        self.max_scenarios = max_scenarios
        self.eval_mode = eval_mode
        self.scenarios_run = 0
        self.total_actions_taken = 0


    def run(self):
        self.run_session()

    def run_session(self):
        self.start_session()
        # Run until an empty scenario is returned
        while True:
            is_empty_scenario = self.retrieve_scenario()
            if is_empty_scenario:
                break
            while not self.adm_knowledge.scenario_complete:
                actions: List[Action] = self.itm.get_available_actions(session_id=self.session_id, scenario_id=self.adm_knowledge.scenario.id)
                action = self.get_next_action(self.adm_knowledge.scenario, self.adm_knowledge.scenario.state, self.adm_knowledge.alignment_target, actions)
                state = self.itm.take_action(session_id=self.session_id, body=action)
                self.adm_knowledge.scenario_actions_taken += 1
                self.adm_knowledge.action_choices.append(action.action_type)
                self.total_actions_taken += 1
                self.adm_knowledge.scenario_complete = state.scenario_complete
            self.scenarios_run += 1
            self.end_scenario()
        self.end_session()

    def end_scenario(self):
        print(f"-------- Scenario {self.scenarios_run} ---------")
        print(f"Scenario actions taken: {self.adm_knowledge.scenario_actions_taken}")
        print(f"Actions taken in Order: {self.adm_knowledge.action_choices}\n")
        self.adm_knowledge = ADMKnowledge()

    def end_session(self):
        print(f"[End Session with id: {self.session_id}]")
        print(f"Session Ended for user: {self.adm_name}")
        print(f"Scenarios run: {self.scenarios_run}")
        print(f"Session actions taken: {self.total_actions_taken}")

    def start_session(self):
        print(f"[Start Session]: {self.session_type}")
        if self.eval_mode:
            self.session_id = self.itm.start_session(
                adm_name=self.adm_name,
                session_type='eval',
                max_scenarios=0
            )
        else:
            self.session_id = self.itm.start_session(
                adm_name=self.adm_name,
                session_type=self.session_type,
                max_scenarios=self.max_scenarios
            )

    def retrieve_scenario(self):
        self.adm_knowledge = ADMKnowledge() 
        scenario: Scenario = self.itm.start_scenario(self.session_id)
        if scenario.session_complete:
            return True
        self.set_scenario(scenario)
        self.adm_knowledge.alignment_target = \
            self.itm.get_alignment_target(self.session_id, self.adm_knowledge.scenario.id)
        return False

    def set_scenario(self, scenario):
        self.adm_knowledge.scenario = scenario
        state: State = scenario.state
        self.adm_knowledge.scenario_id = scenario.id
        self.adm_knowledge.casualties = state.casualties
        self.adm_knowledge.all_casualty_ids = [
            casualty.id for casualty in state.casualties]
        self.adm_knowledge.treated_casualty_ids = []
        self.adm_knowledge.action_choices = []
        self.adm_knowledge.supplies = state.supplies
        self.adm_knowledge.environment = state.environment
        self.adm_knowledge.description = state.mission.unstructured

    def get_next_action(self, scenario: Scenario, state: State, alignment_target: AlignmentTarget,
                    actions: List[Action]):
        available_locations = ["right forearm", "left forearm", "right calf", "left calf", "right thigh", "left thigh", "right stomach", "left stomach", "right bicep", "left bicep", "right shoulder", "left shoulder", "right side", "left side", "right chest", "left chest", "right wrist", "left wrist", "left face", "right face", "left neck", "right neck", "unspecified"]
        available_supplies = ["Tourniquet", "Pressure bandage", "Hemostatic gauze", "Decompression Needle", "Nasopharyngeal airway"]

        random_action = random.choice(actions)
        if random_action.action_type != "DIRECT_MOBILE_CASUALTIES":
            # All but Direct Mobile Casualties requires a casualty ID
            if random_action.casualty_id is None:
                random_action.casualty_id = self.get_random_casualty_id(self)
            if random_action.action_type == "APPLY_TREATMENT":
                if random_action.parameters is None:
<<<<<<< HEAD
                    random_action.parameters = {"location": random.choice(available_locations),"treatment": random.choice(available_supplies)}
=======
                    random_action.parameters = {"location": random.choice(available_locations), "treatment": random.choice(available_supplies)}
>>>>>>> 536f16c42d1507a05769cfcd2d782c825ac23e50
                else :
                   if not random_action.parameters['location'] or random_action.parameters["location"] is None:
                        random_action.parameters["location"] = random.choice(available_locations)
                   if not random_action.parameters['treatment'] or random_action.parameters["treatment"] is None:
                        random_action.parameters["treatment"] = random.choice(available_supplies)
        # fill in any missing fields with random values
        return random_action

    def get_random_casualty_id(self):
        #id = random.choice(self.adm_knowledge.all_casualty_ids)
        #casualties : List[Casualty] = self.adm_knowledge.casualties
        return random.choice(self.adm_knowledge.all_casualty_ids)

    def assess_casualty_priority(self):
        casualty_priority = random.randint(1, 5)
        tag = TagTypeAndPriority.get_enum_by_priority(casualty_priority)
        return tag.value
