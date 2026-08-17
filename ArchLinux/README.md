# Arch linux

## Installation 

For the installation I choose the username **hackthur** but you can choose the user you want 
and that is for the partition

- username: **hackthur**
- parition: **/dev/sda**


```bash

[arthur@hackthur ~]$ cfdisk /dev/sda
[arthur@hackthur ~]$ mkfs.ext4 /dev/sda1

[arthur@hackthur ~]$ mount /dev/sda1 /mnt/

[arthur@hackthur ~]$ pacstrap /mnt linux linux-firmware grub networkmanager base base-devel vim nano

[arthur@hackthur ~]$ genfstab -U /mnt >> /mnt/etc/fstab

[arthur@hackthur ~]$ arch-chroot /mnt/


# the `passwd` first suppose to choose the new password for root

[arthur@hackthur ~]$ passwd 

[arthur@hackthur ~]$ useradd -m hackthur
[arthur@hackthur ~]$ passwd hackthur

[arthur@hackthur ~]$ usermod -aG wheel,video,audio,storage hackthur

[arthur@hackthur ~]$ nano /etc/sudoers

[arthur@hackthur ~]$ echo "hackthur" > /etc/hostname
[arthur@hackthur ~]$ echo "KEYMAP=es" > /etc/vconsole.conf
[arthur@hackthur ~]$ nano /etc/hosts

[arthur@hackthur ~]$ /bin/cat /etc/hosts
# Static table lookup for hostnames.
# See hosts(5) for details.
127.0.0.1        localhost
::1              localhost
127.0.0.1	 hackthur.localhost hackthur

[arthur@hackthur ~]$ nano /etc/locale.gen
[arthur@hackthur ~]$ locale-gen

[arthur@hackthur ~]$ grub-install /dev/sd<partition or disk choosed>
[arthur@hackthur ~]$ grub-mkconfig -o /boot/grub/grub.cfg

[arthur@hackthur ~]$ exit

[arthur@hackthur ~]$ reboot now
[arthur@hackthur ~]$ echo "old command installation"
[arthur@hackthur ~]$ sudo pacman -S gnome firefox alacritty kitty qtile python python-pip xorg xorg-server git
[arthur@hackthur ~]$ echo "new command installation"
[arthur@hackthur ~]$ sudo pacman -S gdm firefox alacritty python python-pip gnome qtile git python-pywlroots xorg-xwayland python-pyxdg ttf-dejavu ttf-nerd-fonts-symbols-common

```


## YAY (AUR) ArchLinux package manager

```bash
sudo pacman -S git
cd /opt/
sudo git clone https://aur.archlinux.org/yay-git.git
sudo chown -R username:username yay-git/
cd yay-git
makepkg -si
```


## Mysql (Mariadb) server and client installation

```bash
sudo pacman -Syu

sudo pacman -S mariadb

sudo mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql 

sudo systemctl start mariadb
sudo systemctl enable mariadb 

sudo mysql_secure_installation

sudo mysql -u root -p 
```

## Create a Mysql user with grant privileges

```bash

CREATE USER 'sammy'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'sammy'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```


## Configuration for the Wayland service
### Check for Broken Python DependenciesQtile is written in Python, and updates to core libraries like cairocffi or xcffib can frequently break the launch sequence.Switch to a virtual terminal by pressing Ctrl + Alt + F3.
  
  1. Switch to a virtual terminal by pressing Ctrl + Alt + F3
  2. Log in with your username and password.
  3. Run the following command to check if Qtile can start at all

```bash
qtile start
```
  4. If it returns an initialization error regarding a specific Python module (e.g., xcffib), you need to reinstall or fix the package. Run:
```bash
sudo pacman -Syu python-cairocffi python-xcffib qtile
```

### Verify the Desktop Entry File

GDM needs a .desktop file to recognize Qtile as an available session. If you are missing this file, GDM will not be able to hand off the session properly.
  
  1. Check if the file exists by running
   ```bash
    ls /usr/share/xsessions/qtile.desktop
  ```
  2. If it is missing, create it manually
  ```bash
  sudo nano /usr/share/xsessions/qtile.desktop
  ```
  3. Paste the following configuration into the file:
  ```bash
  [Desktop Entry]
  Name=Qtile
  Comment=Qtile Tiling Window Manager
  Exec=qtile start
  Type=Application
  Keywords=wm;tiling;
  ```
  4. Save and exit (Ctrl + O, then Ctrl + X)
 

### Force GDM to Use Xorg (Disable Wayland)

GDM runs on Wayland by default, which can cause session handoff failures if you are launching an X11-based window manager like the default Qtile.

  1. Open the GDM custom configuration file:bash
  ```bash
    sudo nano /etc/gdm/custom.conf
  ```
  2. Locate the line #WaylandEnable=false and uncomment it by removing the #
  ```ini
  WaylandEnable=false
  ```
  3. Save the file and restart your GDM service
  ```bash
  sudo systemctl restart gdm.service
  ```
  4. Check the Error LogsIf it still crashes back to the GDM login screen, look at your user system logs immediately after a failed login attempt
  ```bash
  journalctl --user -b 0 -e
  ```
