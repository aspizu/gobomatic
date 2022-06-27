from typing import Union
from . import code
import json


def serialize_block_inputs(inputs):
    ret = {}
    for input_name, input_value in inputs.items():
        if isinstance(input_value, ReporterBlock):
            ret[input_name] = [3, str(id(input_value))]
        elif isinstance(input_value, ProcedurePrototype):
            ret[input_name] = [1, str(id(input_value))]
        elif isinstance(input_value, StatementStack):
            ret[input_name] = [2, str(id(input_value.stack[0]))]
        elif isinstance(input_value, Var):
            ret[input_name] = [3, [12, input_value.name, str(id(input_value))]]
        elif isinstance(input_value, (str, int, float, bool)):
            ret[input_name] = [1, [10, str(input_value)]]
    return ret


class HatBlock:
    def define(self, opcode, inputs, fields):
        self.opcode = opcode
        self.inputs = inputs
        self.fields = fields

    def __call__(self, *stack):
        self.stack = StatementStack(stack)
        return self

    def serialize(self):
        return [
            {
                "id": str(id(self)),
                "opcode": self.opcode,
                "next": str(id(self.stack.stack[0]))
                if len(self.stack.stack) > 0
                else None,
                "parent": None,
                "inputs": serialize_block_inputs(self.inputs),
                "fields": self.fields,
                "shadow": False,
                "topLevel": True,
                "x": 0,
                "y": 0,
            },
            self.stack.serialize(str(id(self))),
        ]


class Block:
    def define(self, opcode, inputs={}, fields={}):
        self.opcode = opcode
        self.inputs = inputs
        self.fields = fields


class StatementStack:
    def __init__(self, stack):
        self.stack = stack

    def serialize(self, parent_id):
        ret = []

        for i, code in enumerate(self.stack):
            if i == 0:
                ret.append(
                    self.stack[0].serialize(
                        str(id(self.stack[1])) if len(self.stack) > 1 else None,
                        parent_id,
                    )
                )
                continue
            if i == len(self.stack) - 1:
                ret.append(self.stack[-1].serialize(None, str(id(self.stack[-2]))))
                continue
            ret.append(
                code.serialize(str(id(self.stack[i + 1])), str(id(self.stack[i - 1])))
            )

        return ret


class StatementBlock(Block):
    def serialize(self, next_id, parent_id):
        return [
            {
                "id": str(id(self)),
                "opcode": self.opcode,
                "next": next_id,
                "parent": parent_id,
                "inputs": serialize_block_inputs(self.inputs),
                "fields": self.fields,
                "shadow": False,
                "topLevel": False,
            },
            [
                i.serialize(str(id(self)))
                for i in self.inputs.values()
                if isinstance(i, (ReporterBlock, StatementStack))
            ],
        ]


class ReporterBlock(Block):
    def serialize(self, parent_id):
        return [
            {
                "id": str(id(self)),
                "opcode": self.opcode,
                "next": None,
                "parent": parent_id,
                "inputs": serialize_block_inputs(self.inputs),
                "fields": self.fields,
                "shadow": False,
                "topLevel": False,
            },
            [
                i.serialize(str(id(self)))
                for i in self.inputs.values()
                if isinstance(i, ReporterBlock)
            ],
        ]

    def __eq__(self, o):
        return code.Eq(self, o)

    def __lt__(self, o):
        return code.Lt(self, o)

    def __gt__(self, o):
        return code.Gt(self, o)

    def __add__(self, o):
        return code.Add(self, o)

    def __sub__(self, o):
        return code.Sub(self, o)

    def __mul__(self, o):
        return code.Mul(self, o)

    def __truediv__(self, o):
        return code.Div(self, o)


InputType = Union[ReporterBlock, "Var", str, int, float, bool]
BooleanType = Union[
    "code.Not",
    "code.Eq",
    "code.Gt",
    "code.Lt",
    "code.ListContainsItem",
    "code.ColorTouchingColor",
    "code.Touching",
]


class Var:
    def __init__(self, name: str = None):
        self.name: str = str(id(self)) if name is None else name

    def __eq__(self, o):
        return code.Eq(self, o)

    def __lt__(self, o):
        return code.Lt(self, o)

    def __gt__(self, o):
        return code.Gt(self, o)

    def __add__(self, o):
        return code.Add(self, o)

    def __sub__(self, o):
        return code.Sub(self, o)

    def __mul__(self, o):
        return code.Mul(self, o)

    def __truediv__(self, o):
        return code.Div(self, o)

    def change(self, change: InputType):
        return ChangeVariable(self, change)

    def set(self, value: InputType):
        return SetVariable(self, value)

    def __le__(self, o):
        return self.set(o)

    def __ge__(self, o):
        return self.change(o)

    def show(self):
        return ShowVariable(self)

    def hide(self):
        return HideVariable(self)

    def serialize(self, parent_id):
        return []

    def field(self):
        return [self.name, str(id(self))]


class SetVariable(StatementBlock):
    def __init__(self, variable: Var, value: InputType):
        self.define(
            "data_setvariableto",
            inputs={"VALUE": value},
            fields={"VARIABLE": variable.field()},
        )


class ChangeVariable(StatementBlock):
    def __init__(self, variable: Var, change: InputType):
        self.define(
            "data_changevariableby",
            inputs={"VALUE": change},
            fields={"VARIABLE": variable.field()},
        )


