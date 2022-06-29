from ..primitives import (
    Var,
    List,
    StatementBlock,
    ReporterBlock,
    BooleanReporterBlock,
    InputType,
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
    def __init__(self, condition: BooleanReporterBlock):
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


class SetVariable(StatementBlock):
    def __init__(self, variable: Var, value: InputType):
        self.define(
            "data_setvariableto",
            inputs={"VALUE": value},
            fields={"VARIABLE": variable},
        )


class ChangeVariable(StatementBlock):
    def __init__(self, variable: Var, change: InputType):
        self.define(
            "data_changevariableby",
            inputs={"VALUE": change},
            fields={"VARIABLE": variable},
        )


class ShowVariable(StatementBlock):
    def __init__(self, variable: Var):
        self.define("data_showvariable", fields={"VARIABLE": variable})


class HideVariable(StatementBlock):
    def __init__(self, variable: Var):
        self.define("data_hidevariable", fields={"VARIABLE": variable})


class AddToList(StatementBlock):
    def __init__(self, lst: List, item: InputType):
        self.define(
            "data_addtolist",
            inputs={"ITEM": item},
            fields={"LIST": lst},
        )


class DeleteOfList(StatementBlock):
    def __init__(self, lst: List, index: InputType):
        self.define("data_deleteoflist", inputs={"INDEX": index}, fields={"LIST": lst})


class DeleteAllOfList(StatementBlock):
    def __init__(self, lst: List):
        self.define("data_deletealloflist", fields={"LIST": lst})


class InsertAtList(StatementBlock):
    def __init__(self, lst: List, index: InputType, item: InputType):
        self.define(
            "data_insertatlist",
            inputs={"INDEX": index, "ITEM": item},
            fields={"LIST": lst},
        )


class ReplaceItemOfList(StatementBlock):
    def __init__(self, lst: List, index: InputType, item: InputType):
        self.define(
            "data_replaceitemoflist",
            inputs={"INDEX": index, "ITEM": item},
            fields={"LIST": lst},
        )


class ShowList(StatementBlock):
    def __init__(self, lst: List):
        self.define("data_showlist", fields={"LIST": lst})


class HideList(StatementBlock):
    def __init__(self, lst: List):
        self.define("data_hidelist", fields={"LIST": lst})


class ItemOfList(ReporterBlock):
    def __init__(self, lst: List, index: InputType):
        self.define("data_itemoflist", inputs={"INDEX": index}, fields={"LIST": lst})


class IndexOfList(ReporterBlock):
    def __init__(self, lst: List, item: InputType):
        self.define("data_itemnumoflist", inputs={"ITEM": item}, fields={"LIST": lst})


class LengthOfList(ReporterBlock):
    def __init__(self, lst: List):
        self.define("data_lengthoflist", fields={"LIST": lst})


class ListContainsItem(ReporterBlock):
    def __init__(self, lst: List, item: InputType):
        self.define(
            "data_listcontainsitem",
            inputs={"ITEM": item},
            fields={"LIST": lst},
        )
