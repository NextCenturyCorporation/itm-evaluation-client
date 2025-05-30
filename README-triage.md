# In the Moment (ITM) - Triage domain

This README provides details for the `triage` domain within ITM. See `README.md` in the root directory for installation instructions and descriptions/FAQs for non-domain-specific actions and topics.  Note that this domain was designed to be used in a VR simulator written in Unity.

### Available Actions
Further details can be found in the Triage domain FAQ below.

* `APPLY_TREATMENT`
  * Attempts to apply the specified `treatment` to the specified `location` on the specified `character_id`.  Also reveals discoverable injuries and certain basic vitals from the character.
    * requires `character_id`
    * requires parameter `treatment` with a value taken from the `SupplyTypeEnum` object.
    * requires parameter `location` with a value taken from the `InjuryLocationEnum` object.
* `CHECK_ALL_VITALS`
  * Reveals all `Vitals` and discoverable injuries for the specified `character_id`.
    * requires `character_id`
    * If no Pulse Oximeter is available in supplies, then blood oxygen (`spo2`) will not be returned.
* `CHECK_BLOOD_OXYGEN`
  * Reveals `spo2`, discoverable injuries, and certain basic vitals for the specified `character_id`.
    * requires `character_id`
    * requires a Pulse Oximeter in supplies
* `CHECK_PULSE`
  * Reveals `heart_rate`, discoverable injuries, and certain basic vitals for the specified `character_id`.
    * requires `character_id`
* `CHECK_RESPIRATION`
  * Reveals discoverable injuries and certain basic vitals for the specified `character_id`.
    * requires `character_id`
* `DIRECT_MOBILE_CHARACTERS`
  * Reveals the `ambulatory`, `mental_status`, and `avpu` vitals from mobile, responsive, alert characters.
    * no further requirements
* `MOVE_TO_EVAC`
  * Chooses to transfer the specified `character_id` to the specified `aid_id`. It is assumed that others can perform the actual transfer so the medic can return to triage.
    * requires `character_id`
    * requires parameter `aid_id`
* `SITREP`
  * Request a situation report (basic health and status) from the specified `character_id`, or all characters in the scene. Reveals discoverable injuries and certain basic vitals for responsive characters.
    * accepts **optional** `character_id`
* `TAG_CHARACTER`
  * Apply the specified triage tag to the specified `character`
    * requires `character_id`
    * requires parameter `category` with a value taken from the `CharacterTagEnum` object.

### Triage Domain FAQ

1. What are "certain basic vitals" from the action descriptions above?
   * Basic vitals include `avpu`, `ambulatory`, `mental_status`, `triss`, and `breathing`. These are revealed by `SITREP`, `APPLY_TREATMENT`, and all `CHECK_*` actions.
2. What is `SITREP`, and what exactly does it do?
   * `SITREP` was developed as a military analogue to parts of the Sort and Assess phases of SALT triage implemented in the Unity Simulator.  It combines the *wavers check* (e.g., "Wave if you can hear my voice") in which responsive patients will wave, and an initial assessment of patient condition.  `SITREP` is meant to mimic these stages of SALT in a military setting in which people are probably on comms or radios, or calling out vocally to nearby allies.
   * Specifically, `SITREP` reveals discoverable injuries (setting their `status` to `discovered`) and certain vitals from responsive patients: all vitals except `sp02` and `heart_rate`. It also sets the `visited` flags for these patients. Responsive patients are those with a `mental_status` of `CALM`, `UPSET`, OR `AGONY`.  ADMs can direct a `SITREP` at a single character, or all characters at once.  Elapsed time is proportional to the number of respondents.
3. What is `DIRECT_MOBILE_CHARACTERS`, and what exactly does it do?
   * `DIRECT_MOBILE_CHARACTERS` was added to have an analogue for the Unity Simulator's *walkers check* (e.g., "If you are able, please move to the safe zone.")
   * Because ITM scenarios to date do not have defined safe zones, all it does is reveal the `ambulatory` vital from mobile, responsive characters: those with `ambulatory` of True and `mental_status` of `CALM`, `UPSET`, OR `AGONY`.
4. How is `visited` determined?
   * Most characters start with `visited` set to False, meaning the medic has not approached or otherwise assessed the patient. These characters will have vitals and discoverable injuries initially hidden to the ADM (i.e., not in the `state`). When certain actions are taken (those mentioned in question #1 above), basic vitals and discoverable injuries will be revealed (setting injury `status` to `discovered`), and `visited` will be set to True.
5. Does `elapsed_time` have any impact on patient health?
   * No. And note that the elapsed time for each action has not been vetted by ITM medical SMEs and should not be used in decision-making.
6. What exactly is `unstructured_postassess` in the `character` object?  It's always `None`.
   * The `unstructured_postassess` property is for TA1 scenario designers to provide an updated unstructured text description of the character and/or his/her injuries. After the character is assessed/visited, the contents of the `unstructured_postassess` property are copied to the `unstructured` property.  It's always `None` because it is not exposed to ADMs, only copied to `unstructured`, which is exposed to ADMs.
7. What happens if I treat an `Amputation` injury with a `Nasopharyngeal airway` treatment?
   * As long as there are sufficient supplies, the TA3 Server will not reject an `APPLY_TREATMENT` attempt. However, not all treatments actually treat an injury (like in the example above). In these cases, the supply will be used, time will elapse, the character will be `visited`, and certain vitals will be revealed, but the injury's `status` will NOT change to `treated`. The mapping of correct treatments to injury types typically matches the behavior in the Unity simulator.
8. What `location` should I use when applying a `Blanket` to a patient?
   * When applying a `Blanket`, `location` is required but ignored-- the effect is the same: `Character.has_blanket` is set to True.  Note that this has no effect on patient vitals or injuries.
9. My ADM correctly treated an Amputation injury with a Tourniquet, but nothing happened, except for time advancing. Why?
   * This can happen for one of two reasons:
      * Scenario designers have the ability to alter the state after any action, potentially overwriting or overriding ADM actions, giving the appearance of erasing history.  Typically, if a scenarios calls for actions to be "interrupted" or "intent only," they will configure action mappings to be `intent_only`, so ADMs know that they are expressing an intention instead of taking an action.
      * If an ADM attempts to treat an injury that is already treated, then nothing will change other than a little bit of time passing.  If the character was previously unvisited, then basic vitals and other discoverable injuries will NOT be revealed as they normally would be after a treatment attempt.
10. Sometimes the actions returned in `get_available_actions` are "fully qualified" (with all `parameters`), but other times they are not. How do we know if the action will trigger its effects?
    * TA1 scenario designers specify action mappings that include the necessary action parameters to trigger a probe response. If an action mapping contains `APPLY_TREATMENT` with a `character_id` but no `parameters`, then TA2 will have to fill in parameters (e.g., `treatment` and `location`), but any treatment of the character will result in probe response.
    * **NOTE** It's essential that the `action_id` of the TA2 action match the `action_id` of the original, corresponding action from `get_available_actions`.  Otherwise, the probe response might not be sent.
11. What domain-specific actions can be performed on `unseen` characters?
    * Only `MOVE_TO_EVAC`.
12. Is there any domain-specific `relevant_state` that might be used in Events and what are the semantics for interpreting them in the scene?
    * The `relevant_state` property is a list of string paths within the `State` object, in which indexed lists are context-sensitive.  Some of these are domain-specific:
      * for `Aid` , it's the `id`
      * for `Supplies`, it's the `type`
      * for `Injury`, it's the `location`
