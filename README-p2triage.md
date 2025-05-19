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
