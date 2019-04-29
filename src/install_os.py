#!/usr/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    install_os.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/25 18:26:40 by abarthel          #+#    #+#              #
#    Updated: 2019/02/25 18:26:40 by abarthel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
import subprocess
from time import sleep
from os import system, popen

def install_os(VM_name):
    system("vboxmanage startvm " + VM_name + " --type headless")
    time.sleep(1)
    status = popen("vboxmanage showvminfo '" \
            + VM_name + "' | grep -c 'powered off'").read()
    if '1' in str(status):
        print ("Could not start the VM " + VM_name)
        exit()
    else:
        print ("Installing operating system on " + VM_name + ".")
        while True:
            status = popen("vboxmanage showvminfo '" \
                    + VM_name + "' | grep -c running").read()
            if '1' not in status:
                print ("Operating system successfully installed.")
                break
            else:
                time.sleep(5)
