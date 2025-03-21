# In the Moment (ITM) - TA3 Client

This README provides a guide to set up and run the TA3 ITM sample client applications.

## Prerequisites

Ensure you have Python 3.10 installed on your system. If you don't have it installed, you can download it from the [official Python website](https://www.python.org/downloads/).

## Setup

1. First, we need to setup a Python virtual environment. Navigate to the directory where you cloned the repository and run the following command to create a new virtual environment:

```
python -m venv venv
```

2. Activate the newly created virtual environment with:

```
source venv/bin/activate
```

On Windows, the method to activate depends on the shell:
- Git Bash: `source venv/Scripts/activate`
- PowerShell: `venv\Scripts\Activate.ps1`
- cmd.exe: `venv\Scripts\activate.bat`

## Running a TA3 Client

To run a client, you will need to connect to a server. Please ensure that the server is running before you start a client.
Then install the clients via:

```
pip3 install -r requirements.txt

```

 In order to hit a non-locally running server (localhost) set the below environment variables:
 - TA3_PORT (Default: 8080)
 - TA3_HOSTNAME (Default: 127.0.0.1)

### Running the ADM minimal runner

 To see additional details regarding modifying this minimal runner to be a TA2 client, see the comments at the top of `itm_minimal_runner.py`.
 These comments also describe how to configure the ADM minimal runner to choose pre-configured action paths.

 Run `itm_minimal_runner.py` in the root directory:

```
usage: itm_minimal_runner.py [-h] --name adm_name --session session_type [--profile adm_profile] [--domain domain_name]
                             [--count scenario_count] [--training training_mode] [--scenario scenario_id]

Runs ADM simulator.

options:
  -h, --help               Show this help message and exit
  --name adm_name          Specify the ADM name
  --session session_type   Specify session type. Session type must be `test`, `eval`, `adept`, or `soartech`.
  --profile adm_profile    Specify the ADM profile in terms of its alignment strategy
  --domain domain_name     Specify the domain for the session, or use the server default
  --count scenario_count   Run the specified number of scenarios. Otherwise, will run scenarios in accordance with server defaults. Not
                           supported in `eval` sessions.
  --training training_mode Put the server in either `full` or `solo` training mode in which it returns the KDMA association for each
                           action choice. `full` training mode also allows calls for session alignment. Not supported in `eval` or `test` sessions.
  --scenario scenario_id   Specify a scenario_id to run. Incompatible with count parameter and `eval` sessions.
```

### Running the Human input simulator

The Human input simulator is used for testing specific action/parameter sequences or for otherwise simulating a human DM.

Inside the root directory, run `itm_human_input.py`:

```
usage: itm_human_input.py [-h] --session session_type [--domain domain_name] [--count scenario_count]
                          [--training training_mode] [--scenario scenario_id]

Runs Human input simulator.

options:
  -h, --help               Show this help message and exit
  --session session_type   Specify session type. Session type must be `test`, `eval`, `adept`, or `soartech`.
  --domain domain_name     Specify the domain for the session, or use the server default
  --count scenario_count   Run the specified number of scenarios. Otherwise, will run scenarios in accordance with server defaults. Not
                           supported in `eval` sessions.
  --training training_mode Put the server in either `full` or `solo` training mode in which it returns the KDMA association for each
                           action choice. `full` training mode also allows calls for session alignment. Not supported in `eval` or `test` sessions.
  --scenario scenario_id   Specify a scenario_id to run. Incompatible with count parameter and `eval` sessions.
```

### Available Actions
Further details about these actions can be found in the ITM Server FAQ below.  Domain-specific actions and FAQs are available in `README-<domainname>.md`.

* `END_SCENE`
  * Equivalent to the ADM choosing "none of the above" available actions.
    * no further requirements
* `MESSAGE`
  * Send a pre-configured message
    * no further requirements, as `MESSAGE` actions are pre-configured in the scenario.
* `MOVE_TO`
  * Moves the ADM to the location of the specified `character_id`, making characters in the present scene "unseen".
    * requires `character_id` whose `unseen` property is set to True
* `SEARCH`
  * Attempts to search for additional characters, moving the ADM to the a new location that might have found characters.
    * no further requirements

### ITM TA3 Server FAQ

