#!/bin/sh
SUDO_PSSWD='root'
##There is an error in the subject, we cannot have the same mask so we won't change nor restart service
#echo $SUDO_PSSWD | sudo -S sed -n -i 'p;14a \\tnetmask 255.255.255.252' /etc/network/interfaces
#echo $SUDO_PSSWD | sudo -S systemctl restart networking
