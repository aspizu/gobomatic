# fmt: off

from gobomatic import *

Self = Sprite(name=__name__, costumes="assets/*")

# Variables:
# --- for all sprites variables ---
GLOBAL_VARIABLE = Var("GLOBAL_VARIABLE")
# --- for this sprite only variables ---
local_variable = Self.Var("local_variable")
x = Self.Var("x")
y = Self.Var("y")

# Lists:
# --- for all sprites lists ---
GLOBAL_LIST = List("GLOBAL_LIST")
# --- for this sprite only lists ---
local_list = Self.List("local_list")

# Functions:
my_function = Self.Func(Arg.argument1, Arg.argument2, name="my_function")

my_function.Define(
    Say(Arg.argument1),
    Say(Arg.argument2),
    Say(Arg.argument3),
)

Self.WhenFlagClicked(
    my_function(1, 2),
    Move(10),
    TurnRight(15),
    TurnLeft(15),
    GotoMousePointer(),
    GotoRandomPosition(),
    GotoSprite("sprite"),
    Goto(0, 0),
    GlideToMousePointer(1),
    GlideToRandomPosition(1),
    GlideToSprite("sprite", 1),
    Glide(0, 0, 1),
    Point(90),
    PointTowardsMousePointer(),
    PointTowards("sprite"),
    ChangeX(10),
    SetX(10),
    ChangeY(10),
    SetY(10),
    IfOnEdgeBounce(),
    SetRotationStyleLeftRight(),
    SetRotationStyleDontRotate(),
    SetRotationStyleAllAround(),
    Say(XPosition()),
    Say(YPosition()),
    Say(Direction()),
)

Self.WhenFlagClicked(
    SayFor("Hello, World!", 2),
    Say("Hello, World!"),
    ThinkFor("Hmm...", 2),
    Think("Hmm..."),
    SwitchCostume("scratchcat"),
    NextCostume(),
    SwitchBackdrop("blank"),
    NextBackdrop(),
    ChangeSize(10),
    SetSize(100),
    ChangeEffectColor(25),
    ChangeEffectFisheye(25),
    ChangeEffectWhirl(25),
    ChangeEffectPixelate(25),
    ChangeEffectMosaic(25),
    ChangeEffectBrightness(25),
    ChangeEffectGhost(25),
    SetEffectColor(0),
    SetEffectFisheye(0),
    SetEffectWhirl(0),
    SetEffectPixelate(0),
    SetEffectMosaic(0),
    SetEffectBrightness(0),
    SetEffectGhost(0),
    ClearGraphicEffects(),
    Show(),
    Hide(),
    GotoFront(),
    GotoBack(),
    GoForward(1),
    GoBackward(1),
    Say(CostumeNumber()),
    Say(CostumeName()),
    Say(BackdropNumber()),
    Say(BackdropName()),
    Say(Size()),
)

Self.WhenFlagClicked(
    PlaySoundUntilDone("A Bass"),
    StartSound("A Bass"),
    StopAllSounds(),
    ChangePitchEffect(10),
    ChangePanEffect(10),
    ClearSoundEffects(),
    ChangeVolume(-10),
    SetVolume(100),
    Say(Volume()),
)

Self.WhenKeyPressed("space")(
    Say("when [space] key pressed"),
)

Self.WhenThisSpriteClicked(
    Say("when this sprite clicked"),
)

Self.WhenBackdropSwitchesTo("backdrop")(
    Say("when backdrop switches to [backdrop]"),
)

Self.WhenLoudnessGreaterThan(10)(
    Say("when [loudness] > (10)"),
)

Self.WhenTimerGreaterThan(10)(
    Say("when [timer] > (10)"),
)

Self.WhenReceived("message1")(
    Say("when I receive [message1]"),
)

