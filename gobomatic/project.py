import json
import zipfile
from . import code as scratchcode

from .helpers import *


class Sprite:
    def __init__(
        self,
        name: str,
        costumes: list[str] = [],
        sounds: list[str] = [],
    ):
        self.name: str = name
        self.variables: list[scratchcode.Var] = []
        self.lists: list[scratchcode.List] = []
        self.costumes: list[str] = costumes
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

    def Code(self, *code):
        self.code: list = code
        return self

    def WhenFlagClicked(self, *code):
        self.code.append(scratchcode.WhenFlagClicked(*code))
        return self

    def Def(self, in_tuple):
        prototype, define, call = in_tuple
        self.code.append(prototype)
        self.code.append(define)
        return call

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
