#!/usr/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    roger_skyline_1.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/25 18:26:40 by abarthel          #+#    #+#              #
#    Updated: 2019/02/25 18:26:40 by abarthel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from os import system, getcwd
import sys

## Get the path
path = getcwd()

## Create and configure the VM
def configure_vm(VM_name, cpu, ram, OS_type, disk_size):
    system("VBoxManage createvm --name " + VM_name + " --ostype " + OS_type + " --register")
    system("VBoxManage modifyvm " + VM_name + " --cpus " + cpu + " --memory " + ram)
    create_disk(VM_name, disk_size)
    boot_order(VM_name)
    #BUG#os.system("VBoxManage modifyvm " + VM_name + " --nic2 bridged  --bridgeadapter1 " + NAT2)

## Mount the iso on the VM
## Create and mount the disk vdi
def create_disk(VM_name, disk_size):
    storage = ('IDE', 'SATA')
    disk_name = 'diskdebianmini'
    disk_file_format = 'vdi'
    disk_type = 'hdd'
    for a_type in storage:
        system("VBoxManage storagectl " + VM_name + " --name " + a_type + " --add " + a_type)
    system("VBoxManage storageattach " + VM_name + " --storagectl " + storage[0] + " --port 0 --device 0 --type dvddrive --medium preseed-mini.iso")
    system("vboxmanage createmedium disk --filename " + disk_name + " --size " + disk_size + " --format " + disk_file_format)
    system("VBoxManage storageattach " + VM_name + " --storagectl " + storage[1] + " --port 0 --device 0 --type " + disk_type + " --medium " + disk_name + "." + disk_file_format)

## Boot order
def boot_order(VM_name):
    boot_devices = ('disk', 'dvd', 'none')
    for device in boot_devices:
        system("vboxmanage modifyvm " + VM_name + " --boot"(boot_devices.index(device) + 1) + " " + device)

'''
## Unmount the iso from the VM
def unmount_iso(VM_name):
    os.system("VBoxManage storageattach " + VM_name + " --storagectl IDE --port 0 --device 0 --medium none")
'''
## Start the VM
def start_vm(VM_name):
    system("vboxmanage startvm " + VM_name + " --type headless")

## Delete the VM
def shutdown_vm(VM_name):
    system("vboxmanage shutdown " + VM_name)

def delete_vm(VM_name):
    system("vboxmanage unregistervm " + VM_name + " --delete")

def main(arg):
    ## Virtual Machine Info  
    VM_name = 'MiniDebian'
    OS_type = 'Debian_64'
    cpu = str(2)
    ram = str(2048)
    disk_size = str(8000)
    NAT2 = 'en0'
    if arg == 'stop':
        shutdown_vm(VM_name)
    elif arg == 'start':
        start_vm(VM_name)
    elif arg == 'delete':
        shutdown_vm(VM_name)
        delete_vm(VM_name)
    else:
        configure_vm(VM_name, cpu, ram, OS_type)

if __name__ == '__main__':
    i = 0
    while sys.argv[i:]:
        i += 1
    if i > 2:
        print(__name__ + ' cannot take more than 2 arguments.\nUsage: ' + __name__ + ' [option]\nOptions:\n\tstart: start the VM\n\tstop: poweroff the VM\n\tdelete: stop and delete the VM with its disk\n')
    elif i == 1:
        main("")
    elif i == 2:
        main(sys.argv[1])

#print ("https://www.oracle.com/technetwork/articles/servers-storage-admin/manage-vbox-cli-2264359.html")
##print ("shasum < disk.vdi")
