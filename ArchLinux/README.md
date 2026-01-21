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
