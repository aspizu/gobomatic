from ..primitives import StatementBlock, ReporterBlock, InputType


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
        self.define("looks_costumenumbername", fields={"NUMBER_NAME": "number"})


class CostumeName(ReporterBlock):
    def __init__(self):
        self.define("looks_costumenumbername", fields={"NUMBER_NAME": "name"})


class BackdropNumber(ReporterBlock):
    def __init__(self):
        self.define("looks_backdropnumbername", fields={"NUMBER_NAME": "number"})


class BackdropName(ReporterBlock):
    def __init__(self):
        self.define("looks_backdropnumbername", fields={"NUMBER_NAME": "name"})


class Size(ReporterBlock):
    def __init__(self):
        self.define("looks_size")


class SetGraphicEffect(StatementBlock):
    def __init__(self, effect: str, value: InputType):
        self.define(
            "looks_seteffectto",
            inputs={"VALUE": value},
            fields={"EFFECT": effect},
        )


class ChangeGraphicEffect(StatementBlock):
    def __init__(self, effect: str, value: InputType):
        self.define(
            "looks_changeeffectby",
            inputs={"CHANGE": value},
            fields={"EFFECT": effect},
        )


def SetColorEffect(value: InputType) -> StatementBlock:
    return SetGraphicEffect("COLOR", value)


def SetFisheyeEffect(value: InputType) -> StatementBlock:
    return SetGraphicEffect("FISHEYE", value)


def SetWhirlEffect(value: InputType) -> StatementBlock:
    return SetGraphicEffect("WHIRL", value)


def SetPixelateEffect(value: InputType) -> StatementBlock:
    return SetGraphicEffect("PIXELATE", value)


def SetMosaicEffect(value: InputType) -> StatementBlock:
    return SetGraphicEffect("MOSAIC", value)


def SetBrightnessEffect(value: InputType) -> StatementBlock:
    return SetGraphicEffect("BRIGHTNESS", value)


def SetGhostEffect(value: InputType) -> StatementBlock:
    return SetGraphicEffect("GHOST", value)


def ChangeColorEffect(value: InputType) -> StatementBlock:
    return ChangeGraphicEffect("COLOR", value)


def ChangeFisheyeEffect(value: InputType) -> StatementBlock:
    return ChangeGraphicEffect("FISHEYE", value)


def ChangeWhirlEffect(value: InputType) -> StatementBlock:
    return ChangeGraphicEffect("WHIRL", value)


def ChangePixelateEffect(value: InputType) -> StatementBlock:
    return ChangeGraphicEffect("PIXELATE", value)


def ChangeMosaicEffect(value: InputType) -> StatementBlock:
    return ChangeGraphicEffect("MOSAIC", value)


def ChangeBrightnessEffect(value: InputType) -> StatementBlock:
    return ChangeGraphicEffect("BRIGHTNESS", value)


def ChangeGhostEffect(value: InputType) -> StatementBlock:
    return ChangeGraphicEffect("GHOST", value)


class Hide(StatementBlock):
    def __init__(self):
        self.define("looks_hide")


class Show(StatementBlock):
    def __init__(self):
        self.define("looks_show")


class GotoFrontBack(StatementBlock):
    def __init__(self, front_back: str):
        self.define("looks_gotofrontback", fields={"FRONT_BACK": front_back})


def GotoFront() -> StatementBlock:
    return GotoFrontBack("front")


def GotoBack() -> StatementBlock:
    return GotoFrontBack("back")


class GoForwardBackwardLayers(StatementBlock):
    def __init__(self, forward_backward: str, layers: InputType):
        self.define(
            "looks_goforwardbackwardlayers",
            inputs={"NUM": layers},
            fields={"FORWARD_BACKWARD": forward_backward},
        )


def GoForward(layers: InputType) -> StatementBlock:
    return GoForwardBackwardLayers("forward", layers)


def GoBackward(layers: InputType) -> StatementBlock:
    return GoForwardBackwardLayers("backward", layers)
