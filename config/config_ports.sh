#!/bin/sh
##host $(hostname) | grep -o -e "[0-9]*[.][0-9]*[.][0-9]*[.][0-9]" IP of your host(dump) here 10.11.6.5
#echo $1 | sudo -S sed -n -i 'p;10a 10.11.6.5' /etc/portsentry/portsentry.ignore
#echo $1 | sudo -S apt-get install -y portsentry
#echo $1 | sudo -S sed -i 's/BLOCK_UDP="0"/BLOCK_UDP="1"/g' /etc/portsentry/portsentry.conf
#echo $1 | sudo -S sed -i 's/BLOCK_TCP="0"/BLOCK_TCP="1"/g' /etc/portsentry/portsentry.conf
#echo $1 | sudo -S sed -i .ignore to avoid ban $hostnaame IP
#echo $1 | sudo -S sed -n -i "p;268a KILL_RUN_CMD=\"/sbin/iptables -I INPUT -s \$TARGET\$ -j DROP \&\& /sbin/iptables -I INPUT -s \$TARGET\$ -m limit --limit 3/minute --limit-burst 5 -j LOG --log-level debug --log-prefix 'Portsentry: dropping: '\"" /etc/portsentry/portsentry.conf
#echo $1 | sudo -S systemctl restart portsentry
