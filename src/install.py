#!/usr/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    install.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/25 18:26:40 by abarthel          #+#    #+#              #
#    Updated: 2019/02/25 18:26:40 by abarthel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from os import system

## Start the VM
def start_vm(VM_name):
    system("vboxmanage startvm " + VM_name + " --type headless")

def shutdown_vm(VM_name):
    system("vboxmanage controlvm " + VM_name + " acpipowerbutton")

def delete_vm(VM_name):
    system("vboxmanage unregistervm " + VM_name + " --delete")

'''
## Unmount the iso from the VM
def unmount_iso(VM_name):
    os.system("VBoxManage storageattach " + VM_name + " --storagectl IDE --port 0 --device 0 --medium none")
'''
#print ("https://www.oracle.com/technetwork/articles/servers-storage-admin/manage-vbox-cli-2264359.html")
##print ("shasum < disk.vdi")
