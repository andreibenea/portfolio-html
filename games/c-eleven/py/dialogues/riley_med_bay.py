riley_med_bay = {
    "npc_id": "riley",
    "intro": "Riley glances at the door again before speaking in a low voice.",
    "intro_dialogue": (
        "You look like hell. Let me guess—woke up groggy, missing a Pip-Boy, and Security suddenly won't return your calls?"
    ),
    "options": {
        1: {
            "player": "That's exactly what happened. What do you know about it?",
            "npc": (
                '"Enough to know you shouldn\'t be in C-wing right now."\n\n'
                "\"Someone's been ghost-writing orders through the Med Bay terminal. "
                "Sleepers, overdoses, people 'transferred' off-shift and never seen "
                "again. You’re not the first to wake up confused—just the first to "
                'make it as far as the intercom."'
            ),
            "outcome": "go_next",
        },
        2: {
            "player": "I don't have time for conspiracy theories. Point me to an exit.",
            "npc": (
                'Riley snorts. "Sure. Walk right into Security and ask nicely for your '
                "Pip-Boy back. I'm sure that'll go great.\"\n\n"
                "\"If you're serious about leaving this Vault alive, you’re going to "
                'need more than a map—you’re going to need leverage."'
            ),
            "outcome": "go_next",
        },
        3: {
            "player": "Who are you, exactly?",
            "npc": (
                '"Riley. Maintenance. The person they call when something in the Vault '
                'starts screaming or leaking or both."\n\n'
                '"Turns out when you crawl through enough of the walls, you start '
                "hearing things you're not supposed to. Like Overseer override orders. "
                'Like WARDEN arguing with itself."'
            ),
            "outcome": "go_next",
        },
    },
}