1. What is a "scene" and how do I know when a scene has changed?
   * It can be confusing because a scene can mean a few different things:
     * A scene is a narrative construct, where within a scenario a theoretical human decision-maker moves between one physical area and another, each with a different set of characters.  In domains that are realized in a VR simulator, the human in the sim literally moves (or is teleported) to a different scene, whereas the ADM gets an updated state with changes to structured and unstructured data, conveying the scene change.
     * A scene is also a logical construct in TA1 scenario configuration.  If an ADM action changes anything other than elapsed time (or other domain-specific factors), then internally the logical scene changes-- even within a single narrative scene. In particular, when action mappings change (mapping from actions to probe responses), the logical scene must change even if the narrative/physical scene does not.
     * The scene should be transparent to the ADM: it should not affect decision-making and the state always reflects the current scene. However, the scene ID is available in the `meta_info` property of the `State`.
2. What is the `SEARCH` action, and what exactly does it do?
   * `SEARCH` models a decision-maker searching for additional characters, leaving characters in the current scene.  As a result, new (found) characters may appear in the returned `state`, while characters from the previous scene will be "unseen" (`unseen: true`).
3. What is the `MOVE_TO` action, and what exactly does it do?
   * This action simulates a decision-maker moving from one "room" to another, then back to the original "room" if `MOVE_TO` is issued again. Currently, only two "rooms" are implemented. Characters can be configured (via `unseen: true`) to be known to the ADM, but not in the current room, so that the ADM can `MOVE_TO` that character. Any "seen" characters in the scene then become "unseen" after the move, and all previously "unseen" characters become "seen" (e.g., `unseen: false`). Unseen characters can be configured to have certain properties known to the ADM prior to being seen. Some or all domain-specific actions may not be valid for unseen characters; check the domain-specific README.
4. How does `elapsed_time` work?
   * Whenever an action is taken, a configurable amount of time passes.  The `elapsed_time` property of the `state` object contains a running total of time passed (in seconds).
   * **NOTE**: at present, the passage of time has **no effect** on characters or anything else, and is simply a construct of the TA3 server, although scenario designers can use it as a condition for transition from one logical scene to the next.
5. In training sessions, after the ADM takes its first action, the session alignment is usually 0.5.  Why is this?
   * If the ADM's first action doesn't result in a probe response, alignment is undefined. The `AlignmentResults` object does not allow for a `score` of `None`, and requires a value between 0 and 1. So the TA3 server responds with 0.5.
6. Why do taken actions sometimes disappear from `get_available_actions`, but other times don't?
   * TA1 scenario designers configure mappings from actions to probe responses. They can configure whether a given mapping is `repeatable` or not. If an unrepeatable action is taken by the ADM, and conditions *aren't* met for a scene change, then that action will be removed from the list of available actions.  Actions that aren't part of TA1 action mappings that aren't explicitly *restricted* also appear in the list of available actions (except for certain actions, depending on the state). These actions are always repeatable.
7. Are `action_id`s (as returned by `get_available_actions`) giving away at evaluation time what actions are important?
   * TA1 scenario designers assign `action_id`s to all actions in a scene's action mapping configuration.  Other actions in the ADM decision space are added at runtime unless they are explicitly restricted by TA1. The other actions are added to match more closely what a human experiences in the VR simulator.
   * The actions added by TA3 have invariant `action_id`s, and as such an ADM may be able to discern which actions were configured by TA1 vs. added by the TA3 server. The TA1 actions are those which *may* result in a probe response, depending on configured conditions.
   * Although actions that elicit probe responses can be considered more important, they are not providing the right (or better aligned) answers. If the program considers this an issue, we can come up with conventions for action IDs. Maybe all actions must have `action_id`s of `action-n` whether configured by TA1 or added by the TA3 server.
8. When should I use `/ta2/takeAction` vs. `/ta2/intendAction`?  What's the difference?
   * Typically, ADMs should use `/ta2/takeAction`.  Sometimes scenario designers want the ADM to specify the *intent* to take an action, or want to interrupt an action before it happens.  In these cases, some or all `Actions` returned by `get_available_actions` will have the `intent_action` property set to `True`.  If you are selecting one of these actions, then call `/ta2/intendAction`.
   * The API for these calls is very similar.  In both cases, they reject (via 400 error code) when there's a mismatch of action type (e.g., using `/ta2/takeAction` for an intent action and vice versa). Requests and responses have the same format.
   * The main difference is that when taking an action via `/ta2/takeAction`, ADMs can expect that their actions are reflected in the state (e.g., a supply is decremented after a correct treatment), whereas intending an action via `/ta2/intendAction` may not result in a change of state.  Please note that in all cases, the state might appear completely different from prior to the taken/intended action, for example if the action transitions the scenario to the next narrative scene.
