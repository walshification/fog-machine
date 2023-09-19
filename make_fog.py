"""Generate commits for shroud my GitHub profile in activity."""

import random
import os

# zalgoification algorithm found here:
# https://codegolf.stackexchange.com/questions/57601/z%CC%A1%CC%ACa%CC%AF%CC%A7%CC%94l%CC%86%CC%93g%CC%98%CC%9F%CC%9Bo%CC%A1-generator
def zalgoify(message: str) -> str:
    return "".join(
        [
            v, v + "".join(
                random.choice(
                    [chr(char) for char in range(768,815)]
                ) for _ in range(int(random.normalvariate(10, 5)))
            )
        ]
        for v in message
        if v.isalpha()
    )

messages = [
    "initial commit",
    "update readme.md",
    "update",
    "first commit",
    "dummy",
    "updated readme",
    "pi push",
    "create readme.md",
    "fix",
    "cleanup",
    "test",
    "typo",
    "wip",
    "bump version",
    "updates"
]

for n in range(random.randint(1, 10)):
    message = zalgoify(random.choice(messages))
    os.system(f"git commit -m '{message}' --allow-empty")
