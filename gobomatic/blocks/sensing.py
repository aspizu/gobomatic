from ..primitives import StatementBlock, ReporterBlock, BooleanReporterBlock, InputType


class Ask(StatementBlock):
    def __init__(self, question: InputType):
        self.define("sensing_askandwait", inputs={"QUESTION": question})


class SetDraggable(StatementBlock):
    def __init__(self):
        self.define("sensing_setdragmode", fields={"DRAG_MODE": "draggable"})


class SetNotDraggable(StatementBlock):
    def __init__(self):
        self.define("sensing_setdragmode", fields={"DRAG_MODE": "not draggable"})


class ResetTimer(StatementBlock):
    def __init__(self):
        self.define("sensing_resettimer")


class Touching(BooleanReporterBlock):
    def __init__(self, sprite: InputType):
        self.define("sensing_touchingobject", inputs={"TOUCHINGOBJECTMENU": sprite})


def TouchingMousePointer() -> BooleanReporterBlock:
    return Touching("_mouse_")


def TouchingEdge() -> BooleanReporterBlock:
    return Touching("_edge_")


class TouchingColor(BooleanReporterBlock):
    def __init__(self, color: InputType):
        self.define("sensing_touchingcolor", inputs={"COLOR": color})


class ColorTouchingColor(BooleanReporterBlock):
    def __init__(self, color1: InputType, color2: InputType):
        self.define(
            "sensing_coloristouchingcolor",
            inputs={"COLOR": color1, "COLOR2": color2},
        )


class DistanceTo(ReporterBlock):
    def __init__(self, sprite: InputType):
        self.define("sensing_distanceto", inputs={"DISTANCETOMENU": sprite})


def DistanceToMousePointer():
    return DistanceTo("_mouse_")


class Answer(ReporterBlock):
    def __init__(self):
        self.define("sensing_answer")


class KeyPressed(BooleanReporterBlock):
    def __init__(self, key: InputType):
        self.define("sensing_keypressed", inputs={"KEY_OPTION": key})


class MouseDown(BooleanReporterBlock):
    def __init__(self):
        self.define("sensing_mousedown")


class MouseX(ReporterBlock):
    def __init__(self):
        self.define("sensing_mousex")


class MouseY(ReporterBlock):
    def __init__(self):
        self.define("sensing_mousey")


class Loudness(ReporterBlock):
    def __init__(self):
        self.define("sensing_loudness")


class Timer(ReporterBlock):
    def __init__(self):
        self.define("sensing_timer")


class Current(ReporterBlock):
    def __init__(self, time_property: str):
        self.define("sensing_current", fields={"CURRENTMENU": time_property})


def CurrentYear() -> ReporterBlock:
    return Current("YEAR")


def CurrentMonth() -> ReporterBlock:
    return Current("MONTH")


def CurrentDate() -> ReporterBlock:
    return Current("DATE")


def CurrentDayofweek() -> ReporterBlock:
    return Current("DAYOFWEEK")


def CurrentHour() -> ReporterBlock:
    return Current("HOUR")


def CurrentMinute() -> ReporterBlock:
    return Current("MINUTE")


def CurrentSecond() -> ReporterBlock:
    return Current("SECOND")


class DaysSince2000(ReporterBlock):
    def __init__(self):
        self.define("sensing_dayssince2000")


class Username(ReporterBlock):
    def __init__(self):
        self.define("sensing_username")
