from ..primitives import Stack, StatementBlock, BooleanReporterBlock, InputType


class If(StatementBlock):
    def __init__(self, condition: BooleanReporterBlock):
        self.define("control_if", inputs={"CONDITION": condition})

    def __call__(self, *stack: StatementBlock):
        self.inputs["SUBSTACK"] = Stack(stack)
        return self

    def Else(self, *stack: StatementBlock):
        self.opcode = "control_if_else"
        self.inputs["SUBSTACK2"] = Stack(stack)
        return self


class Until(StatementBlock):
    def __init__(self, condition: BooleanReporterBlock):
        self.define("control_repeat_until", inputs={"CONDITION": condition})

    def __call__(self, *stack: StatementBlock):
        self.inputs["SUBSTACK"] = Stack(stack)
        return self


class Repeat(StatementBlock):
    def __init__(self, times: InputType):
        self.define("control_repeat", inputs={"TIMES": times})

    def __call__(self, *stack: StatementBlock):
        self.inputs["SUBSTACK"] = Stack(stack)
        return self


class Forever(StatementBlock):
    def __init__(self, *stack: StatementBlock):
        self.define("control_forever", inputs={"SUBSTACK": Stack(stack)})
