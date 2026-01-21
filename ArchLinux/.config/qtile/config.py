from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import psutil  # installed by pip the psutil dependency
import json


from settings.keys import keys
from settings.groups import groups
from settings.layouts import layouts, floating_layout
from settings.screens import screens
from settings.path import qtile_path
from settings.mouse import mouse
from settings.widgets import widget_defaults, extension_defaults

mod = "mod4"

main = None
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False



# floating_layout = layout.Floating(float_rules=[
#     # Run the utility of `xprop` to see the wm class and name of an X client.
#     *layout.Floating.default_float_rules,
#     Match(wm_class='confirmreset'),  # gitk
#     Match(wm_class='makebranch'),  # gitk
#     Match(wm_class='maketag'),  # gitk
#     Match(wm_class='ssh-askpass'),  # ssh-askpass
#     Match(title='branchdialog'),  # gitk
#     Match(title='pinentry'),  # GPG key password entry
# ])



auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

wmname = "LG3D"


cmd = [
    "setxkbmap latam",
    "feh --bg-fill ~/.config/qtile/images/rick.jpg",
    "picom &"
]

for x in cmd:
    os.system(x)

