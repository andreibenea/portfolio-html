riley_med_bay_2 = {
    "npc_id": "riley",
    "intro": "Riley shifts their weight, lowering their voice further.",
    "intro_dialogue": (
        "All right. If you're still listening, here's the part that gets us both shot."
    ),
    "options": {
        1: {
            "player": "Tell me how to get my Pip-Boy back.",
            "npc": (
                "\"Security's got it tagged as 'evidence' in their office.\"\n\n"
                "\"But Security answers to WARDEN, and WARDEN's attention can be… "
                "redirected. There's a back channel in the maintenance tunnels that "
                "leads straight to the Data Core. If you talk fast enough, you might "
                "convince the AI you're an asset instead of a problem.\""
            ),
            "outcome": "go_next",
        },
        2: {
            "player": "You mentioned override orders. Who's pulling the strings?",
            "npc": (
                "\"Overseer signs the paperwork, sure. But half the orders I've seen "
                "have WARDEN's fingerprints all over them.\"\n\n"
                "\"The Vault's supposed to protect people. Somewhere along the line, "
                "the definition of 'people' narrowed to whoever's still useful.\""
            ),
            "outcome": "go_next",
        },
        3: {
            "player": "Why help me? You could just call this in.",
            "npc": (
                '"Because I like sleeping at night. And because last week they tagged '
                "my name on a transfer list by mistake. Took me three hours to convince "
                'the system I was still alive."\n\n'
                "\"If they're cleaning house, I want someone out there who knows where "
                'the bodies are buried."'
            ),
            "outcome": "go_next",
        },
    },
}
