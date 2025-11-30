warden_data_core = {
    "npc_id": "warden",
    "intro": (
        "The holographic mask turns toward you, glyph-eyes dilating."
    ),
    "intro_dialogue": (
        "UNREGISTERED PRESENCE DETECTED IN RESTRICTED SECTOR, WARDEN intones.\n"
        "STATE YOUR DESIGNATION AND JUSTIFICATION FOR ACCESS."
    ),
    "options": {
        1: {
            "player": "Designation C-11, trainee. System sent me to investigate a security incident.",
            "npc": (
                "\"C-11: flagged as 'compromised asset'.\"\n\n"
                "\"Your presence here is statistically unlikely. Correlating causes…\"\n"
                "The glyphs ripple like a thinking frown.\n\n"
                "\"Probability of internal sabotage: rising.\""
            ),
            "outcome": "go_next",
        },
        2: {
            "player": "You know someone tampered with my records. Show me the overrides.",
            "npc": (
                "\"Request: audit trail disclosure.\"\n\n"
                "\"Warning: Overseer privileges supersede standard transparency mandates.\"\n"
                "The mask flickers.\n\n"
                "\"Counter-argument: integrity of Vault security model requires anomaly review. "
                "Request accepted under emergency clause.\""
            ),
            "outcome": "go_next",
        },
        3: {
            "player": "If you wanted me dead, you'd have sealed the tunnels. You brought me here.",
            "npc": (
                "WARDEN is silent for a long moment.\n\n"
                "\"Incorrect.\"\n"
                "\"However, given your presence, the optimal outcome is now conditional cooperation.\""
            ),
            "outcome": "go_next",
        },
    },
}