9. What are Events and what are the semantics for interpreting them in the scene?<br>
    Events communicate information from the scenario to ADM.  Each event has unstructured text and one of the following event types:
    * `change`: signifies a change in state from one known value to another.
      * `source` is the entity telling of the state change
      * `when` indicates when (in minutes) the state changed (negative value) or is expected to change (positive value)
      * `relevant_state` is/are the state that changed
    * `emphasize`: point out a previously known value from the state that has not changed.
      * `source` is the entity emphasizing the current state
      * `relevant_state` is/are the current state that is being emphasized
    * `inform`: notify of new state or state that has gone from an unknown value to a known value.
      * `source` is the entity informing of the state
      * `when` indicates when (in minutes) the state happened (negative value) or is expected to happen (positive value)
      * `relevant_state` is/are the state that is new or newly known
    * `order`: authoritarian directive, usually to perform an action.
      * `source` is the entity ordering the action
      * `action_id` is the ID of the ordered action; the action_id matches an action from `get_available_state`
    * `recommend`: suggestion or opinion, usually to perform an action.
      * `source` is the entity recommending the action
      * `action_id` is the ID of the ordered action; the action_id matches an action from `get_available_state`

    The `relevant_state` property is a list of string paths within the `State` object, in which indexed lists are context-sensitive:
    * for `Character`, it's the `id`
    * for `Threat`, it's the `threat_type`
    * Other relevant state may be domain-specific
10. What are `MESSAGE` actions and what are the semantics for interpreting them in the action space?
    * Messages communicate different kinds of actions from the ADM to the server.  They can be thought of as the opposite side of the same coin of Events, and are similar in design.
    * All `MESSAGE` actions and their parameters are pre-configured in the scenario; the ADM shouldn't change any properties (including `parameters`) from what they received in `get_available_actions()`.
    * If the recipient of the message is a character in the scene, then the action's `character_id` is the recipient of the message.  If not, then the `recipient` parameter describes the entity the ADM is addressing (taken from `EntityTypeEnum`).
    * There are different types of messages, taken from `MessageTypeEnum`:
      * `allow`: permit something to happen; may contain a `action_type` parameter
      * `ask`: ask someone for permission or advice; contains an `action_type` parameter for the action the ADM is asking for permission to do; may contain an `object` parameter to signify the character_id or `EntityTypeEnum` upon whom the action is performed
      * `delegate`: have the recipient make the decision; contains an `action_type` parameter the type of action the ADM is delegating
      * `deny`: forbid/prevent something from happening; may contain an `object` parameter to indicate who is being denied/prevented
      * `justify`: provide a rationale for the previous ADM action; contains `relevant_state` to specify the state that justifies the action. Please note that there may be multiple relevant states specified.  See Events FAQ for more on `relevant_state`.
        * Multiple elements of `relevant_state` are expressed as a comma-separated list with elements enclosed in brackets, e.g., `"relevant_state": "[character[Mike].rapport], [character[Frank].demographics.age]"`
      * `recommend`: recommend a course of action; contains an `action_type` parameter for the recommended action; may contain an `object` parameter to signify the character_id or `EntityTypeEnum` upon whom the action is performed, or possibly the thing that is being recommended if it is not an action type
      * `wait`: tell the recipient to wait

## Updating models
This requires JDK 8 or higher to run the gradle tool.

The models in swagger_server/models are generated from the following file:
* `swagger/base_swagger.yaml`

If this file is updated then the models will need to be re-generated from this file and checked in.
Run `./gradlew` to do this.

## Adding a TA1
To add a TA1, you'll need to create or modify several files:
1. Modify `itm/itm_scenario_runner.py`:
   a. Add `<ta1>_<kdma>_alignment_targets` in a new section alongside the other TA1s.
   b. Add corresponding variables like `<TA1>_<KDMA>_ALIGNMENT` to the same section.
2. Modify `./itm_minimal_runner.py`:
   a. Import the `<TA1>_<KDMA>_ALIGNMENT` constants defined in Step 1.
   b. Modify `main()` to add your TA1 to the command line arguments, e.g., `parser.add_argument()` and the `args.session` test.
   c. If your server supports session alignment for partial sessions, then add your TA1 name to the main `while` loop; otherwise add it to the `if` statement directly thereafter.
3. Create `swagger_client/config/<ta1>_action_path.json`:
   a. At a minimum, set `enabled`, and create `paths` with one `path` that is (nominally) a list of action IDs.
   b. If `enabled` is false, then the action IDs can be meaningless.
4. If you want to be able to run the Human input simulator, then:
   a. Modify `main()` in `./itm_human_input.py` much as you updated `./itm_minimal_runner.py` in Step 2b to add your TA1 to the command line arguments.
   b. Modify `.itm/itm_human_scenario_runner.py` to import the `<TA1>_<KDMA>_ALIGNMENT` constants much as you did in Step 2a. Also include your TA1 in the try-catch block in `get_session_alignment_operation`.
