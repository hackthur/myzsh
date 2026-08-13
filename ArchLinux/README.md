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

url:
https://www.google.com/search?q=how+can+i+do+to+know+which+backend+is+on+my+machine+or+from+which+depends+the+kind+of+backend+installed+in+my+computer+for+the+windows+manager%3F&rlz=1C1VDKB_esEC1200EC1200&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCTM0MTQxajBqN6gCALACAA&sourceid=chrome&ie=UTF-8&udm=50&fbs=ABfTbFUDadgeu2mn4mYJ8iEZ1GUDXtepUMVJXDMtqDc3xxrzVWEVPmVGZcFkg8o3Cglbi-juw-nlGyaUsScK1Rhja0SSIQBamZ_ZBsObNYS6_jkz2k2NkYjcvUp35NKarnPcD0VAOBucWJOTzQUKY0XLlP4VZD-fTo1YnrDhRV8LP-5l-ymFUZcMv9Ph_p6Y_77UIz4UjmsNjCcB8K6IQ8GGNss09_adFQ&aep=10&ntc=1&sxsrf=APpeQnvUCztcchxohCv65KDGYXronc0yaw%3A1786639101760&mstk=AUtExfA5ZurD4M-CAGAgasFcrc7_zZ-Ccr4AgW1zbphbJcSLBH7hDgvOUvYjAXt69twmGonkQC1p2VhrFvwCjHsX5uwGbPeV1s4OgeSreKC_F2H1bO9Vhgxwp_g-i-pg1-8-JfaC1jrAEnO53jfutmeTm5aPoegCeJpiteR9evEk1Sq-ADCJsh91a4PWQ4BaYWX2BHOSeDNcQ6mAzqZfKhZSA1276tp0wQWrpkAkPggTGpVPzMacbb2IEPEOAHsFPkhWXE__dCLr4TccuUM23DssHadWjWVKWNZZmZvVyXx6NVuHcqT8PDMpvw8UhCgw2Lt0ib9TxYLih40w5Q&aioh=3&csuir=1&cs=1&atvm=2&mtid=R_R9aqikHKSGwbkP8KuU6Q0




