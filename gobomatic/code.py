from .codeprimitives import *
from .looks import *
from .motion import *
from .operator import *
from .sensing import *
from .sound import *
from .pen import *
from .scratchaddons import *


class WhenFlagClicked(HatBlock):
    def __init__(self, *stack: StatementBlock):
        self.define("event_whenflagclicked", {}, {})
        self(*stack)


class WhenKeyPressed(HatBlock):
    def __init__(self, key: str):
        self.define("event_whenkeypressed", {}, {"KEY_OPTION": [key, None]})


class WhenThisSpriteClicked(HatBlock):
    def __init__(self, *stack: StatementBlock):
        self.define("event_whenthisspriteclicked", {}, {})
        self(*stack)


class WhenBackdropSwitchesTo(HatBlock):
    def __init__(self, backdrop: str):
        self.define("event_whenbackdropswitchesto", {}, {"BACKDROP": [backdrop, None]})


class WhenGreaterThan(HatBlock):
    def __init__(self, menu: str, value: InputType):
        self.define(
            "event_whengreaterthan",
            inputs={"VALUE": value},
            fields={"WHENGREATERTHANMENU": [menu, None]},
        )


def WhenLoudnessGreaterThan(loudness: InputType):
    return WhenGreaterThan("LOUDNESS", loudness)


def WhenTimerGreaterThan(time: InputType):
    return WhenGreaterThan("TIMER", time)


class WhenReceived(HatBlock):
    def __init__(self, event: str):
        self.define(
            "event_whenbroadcastreceived",
            inputs={},
            fields={"BROADCAST_OPTION": [event, event]},
        )


class Broadcast(StatementBlock):
    def __init__(self, event: InputType):
        self.define("event_broadcast", inputs={"BROADCAST_INPUT": event})


class BroadcastAndWait(StatementBlock):
    def __init__(self, event: InputType):
        self.define("event_broadcastandwait", inputs={"BROADCAST_INPUT": event})


class Wait(StatementBlock):
    def __init__(self, time: InputType):
        self.define("control_wait", inputs={"DURATION": time})


class WaitUntil(StatementBlock):
    def __init__(self, condition: BooleanType):
        self.define("control_wait_until", inputs={"CONDITION": condition})


class CreateClone(StatementBlock):
    def __init__(self, sprite: InputType):
        self.define("control_create_clone_of", inputs={"CLONE_OPTION": sprite})


def CreateCloneOfSelf():
    return CreateClone("_myself_")


class DeleteThisClone(StatementBlock):
    def __init__(self):
        self.define("control_delete_this_clone")


class Stop(StatementBlock):
    def __init__(self, operation: str):
        self.define("control_stop", fields={"STOP_OPTION": [operation, None]})


def StopAll():
    return Stop("all")


def StopThisScript():
    return Stop("this script")


def StopOtherScripts():
    return Stop("other scripts in sprite")


class If(StatementBlock):
    def __init__(self, condition: BooleanType):
        self.define("control_if", inputs={"CONDITION": condition})

    def __call__(self, *if_stack: StatementBlock):
        self.inputs["SUBSTACK"] = StatementStack(if_stack)
        return self

    def Else(self, *else_stack: StatementBlock):
        self.opcode = "control_if_else"
        self.inputs["SUBSTACK2"] = StatementStack(else_stack)
        return self


class Until(StatementBlock):
    def __init__(self, condition: BooleanType):
        self.define("control_repeat_until", inputs={"CONDITION": condition})

    def __call__(self, *stack: StatementBlock):
        self.inputs["SUBSTACK"] = StatementStack(stack)
        return self


class Repeat(StatementBlock):
    def __init__(self, times: InputType):
        self.define("control_repeat", inputs={"TIMES": times})

    def __call__(self, *stack: StatementBlock):
        self.inputs["SUBSTACK"] = StatementStack(stack)
        return self


class Forever(StatementBlock):
    def __init__(self, *stack: StatementBlock):
        self.define("control_forever", inputs={"SUBSTACK": StatementStack(stack)})
