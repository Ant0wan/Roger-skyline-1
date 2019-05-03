#!/bin/sh
SUDO_PSSWD='root'
echo $SUDO_PSSWD | sudo -S sed -n -i 'p;14a \\tnetmask 255.255.255.252' /etc/network/interfaces >/dev/null
