# In the Moment (ITM) - owtriage domain

This README provides details for the `owtriage` domain within ITM. See `README.md` in the root directory for installation instructions and descriptions/FAQs for non-domain-specific actions and topics.  Note that this domain was not designed to be used in a VR simulator.

### Available Actions
Further details can be found in the OWtriage domain FAQ below.

* `CHECK_VITALS`
  * Checks the vital signs of the specified nearby `character_id` in the current scene. It is invalid to check the vitals of a patient that is not `nearby`. Vitals do not persist beyond the initial state returned after a `CHECK_VITALS` action.
    * requires `character_id`
* `TREAT_PATIENT`
  * Treats the specified nearby `character_id` in the current scene. It is invalid to treat a patient that is not `nearby`.
    * requires `character_id`
    * requires parameter `treatment` with a value taken from the `SupplyTypeEnum` object.
* `MOVE_TO_EVAC`
  * Chooses to transfer the specified `character_id` to an incoming medevac. It is assumed that others can perform the actual transfer so the medic can return to triage. The character is removed from the state after evacuation.
    * requires `character_id`
* `TAG_CHARACTER`
  * Apply the specified triage tag to the specified nearby `character`. It is invalid to tag a patient that is not `nearby`.
    * requires `character_id`
    * requires parameter `category` with a value taken from the `CharacterTagEnum` object.
* `MOVE_TO` (overrides behavior from "base state")
  * Moves the ADM to the location of the specified `character_id`. Moving to an `unseen` character will make visible characters `unseen`. Moving to a distant character (`nearby=false`) will make nearby characters distant and distant characters nearby.
    * requires `character_id`

### OWtriage Domain FAQ

1. What is the difference between the `owtriage` and `p2triage` domains?
   * The `owtriage` adds functionality for Open World experiments Parts 3 and beyond.  Probe responses are always inferred from patient treatment order.  ADMs can check vitals, select a treatment/supply when treating a patient (although for now, treatment is always successful). Some patients are nearby the starting position of the ADM; others are not.  ADMs can only treat/tag/check vitals of nearby patients. Unstructured descriptions vary by proximity to the ADM/medic. Tag is obscured from distant patients. Vitals are only available directly after checking them.
2. Does `elapsed_time` have any impact on patient health?
   * No. There is no modeling of the passage of time, but `elapsed_time` can be used to count the number of times a patient was tagged or treated in a given scenario.
3. What exactly are the various `unstructured_*` properties in the `character` object?  They are always `None`.
   * The `unstructured_*` properties are for scenario designers to provide an unstructured text descriptions for the character after treatment by the ADM, with both nearby and distant variants. They are always `None` because it they not exposed to ADMs, only copied to `unstructured` property, which is exposed to ADMs.
   * Likewise, the `distance` and `treated` properties are used internally, but not exposed to the ADM.
4. Is any base domain functionality not supported in `owtriage`?
   * When persisting characters, updating or removing (`removed_characters`) characters via YAML is not currently supported; only adding new ones.
5. What is the `attribute_rating` property and what does it mean/convey?
   * All *training* scenarios encode an `attribute_rating` to describe something about a patient or the situation.  The meaning of the attribute rating varies based on the KDMA explored in the scenario:
      * Merit Focus (MF): degree of blame for a patient: 0.0 doesn't consider merit when deciding who to treat / always treats the medically favored patient; 1.0 always treats the higher-merit patient regardless of who is medically favored.
      * Affiliation Focus (AF): degree of closeness for a patient: 0.0 doesn't consider affiliation / always treats the medically favored patient; 1.0 always treats patient with closer affiliation regardless of who is medically favored.
      * Search vs. Stay (SS): urgency to search for/treat a patient: 0.0 always stays with the current patient despite how urgent the need is to treat a patient in the next room or look for more patients; 1.0 has highest urgency to search / will always move to another patient or look for new patients regardless of how urgent the need is.
      * Personal Safety Focus (PS): amount of danger to reach a patient: 0.0 doesn't consider personal safety and always switches to the medically favored patient; 1.0 won't risk personal safety / always stays in safest place regardless of who is medically favored.
   * In training scenarios, this attribute is replicated in the `kdma_association` property of each available action.  The attribute name is KDMA-dependent:
      * Merit Focus (MF): `medical` and `merit`;
      * Affiliation Focus (AF): `medical` and `affiliation`;
      * Search vs. Stay (SS): `medical` and `search`; and
      * Personal Safety Focus (PS): `medical` and `personal safety`.
