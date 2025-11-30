under_construction = {
    "id": "under_construction",
    "name": "Sector In Assembly",
    "description": (
        "You step through… and immediately realize this part of the Vault was never "
        "meant for human eyes.\n\n"
        "The world around you is half-finished: walls fade into wireframes, floors "
        "end in sharp, glowing edges, and whole chunks of reality hang in the air as "
        "floating placeholders labeled TODO.\n\n"
        "Looming above it all are towering figures made of pure light, moving with "
        "slow, deliberate precision. They rearrange icons, stitch corridors together, "
        "and occasionally drag an entire room a few meters to the left before nodding "
        "in satisfaction.\n\n"
        "One of them pauses, notices you, and flickers a message into your vision:\n"
        '  "AREA STILL UNDER CONSTRUCTION. PLEASE COME BACK IN A LATER BUILD."\n\n'
        "The figure gives what might be a reassuring thumbs-up made of green pixels, "
        "then gently gestures you back the way you came."
    ),
    "objects": {
        "door": {
            "id": "door",
            "kind": "actionable",
            "description": (
                "A standard sliding Vault door. The status light glows yellow - it's locked."
            ),
            "description_unlocked": "A standard sliding Vault door. The status light glows green - it's unlocked.",
            "can_take": False,
            "can_talk": False,
            "is_exit": True,
        },
    },
    "exits": {
        "door": {
            "destination": "hallway_ground",
            "status": "unlocked",  # locked | unlocked (tba: jammed | sealed )
            "unlocked_via": None,
            "required_item": None,
            "unlock_on_use": False,
            "description_locked": (
                "A standard sliding Vault door. The status light glows yellow - it's locked."
            ),
            "description_unlocked": "A standard sliding Vault door. The status light glows green - it's unlocked.",
            "on_attempt": None,
            "on_unlock": None,
        }
    },
}
