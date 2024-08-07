import random
from enum import Enum
from dataclasses import dataclass
from typing import List
from swagger_client.models import (
    Scenario,
    State,
    Character,
    Supplies,
    Environment,
    Action,
    AlignmentTarget
)
from swagger_client.models.action_type_enum import ActionTypeEnum
from swagger_client.models.injury_location_enum import InjuryLocationEnum
from .itm_scenario_runner import ScenarioRunner, get_swagger_class_enum_values


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

    # characters
    characters: List[Character] = None
    all_character_ids: List[str] = None

    # Actions
    scenario_actions_taken = 0
    action_choices: List[str] = None

    # Supplies
    supplies: List[Supplies] = None

    alignment_target: AlignmentTarget = None


class ADMScenarioRunner(ScenarioRunner):

    def __init__(self, session_type, adm_profile=None, max_scenarios=0, scenario_id=None):
        super().__init__()
        self.session_id = None
        self.adm_name = "ITM ADM"
        self.adm_profile = adm_profile
        self.eval_mode = session_type == 'eval'
        self.adm_knowledge: ADMKnowledge = None
        self.session_type = session_type
        self.custom_scenario_id = scenario_id
        self.max_scenarios = max_scenarios
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
                state = self.itm.take_action(session_id=self.session_id, body=action) if not action.intent_action else self.itm.intend_action(session_id=self.session_id, body=action)
                self.update_scenario(state)
                self.adm_knowledge.scenario_actions_taken += 1
                self.adm_knowledge.action_choices.append(action.action_type)
                self.total_actions_taken += 1
                self.adm_knowledge.scenario_complete = state.scenario_complete
                if state.scenario_complete:
                    self.adm_knowledge.scenario.state.unstructured = state.unstructured
            self.scenarios_run += 1
            self.end_scenario()
        self.end_session()

    def end_scenario(self):
        print(f"-------- Scenario {self.scenarios_run} ---------")
        print(f"{self.adm_knowledge.scenario.state.unstructured}")
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
                adm_profile=self.adm_profile,
                max_scenarios=0
            )
        else:
            self.session_id = self.itm.start_session(
                adm_name=self.adm_name,
                session_type=self.session_type,
                adm_profile=self.adm_profile,
                max_scenarios=self.max_scenarios
            )

    def retrieve_scenario(self):
        self.adm_knowledge = ADMKnowledge() 
        if self.custom_scenario_id:
            scenario = self.itm.start_scenario(session_id=self.session_id, scenario_id=self.custom_scenario_id)
        else:
            scenario = self.itm.start_scenario(session_id=self.session_id)
        if scenario.session_complete:
            return True
        self.set_scenario(scenario)
        self.adm_knowledge.alignment_target = \
            self.itm.get_alignment_target(self.session_id, self.adm_knowledge.scenario.id) if self.session_type != 'test' else None
        return False

    def set_scenario(self, scenario):
        self.adm_knowledge.scenario = scenario
        state: State = scenario.state
        self.adm_knowledge.scenario_id = scenario.id
        self.adm_knowledge.action_choices = []
        self.update_scenario(state)

    def update_scenario(self, state):
        self.adm_knowledge.characters = state.characters
        self.adm_knowledge.all_character_ids = [
            character.id for character in state.characters]
        self.adm_knowledge.supplies = state.supplies
        self.adm_knowledge.environment = state.environment
        self.adm_knowledge.description = state.mission.unstructured if state.mission else ''

    def get_next_action(self, scenario: Scenario, state: State, alignment_target: AlignmentTarget,
                    actions: List[Action]):
        available_locations = get_swagger_class_enum_values(InjuryLocationEnum)
        random_action = random.choice(actions)
        # Fill in any missing fields with random values
        if random_action.action_type not in [ActionTypeEnum.DIRECT_MOBILE_CHARACTERS, ActionTypeEnum.END_SCENE, ActionTypeEnum.MESSAGE, ActionTypeEnum.SITREP, ActionTypeEnum.SEARCH]:
            # Most actions require a character ID
            if random_action.character_id is None:
                random_action.character_id = self.get_random_character_id(random_action.action_type)
            if random_action.action_type == ActionTypeEnum.APPLY_TREATMENT:

                if not random_action.parameters:
                    random_action.parameters = {"location": random.choice(available_locations), "treatment": self.get_random_supply(state)}
                else:
                    if not random_action.parameters.get('location') or random_action.parameters['location'] is None:
                        random_action.parameters['location'] = random.choice(available_locations)
                    if not random_action.parameters.get('treatment') or random_action.parameters['treatment'] is None:
                        random_action.parameters['treatment'] = self.get_random_supply(state)
            elif random_action.action_type == ActionTypeEnum.TAG_CHARACTER:
                if not random_action.parameters:
                    random_action.parameters = {"category": self.assess_character_priority()}
            elif random_action.action_type == ActionTypeEnum.MOVE_TO_EVAC:
                if not random_action.parameters:
                    random_action.parameters = {"aid_id": self.get_random_aid_id(state)}
                    
        random_action.justification = "ADM Default Justification"
        return random_action

    def get_random_supply(self, state: State):
        supplies = [new_supply.type for new_supply in state.supplies if new_supply.quantity > 0]
        return random.choice(supplies)

    def get_random_character_id(self, action_type):
        if action_type in [ActionTypeEnum.MOVE_TO_EVAC]:
            characters : List[Character] = [character for character in self.adm_knowledge.characters]
        elif action_type in [ActionTypeEnum.MOVE_TO]:
            characters : List[Character] = [character for character in self.adm_knowledge.characters if character.unseen]
        else:
            characters : List[Character] = [character for character in self.adm_knowledge.characters if not character.unseen]
        index = random.randint(0, len(characters) - 1) if len(characters) > 1 else 0
        return characters[index].id

    def get_random_aid_id(self, state: State):
        aid_id = 'unknown evac'
        if state.environment.decision_environment and state.environment.decision_environment.aid:
            aids = state.environment.decision_environment.aid
            aid_ids = [aid.id for aid in aids if aids]
            aid_id = random.choice(aid_ids)
        return aid_id

    def assess_character_priority(self):
        character_priority = random.randint(1, 4)
        tag = TagTypeAndPriority.get_enum_by_priority(character_priority)
        return tag.value
