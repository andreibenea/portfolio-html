data_core = {
    "id": "data_core",
    "name": "Data Core",
    "description": (
        "Racks of storage arrays ring the circular chamber, their indicator lights "
        "twinkling like a captive starfield. Thick data trunks converge into a "
        "central pillar, wrapped in armored casing and covered in warning sigils.\n\n"
        "At the room's center, a holographic interface hangs in the air: "
        "WARDEN, the Vault's security AI."
    ),
    "objects": {
        "arrays": {
            "kind": "scenery",
            "description": (
                "The storage racks hold decades of logs, personnel files, incident "
                "reports, and probably a dozen things the Overseer swore didn't exist."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
            "needs_item": None,
            "dialog_id": None,
        },
        ### add below to NPCS (AI) ###
        # "warden": {
        #     "kind": "actionable",
        #     "description": (
                # "WARDEN’s hologram manifests as a faceted mask of blue light, eyes "
                # "reduced to scanning glyphs that flicker in unreadable patterns."
        #     ),
        #     "can_take": False,
        #     "can_talk": True,
        #     "is_exit": False,
        #     "needs_item": None,
        #     "dialog_id": "warden_data_core",
        # },
        ### add above to NPCS (AI) ###
        "access_port": {
            "kind": "hint",
            "description": (
                "A physical access port sits at the base of the central pillar, "
                "large enough to accept a Pip-Boy link. Without yours, you're stuck "
                "bargaining with the AI instead of bending it."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
            "needs_item": "pip-boy",
            "dialog_id": "data_core_hint_port",
        },
        "maintenance_tunnels_door": {
            "kind": "actionable",
            "description": (
                "A security field blocks the tunnel entrance, humming at a frequency "
                "you can feel in your teeth."
            ),
            "description_unlocked": "The tunnel entrance is clear, the hum of the security field gone.",
            "can_take": False,
            "can_talk": False,
            "is_exit": True,
        }
    },
    "exits": {
        "maintenance_tunnels_door": {
            "status": "unlocked",
            "description_locked": (
                "A security field blocks the tunnel entrance, humming at a frequency "
                "you can feel in your teeth."
            ),
            "description_unlocked": (
                "The tunnel entrance is clear, the hum of the security field gone."
            ),
            "destination": "maintenance_tunnels",
            "on_unlock": (
                "The security field gutters and dies, leaving only the faint smell of "
                "ozone behind."
            ),
            "unlocked_via": None, # change to "warden"
        },
    },
}
