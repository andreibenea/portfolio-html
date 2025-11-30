warden_data_core_2 = {
    "npc_id": "warden",
    "intro": ('"SCENARIO REVISION IN PROGRESS," WARDEN announces.\n'),
    "intro_dialogue": (
        'You require two assets: restored system trust and physical clearance.'
    ),
    "options": {
        1: {
            "player": "Restore my clearance and tag me as a response unit.",
            "npc": (
                '"Processing…"\n\n'
                '"Status update: C-11 reclassified as PROVISIONAL RESPONSE AGENT. '
                "Security will treat your movements as incident-related until "
                'revocation or death."\n\n'
                '"Note: probability of death remains non-trivial."'
            ),
            "outcome": "go_next",
        },
        2: {
            "player": "Open the route back to the tunnels and Engineering.",
            "npc": (
                '"Releasing local lockouts. Maintenance tunnels and Engineering '
                'access restored."\n\n'
                '"Recommendation: utilize reactor incident simulation to trigger '
                "Vault-wide alert. This will maximize your odds of reaching the "
                'primary door without lethal intervention."'
            ),
            "outcome": "good",
        },
        3: {
            "player": "I want the truth. Who ordered my sedation?",
            "npc": (
                '"Overseer authorization confirmed."\n\n'
                '"Context: directive originated from unidentified external channel. '
                'Metadata scrubbed at source."\n\n'
                '"Conclusion: this Vault is no longer a closed system."'
            ),
            "outcome": "go_next",
        },
    },
}
