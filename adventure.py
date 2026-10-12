"""A short forest adventure about finding a hidden village."""

SCENES = {
    "forest_edge": {
        "title": "The Forest Edge",
        "text": "You step beneath the trees, searching for the hidden village.",
        "choices": [
            ("Follow a trail of blue flowers", "blue_trail"),
            ("Listen for a distant bell", "bell_path"),
        ],
    },
    "blue_trail": {
        "title": "The Blue Trail",
        "text": "The flowers lead to a mossy bridge over a rushing stream.",
        "choices": [
            ("Cross the bridge carefully", "old_bridge"),
            ("Follow the stream upstream", "stream_bank"),
        ],
    },
    "bell_path": {
        "title": "The Bell Path",
        "text": "A faint bell rings near a grove of towering pines.",
        "choices": [
            ("Head toward the sound", "pine_grove"),
            ("Climb a nearby hill to look around", "lookout"),
        ],
    },
    "old_bridge": {
        "title": "The Old Bridge",
        "text": "On the far side, you find a lantern beside a stone marker.",
        "choices": [
            ("Take the lantern and follow the markers", "lantern_path"),
            ("Leave the lantern and turn back", "forest_edge"),
        ],
    },
    "stream_bank": {
        "title": "The Stream Bank",
        "text": "The stream disappears beneath a rocky arch.",
        "choices": [
            ("Go through the arch", "lantern_path"),
            ("Call out and wait for an answer", "lost_ending"),
        ],
    },
    "pine_grove": {
        "title": "The Pine Grove",
        "text": "A fox watches you beside two paths marked with carved leaves.",
        "choices": [
            ("Follow the silver-leaf markers", "village_ending"),
            ("Follow the red-leaf markers", "lost_ending"),
        ],
    },
    "lookout": {
        "title": "The Lookout",
        "text": "From the hill, you spot smoke curling up beyond the woods.",
        "choices": [
            ("Walk toward the smoke", "village_ending"),
            ("Follow a narrow path into a dark ravine", "ravine_ending"),
        ],
    },
    "lantern_path": {
        "title": "The Lantern Path",
        "text": "The lantern glows brighter as the trees grow close together.",
        "choices": [
            ("Follow the warm light between the trees", "village_ending"),
            ("Set the lantern down and explore a cave", "ravine_ending"),
        ],
    },
}

ENDINGS = {
    "village_ending": (
        "The Hidden Village",
        "You find a welcoming village tucked beneath the forest canopy.",
    ),
    "lost_ending": (
        "Lost in the Woods",
        "Night falls before you find the village. You make camp and try again at dawn.",
    ),
    "ravine_ending": (
        "The Quiet Ravine",
        "The ravine is peaceful, but the village remains a mystery.",
    ),
}


def play():
    """Run the adventure until the player reaches an ending."""
    scene_id = "forest_edge"

    while scene_id not in ENDINGS:
        scene = SCENES[scene_id]
        print(f"\n{scene['title']}\n{scene['text']}")

        for number, (label, _) in enumerate(scene["choices"], start=1):
            print(f"{number}. {label}")

        # Keep asking until the player selects one of the two choices.
        while True:
            choice = input("Choose 1 or 2: ").strip()
            if choice in ("1", "2"):
                scene_id = scene["choices"][int(choice) - 1][1]
                break
            print("Please enter 1 or 2.")

    title, text = ENDINGS[scene_id]
    print(f"\n{title}\n{text}")


if __name__ == "__main__":
    play()
