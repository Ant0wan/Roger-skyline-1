#!/bin/sh
SUDO_PSSWD='root'
echo $SUDO_PSSWD | sudo -S sed -n -i 'p;13a \\tbroadcast 10.11.42.47' /etc/network/interfaces
echo $SUDO_PSSWD | sudo -S sed -n -i 'p;14a \\tnetmask 255.255.255.252' /etc/network/interfaces
echo $SUDO_PSSWD | sudo -S sed  -i '11s/allow-hotplug/auto/' /etc/network/interfaces
echo $SUDO_PSSWD | sudo -S systemctl restart networking
