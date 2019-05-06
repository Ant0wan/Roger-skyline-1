#!/bin/sh
SUDO_PSSWD='root'
# Server
echo $SUDO_PSSWD | sudo -S sed -n -i 'p;13a Port 2266' /etc/ssh/sshd_config
echo $SUDO_PSSWD | sudo -S sed -n -i 'p;33a PermitRootLogin no' /etc/ssh/sshd_config
echo $SUDO_PSSWD | sudo -S sed -n -i 'p;57a PasswordAuthentication no' /etc/ssh/sshd_config
# Client
#echo $SUDO_PSSWD | sudo -S sed -n -i 'p;41a Port 2266' /etc/ssh/ssh_config
# Service restart
echo $SUDO_PSSWD | sudo -S systemctl restart ssh
