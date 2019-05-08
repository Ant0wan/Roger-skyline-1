# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    start.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/25 18:26:40 by abarthel          #+#    #+#              #
#    Updated: 2019/05/07 18:25:52 by abarthel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from time import sleep
from os import system, popen

def start_vm(VM_name):
    status = popen("vboxmanage showvminfo '" \
            + VM_name + "' | grep -c 'powered off'").read()
    if '1' in str(status):
        system("vboxmanage startvm " + VM_name + " --type headless")

def ssh_vm(dinfo):
    start_vm(dinfo['VM_name'])
    while system("ping -c 1 -t 1 " + dinfo['ip_vm'] + " >/dev/null"):
        sleep(1)
    sleep(1)
    system("ssh -p " + dinfo['ssh_port'] + " " + \
            dinfo['user'] + "@" + dinfo['ip_vm'])
