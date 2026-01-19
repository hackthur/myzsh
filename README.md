# myzsh



## Arch Linux Installation Steps:

```bash
cfdisk /dev/sd<partition or disk to choose>
mkfs.ext4 /dev/sd<partition or disk to choose>1

mount /dev/sd<partition or disk to choose>1 /mnt/

pacstrap /mnt linux linux-firmware grub networkmanager base base-devel vim nano

genfstab -U /mnt >> /mnt/etc/fstab

arch-chroot /mnt/

passwd 

useradd -m <new user>
passwd <new user>

usermod -aG wheel,video,audio,storage <new user>

nano /etc/sudoers

echo "hackthur" > /etc/hostname
echo "KEYMAP=es" > /etc/vconsole.conf
nano /etc/hosts
nano /etc/locale.gen
locale-gen

grub-install /dev/sd<partition or disk choosed>
grub-mkconfig -o /boot/grub/grub.cfg

exit

reboot now
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
