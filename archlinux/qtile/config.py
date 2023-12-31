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

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import os
import subprocess

mod = "mod4"
terminal = "alacritty" 
fg = "#EBDBB2"
bg = "#282828"
red = "#cc241d"
green = "#98971a"
yellow = "#d79921"
blue = "#458588"
magenta = "#b16286"
cyan = "#689d6a"
cyanBright = "#8ec07c"
blackBright = "#928374"
fontsizeIcon = 24

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    
    # Teclas para lanzar menu rofi
    Key([mod], "m", lazy.spawn("rofi -show drun" ), desc="Launch rofi"),

    # Teclas para captura de pantalla
    Key([mod], "s", lazy.spawn("scrot"), desc="Captura toda la pantalla"),
    Key([mod, "shift"], "s", lazy.spawn("scrot -s"), desc="Captura parte de la pantalla"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

# Iconos
# 1 = \uF303 nf-linux-archlinux

#groups = [Group(i) for i in "123456789"]
#groups = [Group(i) for i in ["1", "2", "3", "4", "5", "6"]]
groups = [Group(i) for i in ["DEV", "WWW", "SYS", "DOC", "MUL"]]

for i, group in enumerate(groups):
    numberDesktop = str(i + 1)
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key([mod], numberDesktop, lazy.group[group.name].toscreen(), desc="Switch to group {}".format(group.name)),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key([mod, "shift"], numberDesktop, lazy.window.togroup(group.name, switch_group=True), desc="Switch to & move focused window to group {}".format(group.name)),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], group.name, lazy.window.togroup(group.name),
            #     desc="move focused window to group {}".format(group.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus=red, border_width=4),
    layout.Max(),
    #layout.Stack(num_stacks=2),
    #layout.Bsp(),
    layout.Matrix(),
    #layout.MonadTall(),
    #layout.MonadWide(),
    #layout.RatioTile(),
    #layout.Tile(),
    #layout.TreeTab(),
    #layout.VerticalTile(),
    #layout.Zoomy(),
]

widget_defaults = dict(
    font="MesloLGM Nerd Font Mono",
    #font="FontAwesome",
    fontsize=16,
    padding=5,
    foreground=fg,
    background=bg,
)
extension_defaults = widget_defaults.copy()

separacion = widget.Sep(linewidth=2)

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
			highlight_method="block", 
			this_current_screen_border=cyan,
			active="#FFFFFF",
			inactive=bg,
			rounded=False,
			block_highlight_text_color=fg, background=blackBright
		),
                widget.Prompt(prompt="$ ", background=cyan),
		separacion,
                widget.WindowName(background=blackBright),
		separacion,
		widget.CheckUpdates(no_update_string="Upd: 0", display_format="Upd: {updates}", update_interval=3600, background=cyanBright),
		separacion,
	        widget.Memory(format="Mem: {MemUsed:.0f}{mm}", background=magenta),	
		separacion,
		widget.PulseVolume(fmt="Vol: {}", limit_max_volume="true", background=green),
		separacion,
                widget.Clock(format="%d/%m/%Y %H:%M", background=blue),
		separacion,
		widget.CurrentLayoutIcon(scale=0.5, padding=0, background=yellow),
		separacion,
                widget.Systray(background=red, icon_size=fontsizeIcon),
		widget.LaunchBar(
			background=red, 
			fontsize=fontsizeIcon, 
			progs=[
				('󰍃', 'qshell:self.qtile.shutdown()', 'Logout'), # Hace lo mismo que QuickExit Icono nf-md-logout \uf0343
				('\uF011', 'poweroff', 'Apagar Ordenador')
			], 
			text_only=True
		)
            ],
            34,
	    background=bg,
	    #margin=[0, 0, 10, 0]
	    border_width=[0, 0, 4, 0],
	    border_color=fg,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
