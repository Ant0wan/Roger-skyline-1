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
    #system("echo root | ssh antoine@10.11.6.42 -p 22")
    #ssh-keygen -t rsa -b 2048 -f config/authorized_keys -N ""

## Generate RSA key and move it to appropriate repo for the preseed to wget it
#https://kb.iu.edu/d/aews
def rsa_gen():
    system("ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa -N ''")
    system("mv ~/.ssh/id_rsa.pub ~/Roger-skyline-1/config/authorized_keys")
    system("git add config/authorized_keys && git commit -m 'upload ssh pub key' && git push")

#def connect_ssh(VM_name, ip_vm, user_passwd)
#    system("ssh ") # change port 2222
                    # block passwd connection
                   # ssh public keys

#print ("https://www.oracle.com/technetwork/articles/servers-storage-admin/manage-vbox-cli-2264359.html")
##print ("shasum < disk.vdi")
