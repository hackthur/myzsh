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
Look for lines containing qtile or Xorg to pinpoint if a syntax error in your personal ~/.config/qtile/config.py file is causing the crash.If you are a




