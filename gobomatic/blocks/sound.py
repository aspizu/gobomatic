from ..primitives import StatementBlock, ReporterBlock, InputType


class PlaySoundUntilDone(StatementBlock):
    def __init__(self, sound: InputType):
        self.define("sound_playuntildone", inputs={"SOUND_MENU": sound})


class StartSound(StatementBlock):
    def __init__(self, sound: InputType):
        self.define("sound_play", inputs={"SOUND_MENU": sound})


class StopAllSounds(StatementBlock):
    def __init__(self):
        self.define("sound_stopallsounds")


class SetSoundEffect(StatementBlock):
    def __init__(self, effect: str, value: InputType):
        self.define(
            "sound_seteffectto",
            inputs={"VALUE": value},
            fields={"EFFECT": effect},
        )


class ChangeSoundEffect(StatementBlock):
    def __init__(self, effect: str, value: InputType):
        self.define(
            "sound_changeeffectby",
            inputs={"VALUE": value},
            fields={"EFFECT": effect},
        )


def SetPitchEffect(value: InputType) -> StatementBlock:
    return SetSoundEffect("PITCH", value)


def ChangePitchEffect(value: InputType) -> StatementBlock:
    return ChangeSoundEffect("PITCH", value)


def SetPanEffect(value: InputType) -> StatementBlock:
    return SetSoundEffect("PAN", value)


def ChangePanEffect(value: InputType) -> StatementBlock:
    return ChangeSoundEffect("PAN", value)


class ClearSoundEffects(StatementBlock):
    def __init__(self):
        self.define("sound_cleareffects")


class ChangeVolume(StatementBlock):
    def __init__(self, change: InputType):
        self.define("sound_changevolumeby", inputs={"VOLUME": change})


class SetVolume(StatementBlock):
    def __init__(self, volume: InputType):
        self.define("sound_setvolumeto", inputs={"VOLUME": volume})


class Volume(ReporterBlock):
    def __init__(self):
        self.define("sound_volume")
