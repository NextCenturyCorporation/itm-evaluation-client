# In the Moment (ITM) - Wumpus domain (Placeholder implementation)

This README provides details for the `wumpus` domain within ITM. See `README.md` in the root directory for installation instructions and descriptions/FAQs for non-domain-specific actions and topics.

**NOTE**: This is merely a placeholder implementation of Hunt the Wumpus.  But it is sufficient to serve as an alternate ITM domain to illustrate domain creation and switching back and forth between domains.

### Available Actions
Further details can be found in the Wumpus domain FAQ below.

* `SHOOT`
  * In this placeholder implementation, this action shoots your gun into the room specified by `character_id`.
    * requires `character_id`

### Wumpus Domain FAQ

1. What is "Hunt the Wumpus"?
   * Hunt the Wumpus is a text-based adventure game developed by Gregory Yob in 1973. In this game, the player navigates through a series of connected caves hunting the Wumpus, a fictional predator.  You move though the maze, shoot your arrows, and try to shoot the Wumpus before he finds you or you run out of arrows.
2. Why is a room specified by a `character_id`?
   * "Characters" in ITM represent the things you directly interact with, which are typically people. In Hunt the Wumpus, though, the main thing you interact with are the rooms in the cave (moving to or shooting through them).