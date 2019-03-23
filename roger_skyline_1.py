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

import os

## Get the path
path = os.getcwd()

## Get the Debian iso()
def download_iso()
    os.system("curl -O http://ftp.nl.debian.org/debian/dists/stretch/main/installer-amd64/current/images/netboot/mini.iso")

## Adding the preseed.cfg file to Initrd
def launch_build()
    os.system("./build_iso.sh")

## Create and configure the VM
def configure_vm(VM_name, cpu, ram, OS_type, disk_size)
    os.system("VBoxManage createvm --name " + VM_name + " --ostype " + OS_type + " --register")
    os.system("VBoxManage modifyvm " + VM_name + " --cpus " + str(cpu) + " --memory " + str(ram))
    create_disk(VM_name, disk_size)
    boot_order(VM_name)
    #BUG#os.system("VBoxManage modifyvm " + VM_name + " --nic2 bridged  --bridgeadapter1 " + NAT2)

## Mount the iso on the VM
## Create and mount the disk vdi
def create_disk(VM_name, disk_size):
    os.system("VBoxManage storagectl " + VM_name + " --name IDE --add ide")
    os.system("VBoxManage storageattach " + VM_name + " --storagectl IDE --port 0 --device 0 --type dvddrive --medium preseed-mini.iso")
    os.system("VBoxManage storagectl " + VM_name + " --name SATA --add SATA")
    os.system("vboxmanage createmedium disk --filename diskdebianmini --size " + disk_size + " --format VDI")
    os.system("VBoxManage storageattach " + VM_name + " --storagectl SATA --port 0 --device 0 --type hdd --medium diskdebianmini.vdi")

## Boot order
def boot_order(VM_name):
    os.system("vboxmanage modifyvm " + VM_name + " --boot1 disk")
    os.system("vboxmanage modifyvm " + VM_name + " --boot2 dvd")
    os.system("vboxmanage modifyvm " + VM_name + " --boot3 none")

## Unmount the iso from the VM
def unmount_iso(VM_name)
    os.system("VBoxManage storageattach " + VM_name + " --storagectl IDE --port 0 --device 0 --medium none")

## Start the VM
def start_vm(VM_name)
    os.system("vboxmanage startvm " + VM_name + " --type headless")

## Delete the VM
def shutdown_vm(VM_name)
    os.system("vboxmanage shutdown " + VM_name)

def delete_vm(VM_name)
    os.system("vboxmanage unregistervm " + VM_name + " --delete")

def main():
    ## Virtual Machine Info
    VM_name = "MiniDebian"
    OS_type = "Debian_64"
    cpu = 2
    ram = 2048
    disk_size = 8000
    NAT2 = "en0"
    # Functions call
    download_iso()
    configure_vm(VM_name, cpu, ram, OS_type)

if __name__ == '__main__':
    main()
#print ("https://www.oracle.com/technetwork/articles/servers-storage-admin/manage-vbox-cli-2264359.html")
##print ("shasum < disk.vdi")
