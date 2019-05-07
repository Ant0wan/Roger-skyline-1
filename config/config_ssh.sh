#!/bin/sh
echo $1 | sudo -S sed -n -i 'p;13a Port '$2 /etc/ssh/sshd_config
echo $1 | sudo -S sed -n -i 'p;33a PermitRootLogin no' /etc/ssh/sshd_config
echo $1 | sudo -S sed -n -i 'p;58a PasswordAuthentication no' /etc/ssh/sshd_config
echo $1 | sudo -S systemctl restart ssh
