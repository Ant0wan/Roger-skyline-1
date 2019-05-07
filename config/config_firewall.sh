#!/bin/sh
# 1 - https://www.digitalocean.com/community/tutorials/how-the-iptables-firewall-works
# 2 - https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-using-iptables-on-ubuntu-14-04
# 3 - https://www.digitalocean.com/community/tutorials/iptables-essentials-common-firewall-rules-and-commands 
SUDO_PSSWD='root'
echo $SUDO_PSSWD | sudo -S iptables -P FORWARD DROP
echo $SUDO_PSSWD | sudo -S iptables -A INPUT -p tcp --dport 2266 -j ACCEPT
echo $SUDO_PSSWD | sudo -S iptables -A INPUT -p tcp --dport 80 -j ACCEPT
echo $SUDO_PSSWD | sudo -S iptables -I INPUT 1 -i lo -j ACCEPT
echo $SUDO_PSSWD | sudo -S iptables -F
