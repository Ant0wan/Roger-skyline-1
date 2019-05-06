#!/usr/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    start.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/25 18:26:40 by abarthel          #+#    #+#              #
#    Updated: 2019/02/25 18:26:40 by abarthel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from os import system

## Start the VM
def start_vm(dinfo):
    system("vboxmanage startvm " + dinfo['VM_name'] + " --type headless")
    while system("ping -c 1 -t 1 " + dinfo['ip_vm']):
        sleep(1)
    system("ssh -p 2266 antoine@10.11.42.42")
