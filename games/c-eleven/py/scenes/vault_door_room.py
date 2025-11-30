vault_door_room = {
    "id": "vault_door_room",
    "name": "Vault Door Antechamber",
    "description": (
        "You stand before the massive gear-shaped Vault Door. Warning lights blink slowly. "
        "A control podium sits nearby, blank where a Pip-Boy interface should be."
    ),
    "objects": {
        "vault_door": {
            "kind": "actionable",
            "description": (
                "The colossal Vault Door is sealed shut. Mechanical locks and massive hinges hold it in place."
            ),
            "description_unlocked": "The colossal Vault Door is finally open. Go through to explore the entire world.... someday",
            "can_take": False,
            "can_talk": False,
            "is_exit": True,
        },
        "control_podium": {
            "kind": "scenery",
            "description": (
                "A control podium with a recessed Pip-Boy docking port and a small status display."
            ),
            "can_take": False,
            "can_talk": False,
            "is_exit": False,
        },
        "door": {
            "kind": "actionable",
            "description": "A reinforced sliding Vault door with its status light glowing green: unlocked.", # needs updating!
            "description_unlocked": "A reinforced sliding Vault door with its status light glowing green: unlocked.",
            "can_take": False,
            "can_talk": False,
            "is_exit": True,
        },
    },
    "exits": {
        "door": {
            "destination": "hallway_ground",  # state
            "status": "unlocked",  # locked | unlocked (tba: jammed | sealed )
            "unlocked_via": None,
            "required_item": None,  # item (pip-boy) or None
            "unlock_on_use": False,  # if using it performs unlock
            # descriptions
            "description_locked": (
                "A reinforced sliding Vault door with a glowing yellow status light — local lockdown. "
                "Under normal conditions it would open at a touch. Now it's sealed by an override from the outside."
            ),
            "description_unlocked": "A reinforced sliding Vault door with its status light glowing green: unlocked.",
            # optional: custom text or event when attempting to open
            "on_attempt": None,
            "on_unlock": "A soft chime sounds as the door's status light shifts from yellow to green.",
        },
        "vault_door": {
            "destination": "world",  # state
            "status": "locked",  # locked | unlocked (tba: jammed | sealed )
            "unlocked_via": "control_podium",
            "required_item": "pip-boy",  # item (pip-boy) or None
            "unlock_on_use": False,  # if using it performs unlock
            # descriptions
            "description_locked": (
                "The colossal Vault Door is sealed shut. Mechanical locks and massive hinges hold it in place."
            ),
            "description_unlocked": "A reinforced sliding Vault door with its status light glowing green: unlocked.",
            # optional: custom text or event when attempting to open
            "on_attempt": None,
            "on_unlock": "A soft chime sounds as the door's status light shifts from yellow to green.",
        },
    },
    "flags": {
        "vault_door_unlocked": False,
        "door_locked": False,
    },
}
