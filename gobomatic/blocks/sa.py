from ..primitives import ProcCall, ProcPrototype, StatementBlock, InputType

PROTOTYPE_Breakpoint = ProcPrototype("\u200b\u200bbreakpoint\u200b\u200b", [])
PROTOTYPE_Log = ProcPrototype("\u200b\u200blog\u200b\u200b %s", ["arg0"])
PROTOTYPE_Warn = ProcPrototype("\u200b\u200bwarn\u200b\u200b %s", ["arg0"])
PROTOTYPE_Error = ProcPrototype("\u200b\u200berror\u200b\u200b %s", ["arg0"])


def SA_Breakpoint() -> StatementBlock:
    return ProcCall(PROTOTYPE_Breakpoint, ())


def SA_Log(message: InputType) -> StatementBlock:
    return ProcCall(PROTOTYPE_Log, (message,))


def SA_Warn(message: InputType) -> StatementBlock:
    return ProcCall(PROTOTYPE_Warn, (message,))


def SA_Error(message: InputType) -> StatementBlock:
    return ProcCall(PROTOTYPE_Error, (message,))
