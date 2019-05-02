#!/usr/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    secure.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/25 18:26:40 by abarthel          #+#    #+#              #
#    Updated: 2019/02/25 18:26:40 by abarthel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from time import sleep
from os import system
from src.start import start_vm

## Secure the VM
def secure_vm(VM_name):
    start_vm(VM_name)
    sleep(10)
    system("echo root | ssh -S antoine@10.11.6.42 -p 22")


#def connect_ssh(VM_name, ip_vm, user_passwd)
#    system("ssh ") # change port 2222
                    # block passwd connection
                   # ssh public keys

#print ("https://www.oracle.com/technetwork/articles/servers-storage-admin/manage-vbox-cli-2264359.html")
##print ("shasum < disk.vdi")
