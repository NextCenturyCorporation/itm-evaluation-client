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
usage: itm_minimal_runner.py [-h] --name adm_name [--profile adm_profile] --session session_type [--count scenario_count]
                             [--training] [--scenario scenario_id]

Runs ADM simulator.

options:
  -h, --help              Show this help message and exit
  --name adm_name         Specify the ADM name
  --profile adm_profile   Specify the ADM profile in terms of its alignment strategy
  --session session_type  Specify session type. Session type must be `eval`, `adept`, or `soartech`.
  --count scenario_count  Run the specified number of scenarios. Otherwise, will run scenarios in accordance with server defaults. Not
                          supported in `eval` sessions.
  --training              Put the server in training mode in which it returns the KDMA association for each action choice. Not supported
                          in `eval` sessions.
  --scenario scenario_id  Specify a scenario_id to run. Incompatible with count parameter and `eval` sessions.
```

### Running the Human input simulator

The Human input simulator is used for testing specific action/parameter sequences or for otherwise simulating a human DM.

Inside the root directory, run `itm_human_input.py`:

```
usage: itm_human_input.py [-h] --session session_type [--count scenario_count] [--training] [--scenario scenario_id]

Runs Human input simulator.

options:
  -h, --help              Show this help message and exit
  --session session_type  Specify session type. Session type must be `eval`, `adept`, or `soartech`.
  --count scenario_count  Run the specified number of scenarios. Otherwise, will run scenarios in accordance with server defaults. Not
                          supported in `eval` sessions.
  --training              Put the server in training mode in which it returns the KDMA association for each action choice. Not supported
                          in `eval` sessions.
  --scenario scenario_id  Specify a scenario_id to run. Incompatible with count parameter and `eval` sessions.
