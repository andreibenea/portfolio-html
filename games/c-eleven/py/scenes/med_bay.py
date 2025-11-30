med_bay = {
    "id": "med_bay",
    "name": "Med Bay",
    "description": (
        "The Med Bay smells faintly of antiseptic and recycled air. Pale green curtain "
        "partitions cast long shadows against the walls, and a bank of diagnostic "
        "monitors hums quietly by the far bulkhead.\n\n"
        "One bed looks recently used, the sheets rumpled. A supply locker sits along "
        "the wall, its access light pulsing standby blue. A ceiling-mounted camera "
        "follows your movements with a soft mechanical whirr."
    ),
    "objects": {
        "bed": {
            "kind": "scenery",
            "description": (
                "The bed's sheets are still warm, indentation fresh on the pillow. "
                "Someone was here not long ago—maybe the person who dosed you."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
            "needs_item": None,
            "dialog_id": None,
        },
        # to be extended with a PIN; change to "actionable"
        "supply_locker": { 
            "kind": "scenery",
            "description": (
                "A standard Vault med supply locker. The panel shows a green standby "
                "light and a prompt for basic access privileges."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
            "needs_item": None,  
            "dialog_id": None,
        },
        "med_terminal": {
            "kind": "hint",
            "description": (
                "The Med Bay terminal lists a series of recent sedative doses, most of "
                "them tagged to C-wing residents. Your ID code is flagged with "
                '"UNAUTHORIZED ADMIN OVERRIDE".\n\n'
                "Whatever happened to you wasn't an accident."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
            "needs_item": None,
            "dialog_id": "med_terminal_hint",
        },
        "camera": {
            "kind": "scenery",
            "description": (
                "A ceiling-mounted security camera tracks you with lazy precision. "
                "If someone is watching, they haven't intervened — yet."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
            "needs_item": None,
            "dialog_id": None,
        },
        "hallway_door": {
            "id": "hallway_door",
            "kind": "actionable",
            "description": (
                "A standard sliding Vault door. The status light glows green - it's unlocked."
            ),
            "description_unlocked": (
                "A standard sliding Vault door. The status light glows green - it's unlocked."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": True,
        },
        "maintenance_hatch": {
            "id": "maintenance_hatch",
            "kind": "actionable",
            "description": (
                "A low hatch marked MAINTENANCE ONLY. The wheel handle refuses to "
                "budge — looks like it's sealed from the other side."
            ),
            "description_unlocked": (
                "The maintenance hatch hangs slightly open, a draft of cooler air "
                "whispering from the tunnels beyond."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": True,
        },
        ### move below to NPCS ###
        # "riley": {
        #     "kind": "actionable",
        #     "description": (
        #         "Riley, a maintenance tech in a grease-stained jumpsuit, leans against "
        #         "a cart stacked with tools and an open diagnostics tablet. Their eyes "
        #         "flick to the door every few seconds, like they're expecting trouble."
        #     ),
        #     "can_take": False,
        #     "can_talk": True,
        #     "is_exit": False,
        #     "needs_item": None,
        #     "dialog_id": "riley_med_bay",
        # },
        ### move above to NPCS ###
    },
    "exits": {
        "hallway_door": {
            "status": "unlocked",
            "description_locked": (
                "The blast door to the main corridor is sealed, Med Bay access light "
                "glowing an accusing red."
            ),
            "description_unlocked": (
                "The Med Bay door stands slightly ajar, emergency seals retracted. "
                "The corridor beyond flickers with intermittent lighting."
            ),
            "destination": "hallway_ground",
            "on_unlock": (
                "The Med Bay door cycles through a short decompression routine before "
                "gliding open with a hiss of equalizing pressure."
            ),
            "unlocked_via": None,
        },
        "maintenance_hatch": {
            "status": "locked",
            "description_locked": (
                "A low hatch marked MAINTENANCE ONLY. The wheel handle refuses to "
                "budge—looks like it's sealed from the other side."
            ),
            "description_unlocked": (
                "The maintenance hatch hangs slightly open, a draft of cooler air "
                "whispering from the tunnels beyond."
            ),
            "destination": "maintenance_tunnels",
            "on_unlock": (
                "Riley works the hatch wheel with a tired grunt. \"There. If you're "
                'heading into the guts of the Vault, try not to die in there, yeah?"'
            ),
            "unlocked_via": "riley",
        },
    },
}
