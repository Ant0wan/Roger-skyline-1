#!/bin/sh
SUDO_PSSWD='root'
SSH_PORT='2266'
echo $SUDO_PSSWD | sudo -S iptables -P FORWARD DROP
echo $SUDO_PSSWD | sudo -S iptables -P INPUT DROP
echo $SUDO_PSSWD | sudo -S iptables -P OUTPUT DROP
echo $SUDO_PSSWD | sudo -S iptables -t filter -A INPUT -p tcp --dport $SSH_PORT -j ACCEPT
echo $SUDO_PSSWD | sudo -S iptables -t filter -A OUTPUT -p tcp --dport $SSH_PORT -j ACCEPT
#echo $SUDO_PSSWD | sudo -S iptables -A INPUT -p tcp --dport 80 -j ACCEPT
echo $SUDO_PSSWD | sudo -S iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
echo $SUDO_PSSWD | sudo -S iptables -A OUTPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
echo $SUDO_PSSWD | sudo -S iptables -t filter -A INPUT -i lo -j ACCEPT
echo $SUDO_PSSWD | sudo -S iptables -t filter -A OUTPUT -o lo -j ACCEPT
echo $SUDO_PSSWD | sudo -S iptables -F
