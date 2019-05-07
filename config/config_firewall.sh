#!/bin/sh
SUDO_PSSWD='root'
# Close all pipes
echo $SUDO_PSSWD | sudo -S iptables -P FORWARD DROP
echo $SUDO_PSSWD | sudo -S iptables -P INPUT DROP
echo $SUDO_PSSWD | sudo -S iptables -P OUTPUT DROP
# Open ports
echo $SUDO_PSSWD | sudo -S iptables -A INPUT -p tcp --dport 2266 -j ACCEPT
#echo $SUDO_PSSWD | sudo -S iptables -A INPUT -p tcp --dport 80 -j ACCEPT
# Keep previous connections
echo $SUDO_PSSWD | sudo -S iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
echo $SUDO_PSSWD | sudo -S iptables -A OUTPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
# Loopback
echo $SUDO_PSSWD | sudo -S iptables -t filter -A INPUT -i lo -j ACCEPT
echo $SUDO_PSSWD | sudo -S iptables -t filter -A OUTPUT -o lo -j ACCEPT
# Load rules
echo $SUDO_PSSWD | sudo -S iptables -F
