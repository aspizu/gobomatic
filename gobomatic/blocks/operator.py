from ..primitives import ReporterBlock, BooleanReporterBlock, InputType


class Add(ReporterBlock):
    def __init__(self, left: InputType, right: InputType):
        self.define("operator_add", inputs={"NUM1": left, "NUM2": right})


class Sub(ReporterBlock):
    def __init__(self, left: InputType, right: InputType):
        self.define("operator_subtract", inputs={"NUM1": left, "NUM2": right})


class Mul(ReporterBlock):
    def __init__(self, left: InputType, right: InputType):
        self.define("operator_multiply", inputs={"NUM1": left, "NUM2": right})


class Div(ReporterBlock):
    def __init__(self, left: InputType, right: InputType):
        self.define("operator_divide", inputs={"NUM1": left, "NUM2": right})


class Random(ReporterBlock):
    def __init__(self, lower: InputType, upper: InputType):
        self.define("operator_random", inputs={"FROM": lower, "TO": upper})


class Gt(BooleanReporterBlock):
    def __init__(self, left: InputType, right: InputType):
        self.define("operator_gt", inputs={"OPERAND1": left, "OPERAND2": right})


class Lt(BooleanReporterBlock):
    def __init__(self, left: InputType, right: InputType):
        self.define("operator_lt", inputs={"OPERAND1": left, "OPERAND2": right})


class Eq(BooleanReporterBlock):
    def __init__(self, left: InputType, right: InputType):
        self.define("operator_equals", inputs={"OPERAND1": left, "OPERAND2": right})


class And(BooleanReporterBlock):
    def __init__(self, left: BooleanReporterBlock, right: BooleanReporterBlock):
        self.define("operator_and", inputs={"OPERAND1": left, "OPERAND2": right})


class Or(BooleanReporterBlock):
    def __init__(self, left: BooleanReporterBlock, right: BooleanReporterBlock):
        self.define("operator_or", inputs={"OPERAND1": left, "OPERAND2": right})


class Not(BooleanReporterBlock):
    def __init__(self, operand: BooleanReporterBlock):
        self.define("operator_not", inputs={"OPERAND": operand})


class Join(ReporterBlock):
    def __init__(self, left: InputType, right: InputType):
        self.define("operator_join", inputs={"STRING1": left, "STRING2": right})


class Letter(ReporterBlock):
    def __init__(self, index: InputType, string: InputType):
        self.define("operator_letter_of", inputs={"LETTER": index, "STRING": string})


class Length(ReporterBlock):
    def __init__(self, string: InputType):
        self.define("operator_length", inputs={"STRING": string})


class Contains(BooleanReporterBlock):
    def __init__(self, string: InputType, substring: InputType):
        self.define(
            "operator_contains", inputs={"STRING1": string, "STRING2": substring}
        )


class Mod(ReporterBlock):
    def __init__(self, left: InputType, right: InputType):
        self.define("operator_mod", inputs={"NUM1": left, "NUM2": right})


class Round(ReporterBlock):
    def __init__(self, operand: InputType):
        self.define("operator_round", inputs={"NUM": operand})


class MathOp(ReporterBlock):
    def __init__(self, operator: str, operand: InputType):
        self.define(
            "operator_mathop",
            inputs={"NUM": operand},
            fields={"OPERATOR": operator},
        )


def Abs(operand: InputType) -> ReporterBlock:
    return MathOp("abs", operand)


def Floor(operand: InputType) -> ReporterBlock:
    return MathOp("floor", operand)


def Ceiling(operand: InputType) -> ReporterBlock:
    return MathOp("ceiling", operand)


def Sqrt(operand: InputType) -> ReporterBlock:
    return MathOp("sqrt", operand)


def Sin(operand: InputType) -> ReporterBlock:
    return MathOp("sin", operand)


def Cos(operand: InputType) -> ReporterBlock:
    return MathOp("cos", operand)


def Tan(operand: InputType) -> ReporterBlock:
    return MathOp("tan", operand)


def Asin(operand: InputType) -> ReporterBlock:
    return MathOp("asin", operand)


def Acos(operand: InputType) -> ReporterBlock:
    return MathOp("acos", operand)


def Atan(operand: InputType) -> ReporterBlock:
    return MathOp("atan", operand)


def Ln(operand: InputType) -> ReporterBlock:
    return MathOp("ln", operand)


def Log(operand: InputType) -> ReporterBlock:
    return MathOp("log", operand)


def AntiLn(operand: InputType) -> ReporterBlock:
    return MathOp("e ^", operand)


def AntiLog(operand: InputType) -> ReporterBlock:
    return MathOp("10 ^", operand)
