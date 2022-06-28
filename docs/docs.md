# Documentation

### Installing gobomatic

```
pip install gobomatic
```

## Creating the project

Create a project directory to hold the source code.

```
mkdir your-project
touch build.py
```

### Adding the stage sprite and exporting the project

build.py
```py
from gobomatic import *

stage = Sprite("Stage", costumes=["assets/blank.svg"])

Self = Project(sprites=[stage])

Self.export("project.sb3")
```

### Building the project

```
python build.py
```
Will output the project into `project.sb3` as defined.

### Adding all costumes from a directory

You can use a **glob** instead of a list as the costumes parameter to add *all* 
costumes from that directory.

```py
Self = Sprite("sprite-name", costumes="assets/sprite-name/*")
```
This will add all files inside the directory `assets/sprite-name` as costumes.

### Adding a sprite

Create a new file for each sprite.

main.py
```py
from gobomatic import *

Self = Sprite(name=__name__, costumes="assets/*") # __name__ returns "main" here

Self.WhenFlagClicked(
    Say("Hello, World!"),
)
```

Add this sprite to the project in `build.py`

build.py
```py
from main import Self as main
...
Self = Project(sprites=[stage, main])
...
```

## Creating Custom Blocks

Every custom block requires a prototype and definition, the prototype
is separate from the definition to allow for recursion.

```py
function = Self.Func(Arg.argument_name_1, Arg,argument_name_2)

function.Define(
    # code goes here...
)
```
Now you can call `function(arg1, arg2)` anywhere in the code

## Variables and Lists

`var_name = Var()` to create a "for all sprites" variable

`list_name = List()` to create a "for all sprites" list

`var_name = Self.Var()` to create a "for this sprite only" variable

`list_name = Self.List()` to create a "for this sprite only" list

### Shorthands

`var_name <= expression` is a shorthand for `var_name.set(expression)`

`var_name >= expression` is a shorthand for `var_name.change(expression)`
