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
from os import system

def start_vm(VM_name):
    system("vboxmanage startvm " + VM_name + " --type headless")
#    # Sould use a subprocess with that command waiting, here in the script a wait function could be used
 #   i = 1
   # print ("\n\n")
  #  args = shlex.split("vboxmanage showvminfo 'MiniDebian' | grep -c running")
   # print (args)
   #while check_output("vboxmanage showvminfo 'MiniDebian' | grep -c running", shell=True):
   #     sleep(i)
   # print ("OS installed")

