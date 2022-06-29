import json
from typing import Any, Union

ValueType = Union[str, int, float, bool]
ValueTypeTuple = (str, int, float, bool)
InputType = Union["ReporterBlock", "Var", "List", ValueType]


def blkid(a) -> str:
    return str(id(a))


def ValueType_to_str(a: ValueType) -> str:
    if isinstance(a, str):
        return repr(a)[1:-1]
    elif isinstance(a, (int, float)):
        return str(a)
    elif isinstance(a, bool):
        return "1" if a else "0"


class Var:
    def __init__(self, name: str, value: ValueType = 0):
        self.id = blkid(self)
        self.name: str = name
        self.value: str = ValueType_to_str(value)

    def set(self, value: InputType):
        from .blocks.otherblocks import SetVariable

        return SetVariable(self, value)

    def change(self, change: InputType):
        from .blocks.otherblocks import ChangeVariable

        return ChangeVariable(self, change)

    def show(self):
        from .blocks.otherblocks import ShowVariable

        return ShowVariable(self)

    def hide(self):
        from .blocks.otherblocks import HideVariable

        return HideVariable(self)

    def __add__(self, o: InputType):
        from .blocks.operator import Add

        return Add(self, o)

    def __sub__(self, o: InputType):
        from .blocks.operator import Sub

        return Sub(self, o)

    def __mul__(self, o: InputType):
        from .blocks.operator import Mul

        return Mul(self, o)

    def __truediv__(self, o: InputType):
        from .blocks.operator import Div

        return Div(self, o)

    def __eq__(self, o):
        if not isinstance(o, InputTypeTuple):
            raise NotImplementedError
        from .blocks.operator import Eq

        return Eq(self, o)

    def __lt__(self, o: InputType):
        from .blocks.operator import Lt

        return Lt(self, o)

    def __gt__(self, o: InputType):
        from .blocks.operator import Gt

        return Gt(self, o)


class List:
    def __init__(self, name: str, values: list[ValueType] = None):
        self.id = blkid(self)
        self.name: str = name
        self.values: list[str] = [ValueType_to_str(a) for a in values or []]

    def add(self, item: InputType):
        from .blocks.otherblocks import AddToList

        return AddToList(self, item)

    def delete(self, index: InputType):
        from .blocks.otherblocks import DeleteOfList

        return DeleteOfList(self, index)

    def index(self, item: InputType):
        from .blocks.otherblocks import IndexOfList

        return IndexOfList(self, item)

    def delete_all(self):
        from .blocks.otherblocks import DeleteAllOfList

        return DeleteAllOfList(self)

    def insert(self, index: InputType, item: InputType):
        from .blocks.otherblocks import InsertAtList

        return InsertAtList(self, index, item)

    def replace(self, index: InputType, item: InputType):
        from .blocks.otherblocks import ReplaceItemOfList

        return ReplaceItemOfList(self, index, item)

    def length(self):
        from .blocks.otherblocks import LengthOfList

        return LengthOfList(self)

    def contains(self, item: InputType):
        from .blocks.otherblocks import ListContainsItem

        return ListContainsItem(self, item)

    def show(self):
        from .blocks.otherblocks import ShowList

        return ShowList(self)

    def hide(self):
        from .blocks.otherblocks import HideList

        return HideList(self)

    def __getitem__(self, index: InputType):
        from .blocks.otherblocks import ItemOfList

        return ItemOfList(self, index)


