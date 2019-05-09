# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loadscript.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/25 18:26:40 by abarthel          #+#    #+#              #
#    Updated: 2019/05/09 10:27:28 by abarthel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from time import sleep
from os import system, popen

def set_ssh(dinfo):
    sleep(1)
    system("ssh -o 'StrictHostKeyChecking no' -i ~/.ssh/id_rsa " + \
            dinfo['user'] + "@" + dinfo['ip_vm'] + \
            " 'sh -s' < config/config_ssh.sh " + dinfo['passwd'] + \
            " " + dinfo['ssh_port'])
    print ("\nSSH has been configured.")

def set_network(dinfo):
    sleep(1)
    system("ssh -p " + dinfo['ssh_port'] + " " + \
            dinfo['user'] + "@" + dinfo['ip_vm'] + \
            " 'sh -s' < config/config_network.sh " + dinfo['passwd'] + \
            " " + dinfo['ip_vm'] + " " + dinfo['netmask'])
    print ("\nNetwork has been configured.")

def set_firewall(dinfo):
    sleep(1)
    system("ssh -p " + dinfo['ssh_port'] + " " + \
            dinfo['user'] + "@" + dinfo['ip_vm'] + \
            " 'sh -s' < config/config_firewall.sh " + dinfo['passwd'] + \
            " " + dinfo['ssh_port'] + " " + dinfo['dns_port'])
    print ("\nFirewall has been configured.")

def set_ports(dinfo):
    sleep(1)
    ip_host = str(popen('host $(hostname) | grep -o -e "[0-9]*[.][0-9]*[.][0-9]*[.][0-9]"').read().strip("\n"))
    system("ssh -p " + dinfo['ssh_port'] + " " + \
            dinfo['user'] + "@" + dinfo['ip_vm'] + \
            " 'sh -s' < config/config_ports.sh " + dinfo['passwd'] + \
            " " + "10.11.6.7")
    print ("\nPorts have been configured.")

def set_grub(dinfo):
    sleep(1)
    system("ssh -p " + dinfo['ssh_port'] + " " + \
            dinfo['user'] + "@" + dinfo['ip_vm'] + \
            " 'sh -s' < config/config_grub.sh " + dinfo['passwd'])
    print ("\nGRUB menu has been disabled.")
