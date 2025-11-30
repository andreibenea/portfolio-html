maintenance_tunnels = {
    "id": "maintenance_tunnels",
    "name": "Maintenance Tunnels",
    "description": (
        "The maintenance tunnels are a cramped maze of pipes, conduits, and "
        "dripping condensation. The lighting here has given up entirely; the only "
        "illumination comes from the occasional status diode blinking in the dark."
        "\n\nYour footsteps echo in uncomfortable ways."
    ),
    "objects": {
        "pipe_leak": {
            "kind": "scenery",
            "description": (
                "A thin spray of coolant hisses from a cracked pipe, turning the air "
                "frigid. Someone patched it with tape that really shouldn't be rated "
                "for this kind of pressure."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
            "needs_item": None,
            "dialog_id": None,
        },
        "maintenance_tags": {
            "kind": "hint",
            "description": (
                "Handwritten maintenance tags are zip-tied to several junctions. "
                "Most are scribbled with routine notes, but one stands out:\n\n"
                '"RILEY: reroute camera feeds to DATA CORE first, then Med Bay. '
                'If they notice, we’re already dead."'
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
            "needs_item": None,
            "dialog_id": "tunnel_hint_tags",
        },
        "data_core_door": {
            "id": "door",
            "kind": "actionable",
            "description": (
                "A security bulkhead blocks the route deeper into the tunnels."
            ),
            "description_unlocked": (
                "Beyond a narrow squeeze, the tunnel opens into a chamber lit by "
                "cold blue monitor glow."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": True,
        },
    },
    "exits": {
        "to_med_bay": {
            "status": "unlocked",
            "description_locked": (
                "The hatch toward the Med Bay is dogged shut from the other side."
            ),
            "description_unlocked": (
                "A short ladder leads up to the underside of the Med Bay maintenance hatch."
            ),
            "destination": "med_bay",
            "on_unlock": (
                "With some effort, you force the hatch mechanism and feel cooler, "
                "cleaner air spill down from the Med Bay above."
            ),
            "unlocked_via": None,
        },
        "data_core_door": {
            "status": "unlocked",
            "description_locked": (
                "A security bulkhead blocks the route deeper into the tunnels."
            ),
            "description_unlocked": (
                "Beyond a narrow squeeze, the tunnel opens into a chamber lit by "
                "cold blue monitor glow."
            ),
            "destination": "data_core",
            "on_unlock": (
                "You slip past the half-jammed bulkhead and follow the cabling until "
                "the tunnels widen into the Vault’s hidden data core."
            ),
            "unlocked_via": None,
        },
    },
}
