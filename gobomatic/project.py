import json
import zipfile
import glob
from . import code as scratchcode

from typing import Union
from .helpers import *


class Sprite:
    def __init__(
        self,
        name: str,
        costumes: Union[list[str], str] = [],
        sounds: list[str] = [],
    ):
        self.name: str = name
        self.variables: list[scratchcode.Var] = []
        self.lists: list[scratchcode.List] = []
        self.costumes: list[str]
        if isinstance(costumes, str):
            self.costumes = glob.glob(costumes)
        else:
            self.costumes = costumes
        self.sounds: list[str] = sounds
        self.code: list = []

    def Var(self, name: str = None):
        variable = scratchcode.Var(name)
        self.variables.append(variable)
        return variable

    def List(self, name: str = None):
        list_ = scratchcode.List(name)
        self.lists.append(list_)
        return list_

    def Code(self, *code: Union[scratchcode.StatementBlock, scratchcode.HatBlock]):
        self.code.extend(code)
        return self

    def WhenFlagClicked(self, *code: scratchcode.StatementBlock):
        self.Code(scratchcode.WhenFlagClicked(*code))
        return self

    def WhenKeyPressed(self, key: str):
        block = scratchcode.WhenKeyPressed(key)
        self.Code(block)
        return block

    def WhenBackdropSwitchesTo(self, backdrop: str):
        block = scratchcode.WhenBackdropSwitchesTo(backdrop)
        self.Code(block)
        return block

    def WhenLoudnessGreaterThan(self, loudness: scratchcode.InputType):
        block = scratchcode.WhenLoudnessGreaterThan(loudness)
        self.Code(block)
        return block

    def WhenTimerGreaterThan(self, timer: scratchcode.InputType):
        block = scratchcode.WhenTimerGreaterThan(timer)
        self.Code(block)
        return block

    def WhenReceived(self, event: str):
        block = scratchcode.WhenReceived(event)
        self.Code(block)
        return block

    def WhenThisSpriteClicked(self, *code: scratchcode.StatementBlock):
        self.Code(scratchcode.WhenThisSpriteClicked(*code))
        return self

    class Func_Class:
        def __init__(self, sprite: "Sprite", *args: scratchcode.ArgReporter, name=None):
            self.sprite = sprite
            self.args = args
            self.name = str(id(self)) if name is None else name
            self.proccode = scratchcode.gen_proccode(self.name, self.args)
            self.prototype = scratchcode.ProcedurePrototype(
                self.proccode, [arg.name for arg in self.args]
            )
            self.sprite.code.append(self.prototype)

        def Define(self, *stack: scratchcode.StatementBlock):
            self.definition = scratchcode.ProcedureDefinition(self.prototype)(*stack)
            self.sprite.code.append(self.definition)

        def __call__(self, *args: scratchcode.InputType):
            if len(args) != len(self.args):
                raise Exception(
                    f'Call to function "{self.name}" with {len(args)} arguments'
                )
            return scratchcode.ProcedureCall(self.prototype, args)

    def Func(
        self, *args: scratchcode.ArgReporter, name: str = None
    ) -> "Sprite.Func_Class":
        return Sprite.Func_Class(self, *args, name=name)

    def serialize_costumes(self):
        return [
            {
                "assetId": md5ext(costume),
                "name": filename_from_path(costume),
                "md5ext": md5ext(costume) + "." + extension_from_path(costume),
                "dataFormat": extension_from_path(costume),
            }
            for costume in self.costumes
        ]

    def serialize_blocks(self):
        return {
            i["id"]: {a: b for a, b in i.items() if a != "id"}
            for i in flatten([x.serialize() for x in self.code])
        }

    def serialize_variables(self):
        return {var.name: [var.name, 0] for var in self.variables}

    def serialize_lists(self):
        return {var.name: [var.name, []] for var in self.lists}

    def serialize_sounds(self):
        return []  # TODO
        return [
            {
                "assetId": md5ext(sound),
                "name": filename_from_path(sound),
                "dataFormat": extension_from_path(sound),
                "rate": 48000,
                "sampleCount": 61300,
                "md5ext": md5ext(sound) + "." + extension_from_path(sound),
            }
            for sound in self.sounds
        ]

    def serialize(self):
        return {
            "isStage": self.name == "Stage",
            "name": self.name,
            "variables": self.serialize_variables(),
            "lists": self.serialize_lists(),
            "blocks": self.serialize_blocks(),
            "costumes": self.serialize_costumes(),
            "sounds": self.serialize_sounds(),
        }


class Project:
    def __init__(self, sprites: list[Sprite]):
        if len(sprites) < 1 or sprites[0].name != "Stage":
            raise Exception("First sprite must be Stage.")
        self.sprites: list[Sprite] = sprites

    def serialize(self):
        return {
            "targets": [sprite.serialize() for sprite in self.sprites],
            "extensions": [],
            "meta": {"semver": "3.0.0", "vm": "0.2.0", "agent": ""},
        }

    def export(self, output_path: str, debug=False):
        sb3 = zipfile.ZipFile(output_path, "w")
        costumes = flatten([sprite.costumes for sprite in self.sprites])
        for costume in costumes:
            sb3.write(
                costume, arcname=md5ext(costume) + "." + extension_from_path(costume)
            )
        project_json = self.serialize()
        if debug:
            from rich import print

            print(project_json)
        sb3.writestr("project.json", json.dumps(project_json))
        return self