Look for lines containing qtile or Xorg to pinpoint if a syntax error in your personal ~/.config/qtile/config.py file is causing the crash.

```bash
sudo pacman -S python-pywlroots xorg-xwayland python-pyxdg
```

```bash
[hackthur@hackarthur ~]$ cat /usr/share/wayland-sessions/qtile.desktop 
─────┬─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
     │ File: /usr/share/wayland-sessions/qtile.desktop 
─────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
1    │ [Desktop Entry] 
2    │ Name=Qtile 
3    │ Comment=Qtile Session 
4    │ DesktopNames=qtile 
5    │ # Start qtile as a systemd user service so graphical-session.target is 
6    │ # activated and xdg-desktop-portal (screen sharing, file pickers, ...) works. 
7    │ # Needs qtile.service and qtile-session.target (from the qtile source tree, 
8    │ # resources/) installed to ~/.config/systemd/user/; see resources/README. 
9    │ # The Exec hands the variables the display manager set for the session to the 
10   │ # user manager (bare "import-environment" is deprecated, so they are listed 
11   │ # explicitly), then starts qtile.service. The list includes XDG_CURRENT_DESKTOP
12   │ # (set above via DesktopNames) and XDG_SESSION_TYPE, which qtile uses to pick 
13   │ # its backend; unset variables are skipped. Static vars (locale, toolkit 
14   │ # settings, ...) are better placed in ~/.config/environment.d/. 
15   │ # To start qtile directly instead, use: Exec=qtile start 
16   │ Exec=/bin/sh -c "systemctl --user import-environment DISPLAY WAYLAND_DISPLAY XAUTHORITY XDG_SEAT XDG_VTNR XDG_SESSION_ID XDG_SESSION_TYPE XDG_SESSION_ │ CLASS XDG_SESSION_DESKTOP XDG_CURRENT_DESKTOP            DESKTOP_SESSION; exec systemctl --user start --wait qtile.service" 
17   │ Type=Application 
18   │ Keywords=wm;tiling
```

replace in line 16 for

`Exec=qtile start`





url:
https://www.google.com/search?q=how+can+i+do+to+know+which+backend+is+on+my+machine+or+from+which+depends+the+kind+of+backend+installed+in+my+computer+for+the+windows+manager%3F&rlz=1C1VDKB_esEC1200EC1200&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCTM0MTQxajBqN6gCALACAA&sourceid=chrome&ie=UTF-8&udm=50&fbs=ABfTbFUDadgeu2mn4mYJ8iEZ1GUDXtepUMVJXDMtqDc3xxrzVWEVPmVGZcFkg8o3Cglbi-juw-nlGyaUsScK1Rhja0SSIQBamZ_ZBsObNYS6_jkz2k2NkYjcvUp35NKarnPcD0VAOBucWJOTzQUKY0XLlP4VZD-fTo1YnrDhRV8LP-5l-ymFUZcMv9Ph_p6Y_77UIz4UjmsNjCcB8K6IQ8GGNss09_adFQ&aep=10&ntc=1&sxsrf=APpeQnvUCztcchxohCv65KDGYXronc0yaw%3A1786639101760&mstk=AUtExfA5ZurD4M-CAGAgasFcrc7_zZ-Ccr4AgW1zbphbJcSLBH7hDgvOUvYjAXt69twmGonkQC1p2VhrFvwCjHsX5uwGbPeV1s4OgeSreKC_F2H1bO9Vhgxwp_g-i-pg1-8-JfaC1jrAEnO53jfutmeTm5aPoegCeJpiteR9evEk1Sq-ADCJsh91a4PWQ4BaYWX2BHOSeDNcQ6mAzqZfKhZSA1276tp0wQWrpkAkPggTGpVPzMacbb2IEPEOAHsFPkhWXE__dCLr4TccuUM23DssHadWjWVKWNZZmZvVyXx6NVuHcqT8PDMpvw8UhCgw2Lt0ib9TxYLih40w5Q&aioh=3&csuir=1&cs=1&atvm=2&mtid=R_R9aqikHKSGwbkP8KuU6Q0



## QTile configuration

`$HOME/.config/qtile/config.py`

```python
from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import psutil  # installed by pip the psutil dependency
import json

# --- ESTO ACTIVA TU TECLADO EN ESPAÑOL LATINOAMERICANO EN WAYLAND ---
from libqtile.backend.wayland import InputConfig
wl_input_rules = {
    "type:keyboard": InputConfig(kb_layout="latam"),
}
# --------------------------------------------------------------------

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

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# Cambiamos "LG3D" por "qtile" ya que Wayland no necesita simular ser Java
wmname = "qtile" 

# --- ELIMINAMOS PICOM, SETXKBMAP Y FEH DE AQUÍ ---
# El fondo de pantalla ahora lo maneja Qtile de forma nativa en tu archivo de pantallas.
```


