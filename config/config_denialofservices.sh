#!/bin/sh
echo $1 | sudo -S apt-get install -y fail2ban
echo $1 | sudo -S echo '[DEFAULT]

findfime = 3600
bantime = 86400
maxretry = 3

[sshd]
enabled = true
port = '$2 > /etc/fail2ban/jail.d/custom.conf
echo $1 | sudo -S systemctl restart fail2ban
