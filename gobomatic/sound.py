from .codeprimitives import *


class PlaySoundUntilDone(StatementBlock):
    def __init__(self, sound: InputType):
        self.define("sound_playuntildone", inputs={"SOUND_MENU": sound})


class StartSound(StatementBlock):
    def __init__(self, sound: InputType):
        self.define("sound_play", inputs={"SOUND_MENU": sound})


class StopAllSounds(StatementBlock):
    def __init__(self):
        self.define("sound_stopallsounds")


class ChangePitchEffect(StatementBlock):
    def __init__(self, change: InputType):
        self.define(
            "sound_changeeffectby",
            inputs={"VALUE": change},
            fields={"EFFECT": ["PITCH", None]},
        )


class ChangePanEffect(StatementBlock):
    def __init__(self, change: InputType):
        self.define(
            "sound_changeeffectby",
            inputs={"VALUE": change},
            fields={"EFFECT": ["PAN", None]},
        )


class SetPitchEffect(StatementBlock):
    def __init__(self, pitch: InputType):
        self.define(
            "sound_seteffectto",
            inputs={"VALUE": pitch},
            fields={"EFFECT": ["PITCH", None]},
        )


class SetPanEffect(StatementBlock):
    def __init__(self, pan: InputType):
        self.define(
            "sound_seteffectto",
            inputs={"VALUE": pan},
            fields={"EFFECT": ["PAN", None]},
        )


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
