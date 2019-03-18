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

## Virtual Machine Info
VM_name = "MiniDebian"
VM_type = "Debian_64"
cpu = 2
RAM = 2048
NAT2 = "en0"

## Get the Debian iso
#os.system("curl -O http://ftp.nl.debian.org/debian/dists/stretch/main/installer-amd64/current/images/netboot/mini.iso")


## Adding the preseed.cfg file to Initrd
#os.system("./build_iso.sh")

## Create and configure the VM
os.system("VBoxManage createvm --name MiniDebian --ostype Debian_64 --register")
os.system("VBoxManage modifyvm " + VM_name + " --cpus " + str(cpu) + " --memory " + str(RAM))
#BUG#os.system("VBoxManage modifyvm " + VM_name + " --nic2 bridged  --bridgeadapter1 " + NAT2)
os.system("VBoxManage storagectl " + VM_name + " --name IDE --add ide")
os.system("VBoxManage storagectl " + VM_name + " --name SATA --add SATA")

## Mount the iso on the VM
os.system("VBoxManage storageattach " + VM_name + " --storagectl IDE --port 0 --device 0 --type dvddrive --medium preseed-mini.iso")

## Create and mount the disk vdi
os.system("vboxmanage createmedium disk --filename diskdebianmini --size 8000 --format VDI")
os.system("VBoxManage storageattach " + VM_name + " --storagectl SATA --port 0 --device 0 --type hdd --medium diskdebianmini.vdi")
#OLD#os.system("VBoxManage storagectl " + VM_name + " --name diskdebianmini.vdi --add ide --bootable on")

## Boot order
os.system("vboxmanage modifyvm " + VM_name + " --boot1 disk")
os.system("vboxmanage modifyvm " + VM_name + " --boot2 dvd")
os.system("vboxmanage modifyvm " + VM_name + " --boot3 none")

## Unmount the iso from the VM
#os.system("VBoxManage storageattach " + VM_name + " --storagectl IDE --port 0 --device 0 --medium none")

## Start the VM
#os.system("vboxmanage startvm " + VM_name + " --type headless")

## Delete the VM
#os.system("vboxmanage shutdown " + VM_name)
#os.system("vboxmanage unregistervm " + VM_name + " --delete")
#print ("https://www.oracle.com/technetwork/articles/servers-storage-admin/manage-vbox-cli-2264359.html")
##print ("shasum < disk.vdi")
