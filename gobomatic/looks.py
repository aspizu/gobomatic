from .codeprimitives import *


class Say(StatementBlock):
    def __init__(self, message: InputType):
        self.define("looks_say", inputs={"MESSAGE": message})


class SayFor(StatementBlock):
    def __init__(self, message: InputType, time: InputType):
        self.define("looks_sayforsecs", inputs={"MESSAGE": message, "SECS": time})


class Think(StatementBlock):
    def __init__(self, message: InputType):
        self.define("looks_think", inputs={"MESSAGE": message})


class ThinkFor(StatementBlock):
    def __init__(self, message: InputType, time: InputType):
        self.define("looks_thinkforsecs", inputs={"MESSAGE": message, "SECS": time})


class SwitchCostume(StatementBlock):
    def __init__(self, costume: InputType):
        self.define("looks_switchcostumeto", inputs={"COSTUME": costume})


class NextCostume(StatementBlock):
    def __init__(self):
        self.define("looks_nextcostume")


class SwitchBackdrop(StatementBlock):
    def __init__(self, backdrop: InputType):
        self.define("looks_switchbackdropto", inputs={"BACKDROP": backdrop})


class NextBackdrop(StatementBlock):
    def __init__(self):
        self.define("looks_nextbackdrop")


class ChangeSize(StatementBlock):
    def __init__(self, change: InputType):
        self.define("looks_changesizeby", inputs={"CHANGE": change})


class SetSize(StatementBlock):
    def __init__(self, size: InputType):
        self.define("looks_setsizeto", inputs={"SIZE": size})


class ClearGraphicEffects(StatementBlock):
    def __init__(self):
        self.define("looks_cleargraphiceffects")


class CostumeNumber(ReporterBlock):
    def __init__(self):
        self.define("looks_costumenumbername", fields={"NUMBER_NAME": ["number", None]})


class CostumeName(ReporterBlock):
    def __init__(self):
        self.define("looks_costumenumbername", fields={"NUMBER_NAME": ["name", None]})


class Size(ReporterBlock):
    def __init__(self):
        self.define("looks_size")


class SetEffectColor(StatementBlock):
    def __init__(self, color: InputType):
        self.define(
            "looks_seteffectto",
            inputs={"VALUE": color},
            fields={"EFFECT": ["COLOR", None]},
        )


class SetEffectFisheye(StatementBlock):
    def __init__(self, fisheye: InputType):
        self.define(
            "looks_seteffectto",
            inputs={"VALUE": fisheye},
            fields={"EFFECT": ["FISHEYE", None]},
        )


class SetEffectWhirl(StatementBlock):
    def __init__(self, whirl: InputType):
        self.define(
            "looks_seteffectto",
            inputs={"VALUE": whirl},
            fields={"EFFECT": ["WHIRL", None]},
        )


class SetEffectPixelate(StatementBlock):
    def __init__(self, pixelate: InputType):
        self.define(
            "looks_seteffectto",
            inputs={"VALUE": pixelate},
            fields={"EFFECT": ["PIXELATE", None]},
        )


class SetEffectMosaic(StatementBlock):
    def __init__(self, mosaic: InputType):
        self.define(
            "looks_seteffectto",
            inputs={"VALUE": mosaic},
            fields={"EFFECT": ["MOSAIC", None]},
        )


class SetEffectBrightness(StatementBlock):
    def __init__(self, brightness: InputType):
        self.define(
            "looks_seteffectto",
            inputs={"VALUE": brightness},
            fields={"EFFECT": ["BRIGHTNESS", None]},
        )


class SetEffectGhost(StatementBlock):
    def __init__(self, ghost: InputType):
        self.define(
            "looks_seteffectto",
            inputs={"VALUE": ghost},
            fields={"EFFECT": ["GHOST", None]},
        )


class ChangeEffectColor(StatementBlock):
    def __init__(self, change: InputType):
        self.define(
            "looks_changeeffectby",
            inputs={"CHANGE": change},
            fields={"EFFECT": ["COLOR", None]},
        )


class ChangeEffectFisheye(StatementBlock):
    def __init__(self, change: InputType):
        self.define(
            "looks_changeeffectby",
            inputs={"CHANGE": change},
            fields={"EFFECT": ["FISHEYE", None]},
        )


class ChangeEffectWhirl(StatementBlock):
    def __init__(self, change: InputType):
        self.define(
            "looks_changeeffectby",
            inputs={"CHANGE": change},
            fields={"EFFECT": ["WHIRL", None]},
        )


class ChangeEffectPixelate(StatementBlock):
    def __init__(self, change: InputType):
        self.define(
            "looks_changeeffectby",
            inputs={"CHANGE": change},
            fields={"EFFECT": ["PIXELATE", None]},
        )


class ChangeEffectMosaic(StatementBlock):
    def __init__(self, change: InputType):
        self.define(
            "looks_changeeffectby",
            inputs={"CHANGE": change},
            fields={"EFFECT": ["MOSAIC", None]},
        )


class ChangeEffectBrightness(StatementBlock):
    def __init__(self, change: InputType):
        self.define(
            "looks_changeeffectby",
            inputs={"CHANGE": change},
            fields={"EFFECT": ["BRIGHTNESS", None]},
        )


class ChangeEffectGhost(StatementBlock):
    def __init__(self, change: InputType):
        self.define(
            "looks_changeeffectby",
            inputs={"CHANGE": change},
            fields={"EFFECT": ["GHOST", None]},
        )
