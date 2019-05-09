# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    secure.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/25 18:26:40 by abarthel          #+#    #+#              #
#    Updated: 2019/05/09 18:42:25 by abarthel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from os import system
from time import sleep
from src.start import start_vm
from src.shutdown import shutdown_vm
from src.loadscript import set_ssh, set_network, set_firewall, set_ports, \
        set_grub, set_denialofservices, set_cron, set_web

def secure_vm(dinfo):
    sleep(5)
    system("vboxmanage startvm " + dinfo['VM_name'] + " --type headless")
    while system("ping -c 1 -t 1 " + dinfo['ip_vm'] + " >/dev/null"):
        sleep(1)
    load_scripts(dinfo)
    shutdown_vm(dinfo['VM_name'])
    print ("\nThe VM has been successfully secured." \
            "\nThe VM is now powered off.")

def load_scripts(dinfo):
    set_ssh(dinfo)
    set_network(dinfo)
    set_firewall(dinfo)
    set_ports(dinfo)
    set_grub(dinfo)
    set_denialofservices(dinfo)
    set_cron(dinfo)
    set_web(dinfo)
    sleep(1)

def rsa_gen():
    system("ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa -N ''")
    system("mv ~/.ssh/id_rsa.pub ~/Roger-skyline-1/config/authorized_keys")
    system("git add config/authorized_keys" \
            "&& git commit -m 'upload ssh pub key'" \
            " && git push")
