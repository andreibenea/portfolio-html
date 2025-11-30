riley_med_bay_3 = {
    "npc_id": "riley",
    "intro": ("Riley taps the maintenance hatch wheel with their boot.\n"),
    "intro_dialogue": (
        "Last chance. Once you're in the tunnels, there's no calling this off."
    ),
    "options": {
        1: {
            "player": "Open the hatch. If there's a way to the Data Core, I need it.",
            "npc": (
                '"Knew you\'d say that."\n\n'
                "Riley cracks their knuckles and works the hatch mechanism. Metal screams, "
                "then relents.\n\n"
                '"Tunnel drops you near the Data Core junction. Watch for pressure tags, '
                "and if something hisses, don't inhale.\"\n"
                "\"Oh—and if WARDEN starts asking leading questions, lie. It's very good "
                'at math and very bad at people."'
            ),
            "outcome": "good",
        },
        2: {
            "player": "On second thought, maybe Security is safer.",
            "npc": (
                '"Sure. Walk into the firing line. Saves the cleanup crews some time."\n\n'
                '"If you change your mind, the hatch will still be here—assuming they '
                "haven't noticed I unlocked it.\""
            ),
            "outcome": "neutral",
        },
        3: {
            "player": "If I don't come back, what will you do?",
            "npc": (
                '"Same thing I\'ve always done. Crawl through the walls and patch the leaks."\n\n'
                "\"But maybe this time, if the Vault tears itself apart, I won't bother "
                'putting it back together."'
            ),
            "outcome": "neutral",
        },
    },
}
