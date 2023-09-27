"""Generate commits for shroud my GitHub profile in activity."""

import json
import os
import random
from typing import Sequence


PLAYS = [play for _, _, plays in os.walk("./fog_machine/shakespeare") for play in plays]


def main(dir_path: str = "./fog_machine/shakespeare/") -> None:
    """Generate Zalgo text messages with random lines of Shakespeare."""
    lines = read_random_shakespeare(dir_path)

    messages = create_shakespearean_zalgo_text(lines)
    for message in messages:
        os.system(f"git commit -m '{message}' --allow-empty")


def read_random_shakespeare(
        dir_path: str, plays: Sequence[str] = PLAYS
    ) -> Sequence[str]:
    """Return lines from a randomly-chosen Shakespeare play."""
    with open(f"{dir_path}{random.SystemRandom().choice(plays)}") as play:
        lines = json.loads(play.read())

    return lines


def create_shakespearean_zalgo_text(lines: Sequence[str]) -> str:
    """Return a list of Zalgo text lines from Shakespeare."""
    messages = []
    for _ in range(random.SystemRandom().choice([i for i in range(1, 10)])):
        line = random.SystemRandom().choice(
            random.SystemRandom().choice(
                random.SystemRandom().choice(
                    lines["chapters"]
                )["paragraphs"]
            )["lines"]
        )
        messages.append(zalgoify(line))

    return messages


# zalgoification algorithm found here:
# https://codegolf.stackexchange.com/questions/57601/z%CC%A1%CC%ACa%CC%AF%CC%A7%CC%94l%CC%86%CC%93g%CC%98%CC%9F%CC%9Bo%CC%A1-generator
def zalgoify(message: str) -> str:
    """Return a Zalgo text version of a given message."""
    return "".join(
        [
            v, v + "".join(
                random.choice(
                    [chr(char) for char in range(768,815)]
                ) for _ in range(int(random.normalvariate(10, 5)))
            )
        ][v.isalpha()]
        for v in message
    )


if __name__ == "__main__":
    main()