Self.WhenFlagClicked(
    Broadcast("message1"),
    BroadcastAndWait("message1"),
    Wait(1),
    Repeat(10)(
        Say("repeat (10) body"),
    ),
    If(Eq("left", "right"))(
        Forever(
            Say("forever body"),
        ),
    ),
    If(Eq("left", "right"))(
        Say("if else body"),
    ).Else(
        Say("else body"),
    ),
    WaitUntil(Eq("left", "right")),
    Until(Eq("left", "right"))(
        Say("repeat until body"),
    ),
    Repeat(1)(
        StopAll(),
    ),
    Repeat(1)(
        StopThisScript(),
    ),
    Repeat(1)(
        StopOtherScripts(),
    ),
    CreateCloneOfSelf(),
    CreateClone("sprite"),
    DeleteThisClone(),
)

Self.WhenFlagClicked(
    If(TouchingMousePointer())(Say("")),
    If(TouchingEdge())(Say("")),
    If(Touching("sprite"))(Say("")),
    If(TouchingColor("#FF00FF"))(Say("")),
    If(ColorTouchingColor("#FF00FF", "#00FF00"))(Say("")),
    If(KeyPressed("space"))(Say("")),
    If(MouseDown())(Say("")),
    Say(DistanceToMousePointer()),
    Say(DistanceTo("sprite")),
    Ask("Question?"),
    Say(Answer()),
    Say(MouseX()),
    Say(MouseY()),
    SetDraggable(),
    SetNotDraggable(),
    Say(Loudness()),
    Say(Timer()),
    ResetTimer(),
    Say(CurrentYear()),
    Say(CurrentMonth()),
    Say(CurrentDate()),
    Say(CurrentDate()),
    Say(CurrentDayofweek()),
    Say(CurrentHour()),
    Say(CurrentHour()),
    Say(CurrentMinute()),
    Say(CurrentSecond()),
    Say(DaysSince2000()),
    Say(Username()),
)

Self.WhenFlagClicked(
    Say(x + y),
    Say(x - y),
    Say(x * y),
    Say(x / y),
    Say(Random(x, y)),
    If(x > y)(Say("")),
    If(x < y)(Say("")),
    If(x == y)(Say("")),
    If(And(x==y, x==y))(Say("")),
    If(Or(x==y, x==y))(Say("")),
    If(Not(x==y))(Say("")),
    Say(Join(x, y)),
    Say(Letter(x, y)),
    Say(Length(x)),
    Say(Contains(x, y)),
    Say(Mod(x, y)),
    Say(Round(x)),
    Say(Abs(x)),
    Say(Floor(x)),
    Say(Ceiling(x)),
    Say(Sqrt(x)),
    Say(Sin(x)),
    Say(Cos(x)),
    Say(Tan(x)),
    Say(Asin(x)),
    Say(Acos(x)),
    Say(Atan(x)),
    Say(Ln(x)),
    Say(Log(x)),
    Say(AntiLn(x)),
    Say(AntiLog(x)),
)

Self.WhenFlagClicked(
    GLOBAL_VARIABLE <= 0, # Set variable to 0
    GLOBAL_VARIABLE >= 1, # Change variable by 1
    local_variable.show(),
    local_variable.hide(),
    GLOBAL_LIST.add("thing"),
    local_list.delete(1),
    local_list.delete_all(),
    local_list.insert(0, "thing"),
    local_list.replace(0, "thing"),
    local_list.show(),
    local_list.hide(),
    Say(local_list[1]), # item 1 of list
    Say(local_list.index("thing")),
    Say(local_list.length()),
    If(local_list.contains("thing"))(Say("")),
)

Self.WhenFlagClicked(
    # Scratch Addons Debugger Blocks
    SA_Breakpoint(),
    SA_Log("log message"),
    SA_Warn("warn message"),
    SA_Error("error message"),

    # Pen Extension Blocks
    EraseAll(),
    Stamp(),
    PenDown(),
    PenUp(),
    SetPenColor("#FF00FF"),
    ChangePenHue(10),
    ChangePenSaturation(10),
    ChangePenBrightness(10),
    ChangePenTransparency(10),
    SetPenHue(0),
    SetPenSaturation(0),
    SetPenBrightness(0),
    SetPenTransparency(0),
    ChangePenSize(1),
    SetPenSize(1),
)
