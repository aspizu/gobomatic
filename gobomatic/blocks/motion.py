from ..primitives import StatementBlock, ReporterBlock, InputType


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


def GotoMousePointer() -> StatementBlock:
    return GotoSprite("_mouse_")


def GotoRandomPosition() -> StatementBlock:
    return GotoSprite("_random_")


class Goto(StatementBlock):
    def __init__(self, x: InputType, y: InputType):
        self.define("motion_gotoxy", inputs={"X": x, "Y": y})


class GlideToSprite(StatementBlock):
    def __init__(self, sprite: InputType, time: InputType):
        self.define("motion_glideto", inputs={"SECS": time, "TO": sprite})


def GlideToMousePointer(time: InputType) -> StatementBlock:
    return GlideToSprite("_mouse_", time)


def GlideToRandomPosition(time: InputType) -> StatementBlock:
    return GlideToSprite("_random_", time)


class Glide(StatementBlock):
    def __init__(self, x: InputType, y: InputType, time: InputType):
        self.define("motion_glidesecstoxy", inputs={"SECS": time, "X": x, "Y": y})


class Point(StatementBlock):
    def __init__(self, direction: InputType):
        self.define("motion_pointindirection", inputs={"DIRECTION": direction})


class PointTowards(StatementBlock):
    def __init__(self, sprite: InputType):
        self.define("motion_pointtowards", inputs={"TOWARDS": sprite})


def PointTowardsMousePointer() -> StatementBlock:
    return PointTowards("_mouse_")


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
        self.define("motion_setrotationstyle", fields={"STYLE": style})


def SetRotationStyleLeftRight() -> StatementBlock:
    return SetRotationStyle("left-right")


def SetRotationStyleAllAround() -> StatementBlock:
    return SetRotationStyle("all around")


def SetRotationStyleDontRotate() -> StatementBlock:
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
