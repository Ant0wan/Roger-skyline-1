#!/bin/sh
SUDO_PSSWD='root'
SSH_PORT='2266'
DNS_PORT='53'
echo $SUDO_PSSWD | sudo -S apt-get install -y ufw
echo $SUDO_PSSWD | sudo -S ufw --force reset
echo $SUDO_PSSWD | sudo -S default deny incoming
echo $SUDO_PSSWD | sudo -S default deny outgoing
echo $SUDO_PSSWD | sudo -S allow $SSH_PORT/tcp
echo $SUDO_PSSWD | sudo -S ufw allow out http
echo $SUDO_PSSWD | sudo -S ufw allow in http
echo $SUDO_PSSWD | sudo -S ufw allow out https
echo $SUDO_PSSWD | sudo -S ufw allow in https
echo $SUDO_PSSWD | sudo -S ufw allow out $DNS_PORT
echo $SUDO_PSSWD | sudo -S ufw logging on
echo $SUDO_PSSWD | sudo -S ufw --force enable
