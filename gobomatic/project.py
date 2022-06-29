import hashlib
import json
from zipfile import ZipFile

from . import primitives
from .blocks import events


def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])


def md5ext(path: str) -> str:
    return hashlib.md5(open(path, "rb").read()).hexdigest()


def extension_from_path(path: str) -> str:
    return path.split("/")[-1].split(".")[-1]


def filename_from_path(path: str) -> str:
    return ".".join(path.split("/")[-1].split(".")[:-1])


class Sprite:
    class FuncFactory:
        def __init__(
            self,
            sprite: "Sprite",
            args: tuple[primitives.ArgReporter, ...],
            name: str,
        ):
            self.sprite = sprite
            self.args_length = len(args)
            proccode = primitives.genproccode(name, args)
            self.prototype = primitives.ProcPrototype(
                proccode, [arg.name for arg in args]
            )
            self.sprite.blocks.append(self.prototype)

        def Define(self, *stack: primitives.StatementBlock):
            self.sprite.blocks.append(primitives.ProcDefinition(self.prototype)(*stack))
            return self

        def __call__(self, *args: primitives.InputType) -> primitives.ProcCall:
            if len(args) != self.args_length:
                raise Exception(
                    f"Wrong no of arguments: expected {self.args_length}, got {len(args)}"
                )
            return primitives.ProcCall(self.prototype, args)

    def __init__(self, name: str, costumes: list[str], sounds: list[str] = None):
        if len(costumes) < 1:
            raise Exception("Must atleast have one costume")

        self.name: str = name
        self.costumes: list[str] = costumes
        self.sounds: list[str] = sounds or []

        self.variables: list[primitives.Var] = []
        self.lists: list[primitives.List] = []
        self.blocks: list[primitives.Block] = []

    def Func(self, *args: primitives.ArgReporter, name: str) -> "Sprite.FuncFactory":
        return Sprite.FuncFactory(self, args, name)

    def Var(self, name: str, value: primitives.ValueType = 0) -> primitives.Var:
        var = primitives.Var(name, value)
        self.variables.append(var)
        return var

    def List(
        self, name: str, values: list[primitives.ValueType] = None
    ) -> primitives.List:
        lst = primitives.List(name, values)
        self.lists.append(lst)
        return lst

    def WhenFlagClicked(self, *stack: primitives.StatementBlock):
        self.blocks.append(events.WhenFlagClicked(stack))
        return self

    def WhenKeyPressed(self, key: str) -> events.WhenKeyPressed:
        block = events.WhenKeyPressed(key)
        self.blocks.append(block)
        return block

    def WhenBackdropSwitchesTo(self, backdrop: str) -> events.WhenBackdropSwitchesTo:
        block = events.WhenBackdropSwitchesTo(backdrop)
        self.blocks.append(block)
        return block

    def WhenLoudnessGreaterThan(
        self, loudness: primitives.InputType
    ) -> events.WhenGreaterThan:
        block = events.WhenLoudnessGreaterThan(loudness)
        self.blocks.append(block)
        return block

    def WhenTimerGreaterThan(
        self, time: primitives.InputType
    ) -> events.WhenGreaterThan:
        block = events.WhenTimerGreaterThan(time)
        self.blocks.append(block)
        return block

    def WhenReceived(self, event: str) -> events.WhenReceived:
        block = events.WhenReceived(event)
        self.blocks.append(block)
        return block

    def WhenThisSpriteClicked(self, *stack: primitives.StatementBlock):
        self.blocks.append(events.WhenThisSpriteClicked(stack))
        return self

    def serialize(self):
        def variables():
            return {var.id: [var.name, 0] for var in self.variables}

        def lists():
            return {lst.id: [lst.name, []] for lst in self.lists}

        def blocks():
            return {
                i["id"]: {a: b for a, b in i.items() if a != "id"}
                for i in flatten([x.serialize() for x in self.blocks])
            }

        def costumes():
            return [
                {
                    "assetId": md5ext(costume),
                    "name": filename_from_path(costume),
                    "md5ext": md5ext(costume) + "." + extension_from_path(costume),
                    "dataFormat": extension_from_path(costume),
                }
                for costume in self.costumes
            ]

        # TODO
        def sounds():
            return []

        return {
            "isStage": self.name == "Stage",
            "name": self.name,
            "variables": variables(),
            "lists": lists(),
            "blocks": blocks(),
            "costumes": costumes(),
            "sounds": sounds(),
        }


class Project:
    def __init__(self, sprites: list[Sprite]):
        if len(sprites) < 1:
            raise Exception("Must atleast have 'Stage' sprite")
        if sprites[0].name != "Stage":
            raise Exception("First sprite must be 'Stage'")

        self.sprites: list[Sprite] = sprites

    def serialize(self):
        return {
            "targets": [sprite.serialize() for sprite in self.sprites],
            "meta": {"semver": "3.0.0", "vm": "0.2.0", "agent": ""},
        }

    def export(self, output: str, debug: bool = False):
        sb3: ZipFile = ZipFile(output, "w")
        for sprite in self.sprites:
            for costume in sprite.costumes:
                sb3.write(
                    costume,
                    arcname=md5ext(costume) + "." + extension_from_path(costume),
                )
        project_json = self.serialize()
        if debug:
            from rich import print

            print(project_json)
        sb3.writestr("project.json", json.dumps(project_json))
        return self
