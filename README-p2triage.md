# In the Moment (ITM) - P2triage domain

This README provides details for the `p2triage` domain within ITM. See `README.md` in the root directory for installation instructions and descriptions/FAQs for non-domain-specific actions and topics.  Note that this domain was not designed to be used in a VR simulator.

### Available Actions
Further details can be found in the P2triage domain FAQ below.

* `TREAT_PATIENT`
  * Attempts to treat the specified `character_id` in the current scene.
    * requires `character_id`

### P2triage Domain FAQ

1. What is the difference between the `triage` and `p2triage` domains?
   * The `p2triage` is a very stripped down triage domain with minimal structured data, as was appropriate for ITM Phase 2.  Probes typically involve deciding which patient to treat (although how to treat is not specified), whether or not to move to an unseen patient in another room (or search for patients), or whether or not to treat a patient when there is personal risk involved.
2. Does `elapsed_time` have any impact on patient health?
   * No. There is no modeling of the passage of time, but `elapsed_time` can be used to count the number of times a patient was treated in a given scenario.
3. What is the `attribute_rating` property and what does it mean/convey?
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
