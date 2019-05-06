# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    start.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/25 18:26:40 by abarthel          #+#    #+#              #
#    Updated: 2019/05/06 12:34:18 by abarthel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from os import system, popen

def start_vm(dinfo):
    status = popen("vboxmanage showvminfo '" \
            + VM_name + "' | grep -c 'powered off'").read()
    if '1' in str(status):
        system("vboxmanage startvm " + dinfo['VM_name'] + " --type headless")

def ssh_vm(dinfo):
    start_vm(dinfo)
    while system("ping -c 1 -t 1 " + dinfo['ip_vm']):
        sleep(1)
    system("ssh -p " + dinfo['ssh-port'] + " " + \
            dinfo['user'] + "@" + dinfo['ip_vm'])