class Block:
    @staticmethod
    def serialize_inputs(inputs: dict[str, Any]) -> dict:
        ret = {}
        for key, value in inputs.items():
            if isinstance(value, ValueType):  # type: ignore
                ret[key] = [1, [10, ValueType_to_str(value)]]
            elif isinstance(value, ReporterBlock):
                ret[key] = [3, value.id]
            elif isinstance(value, Stack):
                ret[key] = [2, value[0].id]
            elif isinstance(value, Var):
                ret[key] = [3, [12, value.name, value.id]]
            elif isinstance(value, List):
                ret[key] = [3, [12, value.name, value.id]]  # FIXME
            elif isinstance(value, ProcPrototype):
                ret[key] = [1, value.id]
            else:
                ret[key] = value
        return ret

    @staticmethod
    def serialize_fields(fields: dict[str, Any]) -> dict:
        ret = {}
        for key, value in fields.items():
            if isinstance(value, str):
                ret[key] = [value, None]
            elif isinstance(value, (Var, List)):
                ret[key] = [value.name, value.id]
            else:
                ret[key] = value
        return ret

    def define(
        self,
        opcode: str,
        inputs: dict[str, Any] = None,
        fields: dict[str, Any] = None,
    ):
        self.id = blkid(self)
        self.opcode: str = opcode
        self.inputs: dict[str, Any] = inputs or {}
        self.fields: dict[str, Any] = fields or {}

    def serialize(self, next_id: str = None, parent_id: str = None):
        return [
            {
                "id": blkid(self),
                "opcode": self.opcode,
                "next": next_id,
                "parent": parent_id,
                "inputs": Block.serialize_inputs(self.inputs),
                "fields": Block.serialize_fields(self.fields),
                "topLevel": isinstance(self, HatBlock),
            },
            [
                block.serialize(parent_id=self.id)
                for block in self.inputs.values()
                if isinstance(block, (Block, Stack)) and not isinstance(block, ProcPrototype)
            ],
        ]


class Stack(list):
    def serialize(self, parent_id):
        return [
            block.serialize(
                next_id=self[i + 1].id if i < len(self) - 1 else None,
                parent_id=self[i - 1].id if 0 < i else parent_id,
            )
            for i, block in enumerate(self)
        ]


class StatementBlock(Block):
    ...


class HatBlock(Block):
    def __call__(self, *stack: StatementBlock):
        self.stack: Stack = Stack(stack)
        return self

    def serialize(self):
        ret = super().serialize()
        ret[0]["next"] = self.stack[0].id
        ret.append(self.stack.serialize(self.id))
        return ret


class ReporterBlock(Block):
    def __add__(self, o: InputType):
        from .blocks.operator import Add

        return Add(self, o)

    def __sub__(self, o: InputType):
        from .blocks.operator import Sub

        return Sub(self, o)

    def __mul__(self, o: InputType):
        from .blocks.operator import Mul

        return Mul(self, o)

    def __truediv__(self, o: InputType):
        from .blocks.operator import Div

        return Div(self, o)

    def __eq__(self, o):
        if not isinstance(o, InputType):  # type: ignore
            raise NotImplementedError
        from .blocks.operator import Eq

        return Eq(self, o)

    def __lt__(self, o: InputType):
        from .blocks.operator import Lt

        return Lt(self, o)

    def __gt__(self, o: InputType):
        from .blocks.operator import Gt

        return Gt(self, o)


class BooleanReporterBlock(ReporterBlock):
    ...


class ArgReporter(ReporterBlock):
    def __init__(self, name: str):
        self.name: str = name
        self.define("argument_reporter_string_number", fields={"VALUE": name})


class ArgFactory:
    def __getattribute__(self, name: str) -> ArgReporter:
        return ArgReporter(name)


Arg = ArgFactory()


def genproccode(name: str, args: tuple[ArgReporter, ...]) -> str:
    return name + " " + " ".join(["%s"] * len(args))


class ProcPrototype(Block):
    def __init__(self, proccode: str, args: list[str]):
        self.proccode = proccode
        self.args = args
        self.define("procedures_prototype", inputs={arg: [1, arg] for arg in self.args})

    def serialize(self):
        ret = super().serialize()
        ret[0]["mutation"] = {
            "tagName": "mutation",
            "children": [],
            "proccode": self.proccode,
            "argumentids": json.dumps(self.args),  # FIXME
            "argumentnames": json.dumps(self.args),  # FIXME
            "warp": "true",
        }
        return ret


class ProcDefinition(HatBlock):
    def __init__(self, prototype: ProcPrototype):
        self.define("procedures_definition", inputs={"custom_block": prototype})


class ProcCall(StatementBlock):
    def __init__(self, prototype: ProcPrototype, args: tuple[InputType, ...]):
        self.prototype = prototype
        self.define(
            "procedures_call",
            inputs={arg: args[i] for i, arg in enumerate(prototype.args)},
        )

    def serialize(self, next_id: str = None, parent_id: str = None):
        ret = super().serialize(next_id, parent_id)
        ret[0]["mutation"] = {
            "tagName": "mutation",
            "children": [],
            "proccode": self.prototype.proccode,
            "argumentids": json.dumps(self.prototype.args),
            "warp": "true",
        }
        return ret


InputTypeTuple = (ReporterBlock, Var, List, *ValueTypeTuple)
