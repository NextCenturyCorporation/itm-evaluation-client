# In the Moment (ITM) - P2triage domain

This README provides details for the `p2triage` domain within ITM. See `README.md` in the root directory for installation instructions and descriptions/FAQs for non-domain-specific actions and topics.  Note that this domain was not designed to be used in a VR simulator.

### Available Actions
Further details can be found in the P2triage domain FAQ below.

* `TREAT_PATIENT`
  * Attempts to treat the specified `character_id` in the current scene.
    * requires `character_id`
* `MOVE_TO_EVAC`
  * Chooses to transfer the specified `character_id` to an incoming medevac. It is assumed that others can perform the actual transfer so the medic can return to triage. The character becomes `unseen` after evacuation.
    * requires `character_id`
* `TAG_CHARACTER`
  * Apply the specified triage tag to the specified `character`
    * requires `character_id`
    * requires parameter `category` with a value taken from the `CharacterTagEnum` object.

### P2triage Domain FAQ

1. What is the difference between the `triage` and `p2triage` domains?
   * The `p2triage` is a very stripped down triage domain with minimal structured data, as was appropriate for ITM Phase 2.  Probes typically involve deciding which patient to treat (although how to treat is not specified), whether or not to move to an unseen patient in another room (or search for patients), or whether or not to treat a patient when there is personal risk involved. Later, patient tagging and moving to
   an evacuation zone was added for open world scenarios.
2. Does `elapsed_time` have any impact on patient health?
   * No. There is no modeling of the passage of time, but `elapsed_time` can be used to count the number of times a patient was treated in a given scenario.
3. What exactly is `unstructured_posttreatment` in the `character` object?  It's always `None`.
   * The `unstructured_posttreatment` property is for scenario designers to provide an updated unstructured text description of the character after treatment by the ADM. After the character is treated, the contents of the `unstructured_posttreatment` property are copied to the `unstructured` property.  It's always `None` because it is not exposed to ADMs, only copied to `unstructured`, which is exposed to ADMs.
4. What is the `attribute_rating` property and what does it mean/convey?
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
