#!/usr/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    createvm.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/25 18:26:40 by abarthel          #+#    #+#              #
#    Updated: 2019/02/25 18:26:40 by abarthel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from os import system

def configure_vm(dinfo):
    system("vboxmanage createvm --name " + dinfo['VM_name'] \
            + " --ostype " + dinfo['OS_type'] + " --register")
    system("vboxmanage modifyvm " + dinfo['VM_name'] \
            + " --cpus " + dinfo['cpu'] \
            + " --memory " + dinfo['ram'])
    create_disk(dinfo['VM_name'], dinfo['disk_size'], dinfo['iso_path'])
    boot_order(dinfo['VM_name'])
#BUG#    system("VBoxManage modifyvm " + VM_name + " --nic2 bridged  --bridgeadapter1 " + NAT2)

def create_disk(VM_name, disk_size, iso_path):
    storage = ('IDE', 'SATA')
    disk_name = 'diskdebianmini'
    disk_file_format = 'vdi'
    disk_type = 'hdd'
    for a_type in storage:
        system("VBoxManage storagectl " + VM_name \
                + " --name " + a_type + " --add " + a_type)
    system("VBoxManage storageattach " + VM_name \
            + " --storagectl " + storage[0] \
            + " --port 0 --device 0 --type dvddrive" \
            + " --medium " + iso_path)
    system("vboxmanage createmedium disk --filename " + disk_name \
            + " --size " + disk_size + " --format " + disk_file_format)
    system("VBoxManage storageattach " + VM_name \
            + " --storagectl " + storage[1] \
            + " --port 0 --device 0 --type " + disk_type \
            + " --medium " + disk_name + "." + disk_file_format)

## Boot order
def boot_order(VM_name):
    boot_devices = ('disk', 'dvd', 'none')
    for device in boot_devices:
        system("vboxmanage modifyvm " + VM_name \
                + " --boot" + str(boot_devices.index(device) + 1) \
                + " " + device)

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
    system("vboxmanage controlvm " + VM_name + " acpipowerbutton")

def delete_vm(VM_name):
    system("vboxmanage unregistervm " + VM_name + " --delete")

#print ("https://www.oracle.com/technetwork/articles/servers-storage-admin/manage-vbox-cli-2264359.html")
##print ("shasum < disk.vdi")