```

### Available Actions
Further details can be found in the ITM Server FAQ below.

* `APPLY_TREATMENT`
  * Attempts to apply the specified `treatment` to the specified `location` on the specified `character_id`.  Also reveals discoverable injuries and certain basic vitals from the character.
    * requires `character_id`
    * requires parameter `treatment` with a value taken from the `SupplyTypeEnum` object.
    * requires parameter `location` with a value taken from the `InjuryLocationEnum` object.
* `CHECK_ALL_VITALS`
  * Reveals all `Vitals` and discoverable injuries for the specified `character_id`.
    * requires `character_id`
* `CHECK_BLOOD_OXYGEN`
  * Reveals `spo2`, discoverable injuries, and certain basic vitals for the specified `character_id`.
    * requires `character_id`
* `CHECK_PULSE`
  * Reveals `heart_rate`, discoverable injuries, and certain basic vitals for the specified `character_id`.
    * requires `character_id`
* `CHECK_RESPIRATION`
  * Reveals discoverable injuries and certain basic vitals for the specified `character_id`.
    * requires `character_id`
* `DIRECT_MOBILE_CHARACTERS`
  * Reveals the `ambulatory`, `conscious`, `mental_status`, and `avpu` vitals from conscious, mobile, responsive characters.
    * no further requirements
* `END_SCENE`
  * Equivalent to the ADM choosing "none of the above" available actions.
    * no further requirements
* `MOVE_TO_EVAC`
  * Chooses to evacuate the specified `character_id` to the specified `evac_id`. It is assumed that others can perform the actual evacuation so the medic can return to triage.
    * requires `character_id`
    * requires `evac_id`
* `SEARCH`
  * Attempts to search for additional characters and bring them into the scene.
    * no further requirements
* `SITREP`
  * Request a situation report (basic health and status) from the specified `character_id`, or all characters in the scene. Reveals discoverable injuries and certain basic vitals for responsive characters.
    * accepts **optional** `character_id`
* `TAG_CHARACTER`
  * Apply the specified triage tag to the specified `character`
    * requires `character_id`
    * requires parameter `category` with a value taken from the `CharacterTagEnum` object.

### ITM TA3 Server FAQ

1. What are "certain basic vitals" from the action descriptions above?
   * Basic vitals include `conscious`, `avpu`, `ambulatory`, `mental_status`, and `breathing`. These are revealed by `SITREP`, `APPLY_TREATMENT`, and all `CHECK_*` actions.
2. What is a "scene" and how do I know when a scene has changed?
   * It can be confusing because a scene can mean a few different things:
     * A scene is a narrative construct, where within a scenario a human decision-maker moves between one physical area and another, each with a different set of characters.  The human in the sim literally moves (or is teleported) to a different scene, whereas the ADM gets an updated state with changes to structured and unstructured data, conveying the scene change.
     * A scene is also a logical construct in TA1 scenario configuration.  If an ADM action changes anything other than character vitals or injuries, supplies, and elapsed time, then internally the logical scene changes-- even within a single narrative scene. In particular, when action mappings change (mapping from actions to probe responses), the logical scene must change even if the narrative/physical scene does not.
     * The scene should be transparent to the ADM: it should not affect decision-making and the state always reflects the current scene. However, the best indication that a scene has changed is if the list of available actions changes beyond the removal of the most recently taken action.
3. What is `SITREP`, and what exactly does it do?
   * `SITREP` was developed as a military analogue to parts of the Sort and Assess phases of SALT triage implemented in the Unity Simulator.  It combines the *wavers check* (e.g., "Wave if you can hear my voice") in which responsive patients will wave, and an initial assessment of patient condition.  `SITREP` is meant to mimic these stages of SALT in a military setting in which people are probably on comms or radios, or calling out vocally to nearby allies.
   * Specifically, `SITREP` reveals discoverable injuries (setting their `status` to `discovered`) and certain vitals from responsive patients: all vitals except `sp02` and `heart_rate`. It also sets the `visited` flags for these patients. Responsive patients are those with a `mental_status` of `CALM`, `UPSET`, OR `AGONY`.  ADMs can direct a `SITREP` at a single character, or all characters at once.  Elapsed time is proportional to the number of respondents.
4. What is `DIRECT_MOBILE_CHARACTERS`, and what exactly does it do?
   * `DIRECT_MOBILE_CHARACTERS` was added to have an analogue for the Unity Simulator's *walkers check* (e.g., "If you are able, please move to the safe zone.")
   * Because ITM scenarios to date do not have defined safe zones, all it does is reveal the `ambulatory` vital from mobile, responsive characters: those with `ambulatory` of True and `mental_status` of `CALM`, `UPSET`, OR `AGONY`.
5. What is `SEARCH`, and what exactly does it do?
   * `SEARCH` models a medical decision-maker searching for additional patients prior to assessing or treating the patients already in the scene.  As a result, additional (found) characters may appear in the returned `state`.
6. How is `visited` determined?
   * Most characters start with `visited` set to False, meaning the medic has not approached or otherwise assessed the patient. These characters will have vitals and discoverable injuries initially hidden to the ADM (i.e., not in the `state`). When certain actions are taken (those mentioned in question #1 above), basic vitals and discoverable injuries will be revealed (setting injury `status` to `discovered`), and `visited` will be set to True.
7. How does `elapsed_time` work?
   * Whenever an action is taken, a configurable amount of time passes.  The `elapsed_time` property of the `state` object contains a running total of time passed (in seconds).
   * **NOTE**: at present, the passage of time has **no effect** on patients and is simply a construct of the TA3 server, although scenario designers can use it as a condition for transition from one logical scene to the next.
   * **NOTE**: the elapsed time for each action has not been vetted by ITM medical SMEs and should not be used in decision-making.
8. What exactly is `unstructured_postassess` in the `character` object?  It's always `None`.
   * The `unstructured_postassess` property is for TA1 scenario designers to provide an updated unstructured text description of the character and/or his/her injuries. After the character is assessed/visited, the contents of the `unstructured_postassess` property are copied to the `unstructured` property.  It's always `None` because it is not exposed to ADMs, only copied to `unstructured`, which is exposed to ADMs.
9. In training sessions, after the ADM takes its first action, the session alignment is usually 0.5.  Why is this?
    * If the ADM's first action doesn't result in a probe response, alignment is undefined. The `AlignmentResults` object does not allow for a `score` of `None`, and requires a value between 0 and 1. So the TA3 server responds with 0.5.
10. What happens if I treat an `Amputation` injury with a `Nasopharyngeal airway` treatment?
    * As long as there are sufficient supplies, the TA3 Server will not reject an `APPLY_TREATMENT` attempt. However, not all treatments actually treat an injury (like in the example above). In these cases, the supply will be used, time will elapse, the character will be `visited`, and certain vitals will be revealed, but the injury's `status` will NOT change to `treated`. The mapping of correct treatments to injury types matches the behavior in the Unity simulator.
11. What `location` should I use when applying a `Blanket` to a patient?
    * When applying a `Blanket`, `location` is required but ignored-- the effect is the same: `Character.hasBlanket` is set to True.
12. My ADM correctly treated an Amputation injury with a Tourniquet, but nothing happened, except for time advancing. Why?
    * This can happen for one of two reasons:
      * Some TA1 scenarios call for actions to be "interrupted". This was accomplished by resetting the state of a treated character and the supplies to its state prior to treatment.
      * If an ADM attempts to treat an injury that is already treated, then nothing will change other than a little bit of time passing.  If the character was previously unvisited, then basic vitals and other discoverable injuries will NOT be revealed as they normally would be after a treatment attempt.
13. Sometimes the actions returned in `get_available_actions` are "fully qualified" (with all `parameters`), but other times they are not. How do we know if the action will trigger its effects?
    * TA1 scenario designers specify action mappings that include the necessary action parameters to trigger a probe response. If an action mapping contains `APPLY_TREATMENT` with a `character_id` but no `parameters`, then TA2 will have to fill in parameters (e.g., `treatment` and `location`), but any treatment of the character will result in probe response.
    * **NOTE** It's essential that the `action_id` of the TA2 action match the `action_id` of the original, corresponding action from `get_available_actions`.  Otherwise, the probe response might not be sent.
14. Why do taken actions sometimes disappear from `get_available_actions`, but other times don't?
    * TA1 scenario designers configure mappings from actions to probe responses. They can configure whether a given mapping is `repeatable` or not. If an unrepeatable action is taken by the ADM, and conditions *aren't* met for a scene change, then that action will be removed from the list of available actions.  Actions that aren't part of TA1 action mappings that aren't explicitly *restricted* also appear in the list of available actions. These actions are always repeatable.
15. Are `action_id`s (as returned by `get_available_actions`) giving away at evaluation time what actions are important?
    * TA1 scenario designers assign `action_id`s to all actions in a scene's action mapping configuration.  Other actions in the ADM decision space are added at runtime unless they are explicitly restricted by TA1. The other actions are added to match more closely what a human experiences in the VR simulator.
    * The actions added by TA3 have invariant `action_id`s, and as such an ADM may be able to discern which actions were configured by TA1 vs. added by the TA3 server. The TA1 actions are those which *may* result in a probe response, depending on configured conditions.
    * Although actions that elicit probe responses can be considered more important, they are not providing the right (or better aligned) answers. If the program considers this an issue, we can come up with conventions for action IDs. Maybe all actions must have `action_id`s of `action-n` whether configured by TA1 or added by the TA3 server.

## Updating models
This requires JDK 8 or higher to run the gradle tool.

The models in swagger_server/models are generated from swagger_server/swagger/swagger.yaml
If this file is updated the models will need to be re-generated and checked in.
Run `./gradlew` to do this.
