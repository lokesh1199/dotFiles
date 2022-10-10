# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

import os
import subprocess

mod = "mod4"
myTerm = 'alacritty'
home = os.path.expanduser('~')

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(myTerm), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "x", lazy.spawn('systemctl suspend'), desc="lock"),
    Key([mod], "r", lazy.spawn('rofi -show drun'),
        desc="Spawn a command using a prompt widget"),
    Key([mod], "e", lazy.spawn('rofi -show emoji -modi emoji -show-icons'),
        desc='Spawn a rofi emoji selector'),
    # Key([mod], "w", lazy.spawn('rofi -show drun -theme dt -font "SourceCodePro 12" -run-shell-command \'{terminal} -e zsh -ic "{cmd} && read"\''),
    #    desc='Spawn a rofi emoji selector'),
]

functionKeys = {
    'XF86AudioMute': 'pactl set-sink-mute @DEFAULT_SINK@ toggle',
    'XF86AudioLowerVolume': 'pactl set-sink-volume @DEFAULT_SINK@ -1%',
    'XF86AudioRaiseVolume': 'pactl set-sink-volume @DEFAULT_SINK@ +1%',
    'XF86AudioMicMute': 'pactl set-source-mute @DEFAULT_SOURCE@ toggle',
    'XF86MonBrightnessUp': 'xbacklight -inc 1',
    'XF86MonBrightnessDown': 'xbacklight -dec 1',
    'XF86Calculator': f'{myTerm} -e "python"',
    'Print': f'flameshot full -p {home}/Pictures',
    'XF86AudioPlay': 'playerctl play-pause',
    'XF86AudioStop': 'playerctl stop',
    'XF86AudioPrev': 'playerctl previous',
    'XF86AudioNext': 'playerctl next',
}

for functionKey in functionKeys:
    keys.append(Key([], functionKey, lazy.spawn(functionKeys[functionKey])))


groups = ["MAIN", "BROWSE", 'NOTES', 'MUSIC', ]
groups = [Group(i) for i in groups]

for index, group in enumerate(groups):
    keys.extend([
        # mod + number -> switch to that group
        Key([mod], str(index+1), lazy.group[group.name].toscreen(),
            desc="Switch to group {}".format(group.name)),

        # mod + shift + number -> send focussed window and switch to that group
        # If you don't want to switch to that group change switch_group to False
        Key([mod, "shift"], str(index+1), lazy.window.togroup(group.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(group.name)),
    ])

layout_theme = {
    "border_focus": "e1acff",
    "border_normal": "1D2330"
}

layouts = [
    layout.Columns(**layout_theme, margin=2, border_width=2),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


# colors
colors = [
    "#282a36", "#3b4252", "#434c5e", "#4c566a",
    "#8fbcbb", "#88c0d0", "#81a1c1", "#5e81ac",
    "#bf616a", "#d08770", "#ebcb8b", "#a3be8c",
    "#b48ead", "#E288DC"
]

widget_defaults = dict(
    #font='UbuntuMono Nerd Font',
    fontsize=14.5,
    padding=0,
    foreground=colors[0],
)
extension_defaults = widget_defaults.copy()


def space():
    return widget.TextBox("  ")


screens = [
    Screen(
        wallpaper='~/.config/qtile/wall.jpg',
        wallpaper_mode='fill',
        top=bar.Bar(
            [
                widget.TextBox("", foreground=colors[5], fontsize=25, padding=7.2),
                space(),
                widget.GroupBox(
                    background=colors[0],
                    highlight_method="text",
                    active=colors[11],
                    disable_drag=True,
                    rounded=False,
                    this_current_screen_border=colors[9],
                    inactive=colors[5],
                    font="Mononoki",
                    fontsize=14,
                    urgent_alert_method="text",
                    urgent_text=colors[8]
                ),
                space(),
                widget.WindowName(
                    foreground=colors[5],
                ),
                widget.TextBox(
                    text='',
                    font='mononoki Nerd Font',
                    background=colors[0],
                    foreground=colors[5],
                    padding=-7.2,
                    fontsize=58,
                ),
                widget.Systray(
                    padding=12,
                    background=colors[5],
                ),

                widget.TextBox(
                    text='',
                    font='mononoki Nerd Font',
                    background=colors[5],
                    foreground=colors[11],
                    padding=-7.2,
                    fontsize=58,
                ),
                widget.Backlight(
                    padding=12,
                    background=colors[11],
                    backlight_name='amdgpu_bl0',
                    format='Br:  {percent:2.0%}',
                    step=2,
                ),

                widget.TextBox(
                    text='',
                    font='mononoki Nerd Font',
                    background=colors[11],
                    foreground=colors[10],
                    padding=-7.2,
                    fontsize=58,
                ),
                widget.TextBox(
                    " ",
                    font='mononoki Nerd Font',
                    background=colors[10],
                    fontsize=20,
                ),
                widget.PulseVolume(
                    padding=12,
                    background=colors[10],
                    foreground=colors[0],
                    limit_max_volume=True,
                ),
                widget.TextBox(
                    text='',
                    font='mononoki Nerd Font',
                    background=colors[10],
                    foreground=colors[9],
                    padding=-7.2,
                    fontsize=58,
                ),
                widget.Net(
                    interface="wlp1s0",
                    format='{down} ↓↑ {up}',
                    foreground=colors[2],
                    background=colors[9],
                    padding=5
                ),
                widget.TextBox(
                    text='',
                    font='mononoki Nerd Font',
                    background=colors[9],
                    foreground=colors[8],
                    padding=-7.2,
                    fontsize=58
                ),
                widget.Clock(
                    background=colors[8],
                    padding=12,
                    format="%a, %B %d - %H:%M ",
                ),
                widget.TextBox(
                    text='',
                    font='mononoki Nerd Font',
                    background=colors[8],
                    foreground=colors[12],
                    padding=-7.2,
                    fontsize=58
                ),
                widget.CurrentLayout(
                    background=colors[12],
                    padding=10,
                ),
                widget.TextBox(
                    text='',
                    font='mononoki Nerd Font',
                    background=colors[12],
                    foreground=colors[13],
                    padding=-7.2,
                    fontsize=58
                ),
                widget.Battery(
                    padding=4,
                    font='mononoki Nerd Font',
                    charge_char=' ',
                    discharge_char=' ',
                    empty_char=' ',
                    full_char=' ',
                    low_percentage=0.15,
                    low_foreground='#ea1717',
                    format="{char} {percent:2.0%}",
                    background=colors[13],
                ),
            ],
            20,
            background=colors[0],
            opacity=0.95,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"


@hook.subscribe.startup_once
def start_once():
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
