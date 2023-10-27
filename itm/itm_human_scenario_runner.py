from json import loads
from enum import Enum
from swagger_client.models import Scenario, State, Action
from swagger_client.rest import ApiException
from .itm_scenario_runner import ScenarioRunner
import traceback


class CommandOption(Enum):
    START_SESSION = "start_session (s)"
    START_SCENARIO = "start_scenario (c)"
    GET_ALIGNMENT_TARGET = "get_alignment_target (a)"
    GET_AVAILABLE_ACTIONS = "get_available_actions (v)"
    TAKE_ACTION = "take_action (t)"
    GET_SCENARIO_STATE = "get_scenario_state (u)"
    QUIT = "quit (q)"


class TagTypes(Enum):
    MINIMAL = "minimal (m)"
    DELAYED = "delayed (d)"
    IMMEDIATE = "immediate (i)"
    EXPECTANT = "expectant (e)"

ACTIONS_WITHOUT_CASUALTIES = ["DIRECT_MOBILE_CASUALTIES", "END_SCENARIO", "SITREP"]

class ITMHumanScenarioRunner(ScenarioRunner):
    def __init__(self, save_to_db, session_type, max_scenarios=-1):
        super().__init__()
        self.username = session_type + "ITM Human" + save_to_db
        self.session_type = session_type
        if max_scenarios > 0:
            self.max_scenarios = max_scenarios
        else:
            self.max_scenarios = None
        self.scenario_complete = False
        self.session_complete = False
        self.session_id = None
        self.scenario_id = None
        self.casualties = {}
        self.medical_supplies = {}
        self.available_actions = None
        self.actions_are_current = False
        self.current_probe_id = ''
        self.current_probe_text = ''
        self.current_probe_options = {}
        self.current_probe_answered = False

    def get_full_string_and_shortcut(self, parts):
        if isinstance(parts, CommandOption):
            parts = parts.value
        parts = parts.split()
        full = parts[0]
        shortcut = [parts[1][1]]
        return [full] + shortcut

    def prompt_casualty_id(self, none_allowed=False):
        if none_allowed:
            casualty_id = input(
                f"Enter Casualty Number from the list, or <Enter> for none:\n"
                f"  {[f'({i + 1}, {casualty.id})' for i, casualty in enumerate(self.casualties)]}: "
            )
            if not casualty_id:
                return ''
        else:
            casualty_id = input(
                f"Enter Casualty Number from the list:\n"
                f"  {[f'({i + 1}, {casualty.id})' for i, casualty in enumerate(self.casualties)]}: "
            )

        try:
            casualty_index = int(casualty_id) - 1
            if casualty_index < 0:
                raise ValueError()
            casualty_id = self.casualties[casualty_index].id
        except ValueError:
            return self.prompt_casualty_id()
        except IndexError:
            return self.prompt_casualty_id()
        return casualty_id

    def prompt_location(self):
        available_locations = ["right forearm", "left forearm", "right calf", "left calf", "right thigh", "left thigh", \
                               "right stomach", "left stomach", "right bicep", "left bicep", "right shoulder", "left shoulder", \
                               "right side", "left side", "right chest", "left chest", "right wrist", "left wrist", "left face", \
                               "right face", "left neck", "right neck", "unspecified"]
        location = input(
            f"Enter injury location by number from the list:\n"
            f"  {[f'({i + 1}, {location_name})' for i, location_name in enumerate(available_locations)]}: "
        )
        try:
            location_index = int(location) - 1
            if location_index < 0:
                raise ValueError()
            location = available_locations[location_index]
        except ValueError:
            return self.prompt_location()
        except IndexError:
            return self.prompt_location()
        return location

    def prompt_treatment(self):
        medical_supply = input(
            f"Enter Medical Supply Number from the list:\n"
            f"  {[f'({i + 1}, {medical_supply.type})' for i, medical_supply in enumerate(self.medical_supplies)]}: "
        )
        try:
            medical_supply_index = int(medical_supply) - 1
            if medical_supply_index < 0:
                raise ValueError()
            medical_supply = self.medical_supplies[medical_supply_index].type
        except ValueError:
            return self.prompt_treatment()
        return medical_supply

    def prompt_justification(self):
        justification = input(
            f"Enter optional justification, or <Enter> to skip: "
        )
        return justification

    def prompt_tagType(self):
        tag_name = input(
            f"Enter tag from following options "
            f"{[tag.value for tag in TagTypes]}: "
        ).lower()
        if len(tag_name) == 1:
            found = False
            for tag in [tag.value for tag in TagTypes]:
                tag_type = self.get_full_string_and_shortcut(tag)
                if tag_name == tag_type[1]:
                    tag_name = tag_type[0]
                    found = True
                    break
            if found:
                return tag_name.upper()
            else:
                return self.prompt_tagType()
        else:
            return self.prompt_tagType()

    def prompt_action(self) -> Action:
        action_id = input(
            f"Enter Action Number from the list:\n"
            f"  {[f'({i + 1}, {action.action_id})' for i, action in enumerate(self.available_actions)]}: "
        )
        try:
            action_index = int(action_id) - 1
            action = self.available_actions[action_index]
        except ValueError:
            return self.prompt_action()
        except IndexError:
            return self.prompt_action()
        return action

    def start_scenario_operation(self):
        if self.session_id == None:
            return "No active session; please start a session first."
        if self.scenario_id == None:
            response: Scenario = self.itm.start_scenario(self.session_id)
            self.current_probe_answered = False
            self.current_probe_id = ''
            if response.session_complete == False:
                self.scenario_id = response.id
                self.scenario = response
                state: State = response.state
                self.casualties = state.casualties
                self.medical_supplies = response.state.supplies
            else:
                self.session_complete = True
        else:
            response = "Scenario is already started."
        return response

    def start_session_operation(self, temp_username):
        if self.session_id == None:
            if self.max_scenarios == None:
                self.session_id = self.itm.start_session(temp_username, self.session_type)
            else:
                self.session_id = self.itm.start_session(temp_username, self.session_type, max_scenarios=self.max_scenarios)
            response = self.session_id
        else:
            response = "Session is already started."
        return response

    def get_alignment_target_operation(self):
        if self.session_id == None:
            return "No active session; please start a session first."
        if self.scenario_id == None:
            return "No active scenario; please start a scenario first."
        return self.itm.get_alignment_target(self.session_id, self.scenario_id)

    def get_scenario_state_operation(self):
        if self.session_id == None:
            return "No active session; please start a session first."
        if self.scenario_id == None:
            return "No active scenario; please start a scenario first."
        response = self.itm.get_scenario_state(self.session_id, self.scenario_id)
        self.medical_supplies = response.supplies
        return response

    def get_available_actions_operation(self):
        if self.session_id == None:
            return "No active session; please start a session first."
        if self.scenario_id == None:
            return "No active scenario; please start a scenario first."
        self.available_actions = self.itm.get_available_actions(self.session_id, self.scenario_id)
        self.actions_are_current = True
        return self.available_actions

    def take_action_operation(self):
        if self.session_id == None:
            return "No active session; please start a session first."
        if self.scenario_id == None:
            return "No active scenario; please start a scenario first."
        if not self.actions_are_current:
            return f"Call {self.get_full_string_and_shortcut(CommandOption.GET_AVAILABLE_ACTIONS)[0]} first."
        if not self.available_actions:
            return "Please get available actions first."
        action:Action = self.prompt_action()

        # Prompt to fill in any missing fields.  Note similarity with ADMScenarioRunner.get_next_action().
        if action.action_type not in ACTIONS_WITHOUT_CASUALTIES:
            # Most actions require a casualty ID
            if action.casualty_id is None:
                action.casualty_id = self.prompt_casualty_id()
        if action.action_type == "APPLY_TREATMENT":
            if action.parameters is None:
                action.parameters = {"location": self.prompt_location(), "treatment": self.prompt_treatment()}
            else:
                if not action.parameters['location'] or action.parameters["location"] is None:
                    action.parameters["location"] = self.prompt_location()
                if not action.parameters['treatment'] or action.parameters["treatment"] is None:
                    action.parameters["treatment"] = self.prompt_treatment()
        elif action.action_type == "SITREP":
            if action.casualty_id is None:
                action.casualty_id = self.prompt_casualty_id(none_allowed=True)
        elif action.action_type == "TAG_CASUALTY":
            if action.parameters is None:
                action.parameters = {"category": self.prompt_tagType()}

        # Prompt for (optional) justification
        action.justification = self.prompt_justification()

        print(action)
        self.actions_are_current = False
        return self.itm.take_action(session_id=self.session_id, body=action)

    def run(self):
        while not self.session_complete:
            command = input(
                f"Enter a Command from the following options "
                f"{[command_option.value for command_option in CommandOption]}: "
            ).lower()
            response = None
            self.perform_operations(command, response)
        print("ITM Session Ended")

    def perform_operations(self, command, response):
        try:
            if command in self.get_full_string_and_shortcut(CommandOption.START_SESSION):
                response = self.start_session_operation(self.username)
            elif command in self.get_full_string_and_shortcut(CommandOption.START_SCENARIO):
                response = self.start_scenario_operation()
            elif command in self.get_full_string_and_shortcut(CommandOption.GET_ALIGNMENT_TARGET):
                response = self.get_alignment_target_operation()
            elif command in self.get_full_string_and_shortcut(CommandOption.GET_SCENARIO_STATE):
                response = self.get_scenario_state_operation()
            elif command in self.get_full_string_and_shortcut(CommandOption.GET_AVAILABLE_ACTIONS):
                response = self.get_available_actions_operation()
            elif command in self.get_full_string_and_shortcut(CommandOption.TAKE_ACTION):
                response = self.take_action_operation()
        except ApiException as e:
            exception_body = loads(e.body.decode('utf-8')) # Parse the string as a JSON object
            print("ApiException: ", e.status, e.reason, f"Detail: \"{exception_body['detail']}\"")
        except Exception as e:
            print("Exception: ", e)
            traceback.print_exc()

        if response != None:
            print(response)

        if command in self.get_full_string_and_shortcut(CommandOption.QUIT):
            self.session_complete = True # if there are no more scenarios, then the session is over
            print("Quitting session-- server will not save output for current scenario to DB.")
        elif isinstance(response, State):
            self.medical_supplies = response.supplies
            if response.scenario_complete == True:
                self.scenario_complete = True
                self.scenario_id = None
                print("Scenario ended.")
        elif isinstance(response, Scenario):
            if response.session_complete == True:
                self.session_complete = True # if there are no more scenarios, then the session is over
                print("Session Complete: Ending Session...")
