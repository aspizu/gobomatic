from .codeprimitives import *


class EraseAll(StatementBlock):
    def __init__(self):
        self.define("pen_clear")


class Stamp(StatementBlock):
    def __init__(self):
        self.define("pen_stamp")


class PenDown(StatementBlock):
    def __init__(self):
        self.define("pen_penDown")


class PenUp(StatementBlock):
    def __init__(self):
        self.define("pen_penUp")


class SetPenColor(StatementBlock):
    def __init__(self, color: InputType):
        self.define("pen_setPenColorToColor", inputs={"COLOR": color})


class ChangePenColorParam(StatementBlock):
    def __init__(self, param: str, change: InputType):
        self.define(
            "pen_changePenColorParamBy", inputs={"COLOR_PARAM": param, "VALUE": change}
        )


class SetPenColorParam(StatementBlock):
    def __init__(self, param: str, value: InputType):
        self.define(
            "pen_setPenColorParamTo", inputs={"COLOR_PARAM": param, "VALUE": value}
        )


class ChangePenSize(StatementBlock):
    def __init__(self, change: InputType):
        self.define("pen_changePenSizeBy", inputs={"SIZE": change})


class SetPenSize(StatementBlock):
    def __init__(self, size: InputType):
        self.define("pen_setPenSizeTo", inputs={"SIZE": size})


def ChangePenColor(change: InputType):
    return ChangePenColorParam("color", change)


def ChangePenSaturation(change: InputType):
    return ChangePenColorParam("saturation", change)


def ChangePenBrightness(change: InputType):
    return ChangePenColorParam("brightness", change)


def ChangePenTransparency(change: InputType):
    return ChangePenColorParam("transparency", change)


def SetPenHue(change: InputType):
    return SetPenColorParam("color", change)


def SetPenSaturation(change: InputType):
    return SetPenColorParam("saturation", change)


def SetPenBrightness(change: InputType):
    return SetPenColorParam("brightness", change)


def SetPenTransparency(change: InputType):
    return SetPenColorParam("transparency", change)