`$HOME/.config/qtile/screens.py`

```python
from libqtile.config import Screen
from libqtile import bar
from qtile import qtile  # Importamos el objeto principal de qtile
from .widgets import primary_widgets, secondary_widgets

def status_bar(widgets):
    return bar.Bar(widgets, 16, opacity=0.60)

# Ruta de tu fondo de pantalla clásico
mi_fondo = "~/.config/qtile/images/hackthur2.png"

# Creamos la lista de pantallas vacía
screens = []

# Le preguntamos a Qtile cuántas pantallas físicas detecta Wayland en tu máquina
# Si por alguna razón no detecta ninguna en el arranque, ponemos 1 por defecto
try:
    num_monitores = len(qtile.core.outputs) if qtile and qtile.core else 1
except AttributeError:
    num_monitores = 1

# Configuramos la pantalla principal (Monitor 1)
screens.append(
    Screen(
        top=status_bar(primary_widgets),
        wallpaper=mi_fondo,
        wallpaper_mode="fill"
    )
)

# Si tienes más monitores conectados (Monitor 2, 3, etc.), les añade su barra secundaria y su fondo
if num_monitores > 1:
    for _ in range(1, num_monitores):
        screens.append(
            Screen(
                top=status_bar(secondary_widgets),
                wallpaper=mi_fondo,
                wallpaper_mode="fill"
            )
        )

```


`$HOME/.config/qtile/settings/widgets.py`

````python
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

    widget.StatusNotifier(background=colors['dark'], padding=5),
]

"""
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
    # Dejamos Net listo. Si no marca red, recuerda quitarle el parámetro interface
    widget.Net(**base(bg='color3'), interface='enp0s25'), 
    powerline('color1', 'color3'),
    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),
    powerline('dark', 'color1'),
    # === CAMBIO CRÍTICO PARA WAYLAND AQUÍ ===
    widget.StatusNotifier(background=colors['dark'], padding=5),
]
"""

secondary_widgets = [
    *workspaces(),
    separator(),
    powerline('color1', 'dark'),
    widget.CurrentLayout(**base(bg='color1'), scale=0.65),
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
```

## 🛡️ AUR Security Guide (How to Read & Audit Recipes)

Since the Arch User Repository (AUR) relies on community-driven installation recipes (`PKGBUILD` files), malicious actors can compromise orphan packages to inject malware. Follow these steps to audit your packages using `yay` before compiling them on your machine.

### 1. Inspecting a Package BEFORE Installation
When installing a new package {e.g., `burpsuite`), `yay` will ask you several interactive questions. Handle them like this:


1. **`PKGBUILDs to edit?`** -> Press **`Enter`** (None) unless you need to change something manually.
2. **`Diffs to show? [N]one [A]ll [Ab]ort`** -> Type **`A`** (All) and press **`Enter`**.

This opens the full script inside a secure text viewer (`less`).
* Use the **Arrow Keys** to scroll up and down.
* Press **`Q`** to exit the viewer and continue with the installation.

> 💡 **Quick Tip:** If you want to download and inspect a recipe *without* starting the installation process, run:
> ```bash
> yay --getpkgbuild <package_name>
> ```

---

### 2. Auditing Packages That Are ALREADY Installed
`yay` keeps a local history of every recipe you have ever built. You can inspect your current setup at any time by exploring your local cache folder:

```bash
# Navigate to your local yay cache
cd ~/.cache/yay/

# List all your installed AUR packages
ls

# Enter a specific package folder and view its instructions
cd <package_name>
cat PKGBUILD
```

---

### 3. The Security Checklist: What to Look For
When reading a `PKGBUILD` script, pay close attention to these three specific sections where malicious code is usually injected:

* **`source=(...)`** (Where the files are downloaded from)
  * ✅ **Safe:** Links pointing to official websites (e.g., `portswigger.net`) or the author's official GitHub repository.
  * ❌ **Suspicious:** Domains using strange extensions (`.xyz`, `.top`), unknown servers, or random personal GitHub profiles.

* **`prepare()`** (Pre-compilation steps)
  * ❌ **Suspicious:** Look for active network commands like `curl`, `wget`, or `npm install` fetching external binaries and executing them immediately via `bash script.sh`. Clean recipes rarely download hidden files here.

* **`build()` or `package()`** (Compilation and folder creation)
  * ❌ **Suspicious:** Any line attempting to read your home directory (`$HOME` or `~/.ssh`), copy your personal files, or execute obfuscated background binaries.
