# py/web_main.py

from npc import NonPlayerCharacter
from player import Player
from world import World
from event_emitter import Output
from game import Game
from scenes import SCENES


def create_world():
    """
    Build the same initial state you use in main.py, but WITHOUT calling game.run().

    If your real main.py has different descriptions, dialog IDs, or scene IDs,
    copy those values in here so the web version matches exactly.
    """

    juno = NonPlayerCharacter(
        id="juno",
        name="Juno",
        description=(
            "Juno carries an anxious energy beneath her calm exterior. Her posture "
            "is controlled, but her thoughts look like they're racing ahead of her words."
        ),
        scene_id="j23",
        dialog_id="juno_j23",
    )

    riley = NonPlayerCharacter(
        id="riley",
        name="Riley",
        description=(
            "Riley, a maintenance tech in a grease-stained jumpsuit, leans against "
            "a cart stacked with tools and an open diagnostics tablet. Their eyes "
            "flick to the door every few seconds, like they're expecting trouble."
        ),
        scene_id="med_bay",
        dialog_id="riley_med_bay",
    )

    security_guard_one = NonPlayerCharacter(
        id="security_guard_one",
        name="Security Guard",
        description=(
            "A tired-looking security officer, the same voice you heard crackling over the "
            "intercom outside your quarters."
        ),
        scene_id="security_office",
        dialog_id=None,  # dialogue ID later if needed
    )

    overseer = NonPlayerCharacter(
        id="overseer",
        name="Overseer",
        description=(
            "The Overseer of Vault 656, bearing the weight of the vault's systems, secrets, "
            "and the lives of everyone inside."
        ),
        scene_id="overseer_office",
        dialog_id=None,
    )

    warden = NonPlayerCharacter(
        id="warden",
        name="WARDEN",
        description=(
            "WARDEN's hologram manifests as a faceted mask of blue light, eyes "
                "reduced to scanning glyphs that flicker in unreadable patterns."
        ),
        scene_id="data_core",
        dialog_id="warden_data_core",
    )

    npcs = {
        "juno": juno,
        "riley": riley,
        "security_guard_one": security_guard_one,
        "overseer": overseer,
        "warden": warden,
    }

    output = Output()
    # Starting scene: Quarters C-11
    player = Player("You", "Player", SCENES["c11"]["id"])
    world = World(SCENES, npcs)
    game = Game(player, world, output, allow_exit=False)

    return game, output


# Create a global game + output instance for the web session
game, output = create_world()


def start():
    """
    Called once from JavaScript when the page loads.
    Emits the description of the current scene and returns all output events.
    """
    output.events.clear()
    # This mirrors what Game.run() does at the very start.
    output.emit(game.describe_current_scene(), "scene")
    return list(output.events)


def handle_input(text: str):
    """
    Called every time the player submits a command in the browser.
    Runs one 'step' of the game and returns the new output events.
    """
    text = (text or "").strip().lower()
    if not text:
        return []

    output.events.clear()
    # Reuse your existing command logic – no game loop, just one command at a time.
    try:
        game.handle_command(text)
    except SystemExit:
        # Game tried to exit (bad ending, quit, etc.)
        # Emit final messages plus a sentinel "game_over" event.
        output.emit("GAME OVER.", "system")
        output.emit("Refresh the page to play again.", "system")
        # Empty text is OK; we only care about the kind on the JS side.
        # output.emit("", "game_over")
    except Exception as e:
        output.emit(f"[ERROR] {e}", "system")

    return list(output.events)
