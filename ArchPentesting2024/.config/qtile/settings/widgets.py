from libqtile import widget
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)


dickers = [["#282c34", "#282c34"],
           ["#1c1f24", "#1c1f24"],
           ["#dfdfdf", "#dfdfdf"],
           ["#ff6c6b", "#ff6c6b"],
           ["#98be65", "#98be65"],
           ["#da8548", "#da8548"],
           ["#51afef", "#51afef"],
           ["#c678dd", "#c678dd"],
           ["#46d9ff", "#46d9ff"],
           ["#a9a1e1", "#a9a1e1"]]


def base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }
    
    
def custom_base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        # 'background': colors[bg]
    }

def separator():
    return widget.Sep(**base(), linewidth=0, padding=1)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=2
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="",  # Icon: nf-oct-triangle_left
        fontsize=50,
        padding=3
    )
    
    
def custom_powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **custom_base(fg, bg),
        text="",  # Icon: nf-oct-triangle_left
        fontsize=50,
        padding=3
    )    
    


def workspaces():
    return [
        # separator(),
        widget.GroupBox(
            **custom_base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=12,
            margin_y=2,
            margin_x=0,
            padding_y=2,
            padding_x=3,
            borderwidth=3,
            active=dickers[2],
            inactive=dickers[4],
            rounded=True,
            highlight_color=dickers[1],
            highlight_method='line',
            # urgent_alert_method='block',
            # urgent_border=colors['urgent'],
            this_current_screen_border=dickers[6],
            this_screen_border=dickers[4],
            other_current_screen_border=dickers[6],
            other_screen_border=dickers[4],
            # disable_drag=True
        ),
        widget.TextBox(
            text='   ',
            font="Hack Nerd Font",
            # background=dickers[0],
            #foreground='#4c566a',
            padding=2,
            fontsize=14
        ),
        separator(),
        widget.WindowName(font="Hack Nerd Font",
                          foreground="#4c566a", fontsize=10),
        # separator(),
    ]


primary_widgets = [
    *workspaces(),

    # separator(),

    custom_powerline('color4', 'dark'),

    icon(bg="color4", text=' '),  # Icon: nf-fa-download

    widget.CheckUpdates(
        background=colors['color4'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),

    powerline('color3', 'color4'),

    icon(bg="color3", text=' '),  # Icon: nf-fa-feed

    widget.Net(**base(bg='color3'), interface='enp0s25'),

    #powerline('color2', 'color3'),

    #widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

    # widget.CurrentLayout(**base(bg='color2'), padding=5),

    powerline('color1', 'color3'),

    # icon(bg="color1", fontsize=17),  # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color1'),

    widget.Systray(background=colors['dark'], padding=5),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
