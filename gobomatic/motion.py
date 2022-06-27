from .codeprimitives import *


class Move(StatementBlock):
    def __init__(self, steps: InputType):
        self.define("motion_movesteps", inputs={"STEPS": steps})


class TurnRight(StatementBlock):
    def __init__(self, degrees: InputType):
        self.define("motion_turnright", inputs={"DEGREES": degrees})


class TurnLeft(StatementBlock):
    def __init__(self, degrees: InputType):
        self.define("motion_turnleft", inputs={"DEGREES": degrees})


class GotoSprite(StatementBlock):
    def __init__(self, sprite: InputType):
        self.define("motion_goto", inputs={"TO": sprite})


def GotoMousePointer():
    return GotoSprite("_mouse_")


def GotoRandomPosition():
    return GotoSprite("_random_")


class Goto(StatementBlock):
    def __init__(self, x: InputType, y: InputType):
        self.define("motion_gotoxy", inputs={"X": x, "Y": y})


class Glide(StatementBlock):
    def __init__(self, x: InputType, y: InputType, time: InputType):
        self.define("motion_glidesecstoxy", inputs={"SECS": time, "X": x, "Y": y})


class Point(StatementBlock):
    def __init__(self, direction: InputType):
        self.define("motion_pointindirection", inputs={"DIRECTION": direction})


class ChangeX(StatementBlock):
    def __init__(self, dx: InputType):
        self.define("motion_changexby", inputs={"DX": dx})


class ChangeY(StatementBlock):
    def __init__(self, dy: InputType):
        self.define("motion_changeyby", inputs={"DY": dy})


class SetX(StatementBlock):
    def __init__(self, x: InputType):
        self.define("motion_setx", inputs={"X": x})


class SetY(StatementBlock):
    def __init__(self, y: InputType):
        self.define("motion_sety", inputs={"Y": y})


class IfOnEdgeBounce(StatementBlock):
    def __init__(self):
        self.define("motion_ifonedgebounce")


class SetRotationStyle(StatementBlock):
    def __init__(self, style: str):
        self.define("motion_setrotationstyle", fields={"STYLE": [style, None]})


def SetRotationStyleLeftRight():
    return SetRotationStyle("left-right")


def SetRotationStyleAllAround():
    return SetRotationStyle("all around")


def SetRotationStyleDontRotate():
    return SetRotationStyle("don't rotate")


class XPosition(ReporterBlock):
    def __init__(self):
        self.define("motion_xposition")


class YPosition(ReporterBlock):
    def __init__(self):
        self.define("motion_yposition")


class Direction(ReporterBlock):
    def __init__(self):
        self.define("motion_direction")
