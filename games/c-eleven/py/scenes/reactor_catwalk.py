reactor_catwalk = {
    "id": "reactor_catwalk",
    "name": "Reactor Catwalk",
    "description": (
            "Heat rolls off the reactor core in slow, suffocating waves. The narrow "
            "catwalk vibrates under your boots, every tremor a reminder of the "
            "megawatts roaring beneath you.\n\n"
            "A safety railing barely comes up to your hips. Warning holos hover over "
            "the drop, politely suggesting you avoid falling into the glowing heart "
            "of Vault 656."
    ),
    "objects": {
        "core": {
            "kind": "scenery",
            "description": (
                "The reactor core churns with contained violence, protective fields "
                "rippling like heat haze. Whatever is wrong with the Vault, the core "
                "is compensating—for now."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
            "needs_item": None,
            "dialog_id": None,
        },
        "control_panel": {
            "kind": "actionable",
            "description": (
                "A small side panel allows limited manual overrides: power shunts, "
                "emergency scram triggers, and a curious entry labeled "
                "\"SECURITY INCIDENT SIMULATION\".\n\n"
                "This might be the back-door Juno was counting on."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
            "needs_item": None,
            "dialog_id": None,
        },
        "safety_sign": {
            "kind": "hint",
            "description": (
                "A fading sign warns: DO NOT TRIGGER INCIDENT MODE WHILE PERSONNEL "
                "ARE IN LOCKED SECURE AREAS.\n\n"
                "Which, interpreted generously, means: flip the switch while the "
                "guards are penned up and the Vault might unseal in interesting ways."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
            "needs_item": None,
            "dialog_id": "reactor_incident_hint",
        },
    },
    "exits": {
        "back_to_engineering": {
            "status": "unlocked",
            "description_locked": (
                "The hatch back to Engineering is sealed with an internal "
                "lockout you don't recognize."
            ),
            "description_unlocked": (
                "The hatch to Engineering stands open, catwalk vibrations fading "
                "into the steadier hum of the bay."
            ),
            "destination": "engineering_bay",
            "on_unlock": (
                "The hatch cycles open, the noisy air of Engineering rushing "
                "in to replace the reactor’s oppressive heat."
            ),
            "unlocked_via": None,
        },
    },
}
