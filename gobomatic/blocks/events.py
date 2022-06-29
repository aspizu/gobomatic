from ..primitives import HatBlock, StatementBlock, InputType


class WhenFlagClicked(HatBlock):
    def __init__(self, stack: tuple[StatementBlock, ...]):
        self.define("event_whenflagclicked")
        self(*stack)


class WhenKeyPressed(HatBlock):
    def __init__(self, key: str):
        self.define("event_whenkeypressed", fields={"KEY_OPTION": key})


class WhenThisSpriteClicked(HatBlock):
    def __init__(self, stack: tuple[StatementBlock, ...]):
        self.define("event_whenthisspriteclicked")
        self(*stack)


class WhenBackdropSwitchesTo(HatBlock):
    def __init__(self, backdrop: str):
        self.define("event_whenbackdropswitchesto", fields={"BACKDROP": backdrop})


class WhenGreaterThan(HatBlock):
    def __init__(self, menu: str, value: InputType):
        self.define(
            "event_whengreaterthan",
            inputs={"VALUE": value},
            fields={"WHENGREATERTHANMENU": menu},
        )


def WhenLoudnessGreaterThan(loudness: InputType):
    return WhenGreaterThan("LOUDNESS", loudness)


def WhenTimerGreaterThan(time: InputType):
    return WhenGreaterThan("TIMER", time)


class WhenReceived(HatBlock):
    def __init__(self, event: str):
        self.define(
            "event_whenbroadcastreceived",
            fields={"BROADCAST_OPTION": [event, event]},
        )
