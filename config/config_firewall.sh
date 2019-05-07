#!/bin/sh
SUDO_PSSWD='root'
SSH_PORT='2266'
echo $SUDO_PSSWD | sudo -S apt-get install -y ufw
echo $SUDO_PSSWD | sudo -S ufw --force reset
echo $SUDO_PSSWD | sudo -S default deny incoming
echo $SUDO_PSSWD | sudo -S default deny outgoing
echo $SUDO_PSSWD | sudo -S allow $SSH_PORT/tcp
echo $SUDO_PSSWD | sudo -S ufw allow out http
echo $SUDO_PSSWD | sudo -S ufw allow in http
echo $SUDO_PSSWD | sudo -S ufw allow out https
echo $SUDO_PSSWD | sudo -S ufw allow in https
echo $SUDO_PSSWD | sudo -S ufw allow out 53 
#/var/log/ufw.log
echo $SUDO_PSSWD | sudo -S ufw logging on
echo $SUDO_PSSWD | sudo -S ufw --force enable
#echo $SUDO_PSSWD | sudo -S 
