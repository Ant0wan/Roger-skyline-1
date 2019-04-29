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

import subprocess
from time import sleep
from os import system, popen

def start_vm(VM_name):
    system("vboxmanage startvm " + VM_name + " --type headless")
    time.sleep(1)
    status = popen("vboxmanage showvminfo 'MiniDebian' | grep -c 'powered off'").read()
    if '1' in str(status):
        print ("Could not start the VM")
        exit()
    else:
        while True:
            status = popen("vboxmanage showvminfo 'MiniDebian' | grep -c running").read()
            if '1' not in status:
                print ("OS installed")
                break
            else:
                time.sleep(5)
