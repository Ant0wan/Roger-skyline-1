#!/bin/sh
echo $1 | sudo -S sed -n -i 'p;13a \\tbroadcast '$2 /etc/network/interfaces
echo $1 | sudo -S sed -n -i 'p;14a \\tnetmask '$3 /etc/network/interfaces
echo $1 | sudo -S sed -i '11s/allow-hotplug/auto/' /etc/network/interfaces
echo $1 | sudo -S systemctl restart networking
