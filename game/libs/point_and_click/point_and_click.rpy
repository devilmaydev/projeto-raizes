########## DEVIL SPIδεR'S POINT'n'CLICK PLUGIN ##########
# This plugin implements a modular point'n'click feature to make gameplay more interactive
# Currently supported features:
#   - Conditional interaction - make interactions available only when a certain condition is met
#   - Perspective switching - make segments take place in multiple rooms or angles
#   - Multiple ways to start or end one point'n'click segment - it's all a matter of jumping in and out of the segment

## Parameters ##
# There are numerous occasions where I list out a format for parameters. If the argument is in quotation marks in the format (like "this")
# the argument should also be in quotation marks

## Images ##
# There should an arbitrary amount of image pairs in game/images/point_and_click:
# the pair should consist of images in the filename format of X_idle.png and X_hover.png, where X is a word or a phrase
# this will be needed later in the plugin.

# This is the code that renders the point'n'click elements to the player

# To see steps necessary outside the PnC segments that initialize them, see the demo game's script.rpy file
# If you don't have the demo script, the rundown is that you have to set the current_room variable correctly and start the segment like this:
#   $ current_room = "example" # this value can be changed
#   jump pnc_loop

init -3:
    default current_room = None # This variable controls what list to get buttons from
    default pnc_flags = {} # This variable controls various creator-defined flags that control the state of a given point'n'click segment

screen pnc_screen(room="left"):

    style_prefix "pnc"

    for i in eval(f"{room}_buttons"):
        if (i[3] is None) or (eval(i[3])):
            if isinstance(i[0], (tuple, list)):
                imagebutton idle i[0][0] hover i[0][1] pos i[1] action Return(i[2])
            else:
                imagebutton auto "images/point_and_click/" + str(i[0]) + "_%s.png" pos i[1] action Return(i[2])

style pnc_image_button:
    anchor (0.5, 0.5)

define diss = {"screens" : Dissolve(0.15)} # this allows the textbox to be hidden and shown without any pause

# Demo rooms (plugin example only; replace with real backgrounds if you use left/right_buttons).
image room_left = Solid("#2a2a3a")
image room_right = Solid("#3a2a2a")


# This label handles showing the screen to the player.
label pnc_loop:
    $ quick_menu = False
    window hide diss
    call screen pnc_screen(current_room)
    window show diss
    $ quick_menu = True
    jump expression _return

### INTERACTION LISTS ###
# The plugin supports creation of an unlimited amount of so-called interaction lists, which are Python lists of tuples of a given format:
# (("image_name"),(x_coordinate, y_coordinate),"label_name", condition),
# - image_name represents a string that will determine the button's appearance. To demonstrate with an example, if this parameter was "dog",
# then the plug-in expects dog_idle.png and dog_hover.png to exist in game/images/point_and_click.
# - x_coordinate and y_coordinate correspond to the position of the button in the screen, relative to the button's center.
# - label_name represents the label that triggers when that button is pressed.
# - conditions corresponds to either:
# -- a string containing Python expression that determines the button's visibility - it shows when the condition is True
# -- the None value - making the button visible at all times
# The lists should end in _buttons

define left_buttons = [
    (("look"),(530, 430),"left_frame", None),
    (("look"),(1140, 550),"left_door", None),
    (("move"),(1140, 650),"escape", "pnc_flags.get('door_unlocked') == True"), # Condition. The way it's written ensures that the game doesn't throw an error if the "door_unlocked" key isn't in the dictionary
    (("move"),(1720, 540),"to_right", None),
]

define right_buttons = [
    (("look"),(1390, 430), "right_frame", None),
    (("move"),(200, 540), "to_left", None),
]

### POINT'n'CLICK LABELS ###
# Labels within a point'n'click segment almost always end in a jump statement.

label left_frame:
    "An empty frame."
    "Nothing special."
    jump pnc_loop

label right_frame:
    "An empty frame."
    "Nothing special."
    extend " Except for the fact that when you touch it, you hear a click."
    $ pnc_flags["door_unlocked"] = True # this adds a key-value pair into the pnc_flags dictionary.
    jump pnc_loop

label left_door:
    "A door."
    if pnc_flags.get("door_unlocked") == True: # This ensures that the game doesn't throw an error if the value isn't in the dictionary
        "It's unlocked, so there's nothing stopping you from leaving."
    else:
        "It's locked."
    jump pnc_loop # this throws the player out from the point'n'click segment

label escape:
    "You open the door."
    return

# The following is an example of interactions that move the player or change perspective.
# They change the background and set the room variable so that the correct set of buttons is displayed

label to_left:
    window hide diss
    scene room_left with dissolve
    $ current_room = "left"
    jump pnc_loop

label to_right:
    window hide diss
    scene room_right with dissolve
    $ current_room = "right"
    jump pnc_loop
