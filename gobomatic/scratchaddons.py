from .codeprimitives import *

PROTOTYPE_Breakpoint = ProcedurePrototype("\u200b\u200bbreakpoint\u200b\u200b", [])
PROTOTYPE_Log = ProcedurePrototype("\u200b\u200blog\u200b\u200b %s", ["arg0"])
PROTOTYPE_Warn = ProcedurePrototype("\u200b\u200bwarn\u200b\u200b %s", ["arg0"])
PROTOTYPE_Error = ProcedurePrototype("\u200b\u200berror\u200b\u200b %s", ["arg0"])


def SA_Breakpoint() -> StatementBlock:
    return ProcedureCall(PROTOTYPE_Breakpoint, ())


def SA_Log(message: InputType) -> StatementBlock:
    return ProcedureCall(PROTOTYPE_Log, (message,))


def SA_Warn(message: InputType) -> StatementBlock:
    return ProcedureCall(PROTOTYPE_Warn, (message,))


def SA_Error(message: InputType) -> StatementBlock:
    return ProcedureCall(PROTOTYPE_Error, (message,))
