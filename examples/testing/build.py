from gobomatic import *

from main import Self as main

stage = Sprite(
    "Stage",
    costumes = [
        "assets/blank.svg"
    ]
)

Self = Project(
    sprites = [
        stage,
        main
    ]
)

Self.export("project.sb3", debug=True)
