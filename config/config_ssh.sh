#!/bin/sh
SUDO_PSSWD='root'
echo $SUDO_PSSWD | sudo -S sed -n -i 'p;13a Port 2266' /etc/ssh/sshd_config
echo $SUDO_PSSWD | sudo -S sed -n -i 'p;41a Port 2266' /etc/ssh/ssh_config
echo $SUDO_PSSWD | sudo -S systemctl restart ssh

# port 2222
# block passwd connection
# block root connection
