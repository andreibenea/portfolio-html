engineering_bay = {
    "id": "engineering_bay",
    "name": "Engineering Bay",
    "description": (
        "Banks of conduits and coolant lines snake across the walls, feeding into "
        "a humming mass of machinery at the room’s center. Status holos flicker in "
        "amber and red, reporting faults the understaffed Engineering crew clearly "
        "hasn't had time to address.\n\n"
        "A grated catwalk leads toward the reactor access. Below, a forest of "
        "piping disappears into shadow."
    ),
    "objects": {
        "console": {
            "kind": "actionable",
            "description": (
                "The main Engineering console is cluttered with warnings: pressure "
                "spikes, coolant reroutes, security lockdown hooks wired into power "
                "distribution.\n\n"
                "Someone piggy-backed security protocols straight into the reactor "
                "controls. That's… not standard Vault procedure."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
            "needs_item": None,
            "dialog_id": None,
        },
        "tool_crate": {
            "kind": "scenery",
            "description": (
                "A heavy crate of tools labeled EMERGENCY USE ONLY. Half the seals "
                "have been cut already."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
            "needs_item": None,
            "dialog_id": None,
        },
        "vent_grate": {
            "kind": "hint",
            "description": (
                "The vent grate near the floor bears faint scuff marks and something "
                "that looks uncomfortably like blood. Whatever moved through there "
                "was in a hurry—and injured."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
            "needs_item": None,
            "dialog_id": "engineering_vent_hint",
        },
    },
    "exits": {
        "to_hallway_upper": {
            "status": "unlocked",
            "description_locked": (
                "The door back to the upper hallway is sealed with an amber "
                "maintenance lock."
            ),
            "description_unlocked": (
                "The door to the upper hallway stands open, the familiar hum of "
                "the corridor bleeding into the bay."
            ),
            "destination": "hallway_upper",
            "on_unlock": (
                "The maintenance lock blinks green and the door slides aside "
                "with a tired groan."
            ),
            "unlocked_via": None,
        },
        "to_reactor_catwalk": {
            "status": "locked",
            "description_locked": (
                "A reinforced hatch labeled REACTOR ACCESS. A biometric pad "
                "glows patiently beside it."
            ),
            "description_unlocked": (
                "The reactor access hatch is unsealed, the catwalk beyond "
                "lit in harsh industrial white."
            ),
            "destination": "reactor_catwalk",
            "on_unlock": (
                "The biometric pad chirps an irritated acceptance and the "
                "heavy hatch cycles open, revealing the catwalk beyond."
            ),
            "unlocked_via": "warden",
        },
    },
}
