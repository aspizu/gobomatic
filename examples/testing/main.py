from gobomatic import *

Self = Sprite(
    name=__name__,
    costumes = [
        "assets/scratchcat.svg"
    ]
)

Self.WhenFlagClicked(
    Goto(-100, 0),
    Glide(0, 0, 0.5),
    Say("Hello, World!"),
)