class ShowVariable(StatementBlock):
    def __init__(self, variable: Var):
        self.define(
            "data_showvariable",
            fields={"VARIABLE": variable.field()},
        )


class HideVariable(StatementBlock):
    def __init__(self, variable: Var):
        self.define(
            "data_hidevariable",
            fields={"VARIABLE": variable.field()},
        )


class List:
    def __init__(self, name: str = None):
        self.name = str(id(self)) if name is None else name

    def field(self):
        return [self.name, str(id(self))]

    def add(self, item: InputType):
        return AddToList(self, item)

    def delete(self, index: InputType):
        return DeleteOfList(self, index)

    def delete_all(self):
        return DeleteAllOfList(self)

    def insert(self, index: InputType, item: InputType):
        return InsertAtList(self, index, item)

    def replace(self, index: InputType, item: InputType):
        return ReplaceItemOfList(self, index, item)

    def show(self):
        return ShowList(self)

    def hide(self):
        return HideList(self)

    def __getitem__(self, index):
        return ItemOfList(self, index)

    def index(self, item: InputType):
        return IndexOfList(self, item)

    def length(self):
        return LengthOfList(self)

    def contains(self, item: InputType):
        return ListContainsItem(self, item)


class AddToList(StatementBlock):
    def __init__(self, list_: List, item: InputType):
        self.define(
            "data_addtolist",
            inputs={"ITEM": item},
            fields={"LIST": list_.field()},
        )


class DeleteOfList(StatementBlock):
    def __init__(self, list_: List, index: InputType):
        self.define(
            "data_deleteoflist", inputs={"INDEX": index}, fields={"LIST": list_.field()}
        )


class DeleteAllOfList(StatementBlock):
    def __init__(self, list_: List):
        self.define("data_deletealloflist", fields={"LIST": list_.field()})


class InsertAtList(StatementBlock):
    def __init__(self, list_: List, index: InputType, item: InputType):
        self.define(
            "data_deleteoflist",
            inputs={"INDEX": index, "ITEM": item},
            fields={"LIST": list_.field()},
        )


class ReplaceItemOfList(StatementBlock):
    def __init__(self, list_: List, index: InputType, item: InputType):
        self.define(
            "data_replaceitemoflist",
            inputs={"INDEX": index, "ITEM": item},
            fields={"LIST": list_.field()},
        )


class ShowList(StatementBlock):
    def __init__(self, list_: List):
        self.define("data_showlist", fields={"LIST": list_.field()})


class HideList(StatementBlock):
    def __init__(self, list_: List):
        self.define("data_hidelist", fields={"LIST": list_.field()})


class ItemOfList(ReporterBlock):
    def __init__(self, list_: List, index: InputType):
        self.define(
            "data_itemoflist", inputs={"INDEX": index}, fields={"LIST": list_.field()}
        )


class IndexOfList(ReporterBlock):
    def __init__(self, list_: List, item: InputType):
        self.define(
            "data_itemnumoflist", inputs={"ITEM": item}, fields={"LIST": list_.field()}
        )


class LengthOfList(ReporterBlock):
    def __init__(self, list_: List):
        self.define("data_lengthoflist", fields={"LIST": list_.field()})


class ListContainsItem(ReporterBlock):
    def __init__(self, list_: List, item: InputType):
        self.define(
            "data_listcontainsitem",
            inputs={"ITEM": item},
            fields={"LIST": list_.field()},
        )


class ArgReporter(ReporterBlock):
    def __init__(self, name: str):
        self.name = name
        self.define("argument_reporter_string_number", fields={"VALUE": [name, None]})


class ArgFactory:
    def __getattribute__(self, name):
        return ArgReporter(name)


Arg = ArgFactory()


class ProcedurePrototype:
    def __init__(self, proccode: str, args: list[str]):
        self.proccode = proccode
        self.args = args

    def serialize(self):
        return {
            "id": str(id(self)),
            "opcode": "procedures_prototype",
            "next": None,
            "parent": None,
            "inputs": {
                "ArgReporter:" + argname: [1, "ArgReporter:" + argname]
                for argname in self.args
            },
            "fields": {},
            "topLevel": False,
            "mutation": {
                "tagName": "mutation",
                "children": [],
                "proccode": self.proccode,
                "argumentids": json.dumps(
                    ["ArgReporter:" + argname for argname in self.args]
                ),
                "argumentnames": json.dumps(self.args),
                "argumentdefaults": json.dumps(self.args),
                "warp": "true",
            },
        }


class ProcedureDefinition(HatBlock):
    def __init__(self, prototype: ProcedurePrototype):
        self.define(
            "procedures_definition", inputs={"custom_block": prototype}, fields={}
        )


class ProcedureCall(StatementBlock):
    def __init__(self, prototype: ProcedurePrototype, args: list[InputType]):
        self.prototype = prototype
        self.define(
            "procedures_call",
            inputs={
                "ArgReporter:" + argname: args[i]
                for i, argname in enumerate(prototype.args)
            },
        )

    def serialize(self, next_id, parent_id):
        ret = super().serialize(next_id, parent_id)
        ret[0]["mutation"] = {
            "tagName": "mutation",
            "children": [],
            "proccode": self.prototype.proccode,
            "argumentids": json.dumps(
                ["ArgReporter:" + argname for argname in self.prototype.args]
            ),
            "warp": "true",
        }
        return ret


def gen_proccode(name: str, args: tuple[ArgReporter, ...]) -> str:
    return name + " " + " ".join(["%s"] * len(args))
