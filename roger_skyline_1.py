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
os.system("curl -O http://ftp.nl.debian.org/debian/dists/stretch/main/installer-amd64/current/images/netboot/mini.iso")


## Adding the preseed.cfg file to Initrd
#os.system("./build_iso.sh")
os.system("mkdir ./DESTINATION/")
os.system("bsdtar -C ./DESTINATION/ -xf mini.iso")
os.system("chmod +w -R ./DESTINATION/")
os.system("cd ./DESTINATION/")
os.system("gunzip initrd.gz")
os.system("echo ../preseed.cfg | cpio -H newc -o -A -F initrd")
os.system("gzip initrd")
os.system("cp -f ../isolinux.cfg ./")
os.system("cd ..")
os.system("chmod -w -R ./DESTINATION/")
os.system("cd ./DESTINATION/")
os.system("md5sum `find -follow -type f` > md5sum.txt")
os.system("cd ..")
os.system("genisoimage -r -J -b isolinux.bin -c boot.cat -no-emul-boot -boot-load-size 4 -boot-info-table -o preseed-mini.iso ./DESTINATION/")
os.system("rm -rf ./DESTINATION/")

## Create and configure the VM
os.system("VBoxManage createvm --name MiniDebian --ostype Debian_64 --register")
os.system("VBoxManage modifyvm " + VM_name + " --cpus " + str(cpu) + " --memory " + str(RAM))
#BUG #os.system("VBoxManage modifyvm " + VM_name + " --nic2 bridged  --bridgeadapter1 " + NAT2)
os.system("VBoxManage storagectl " + VM_name + " --name IDE --add ide")

## Mount the iso on the VM
os.system("VBoxManage storageattach " + VM_name + " --storagectl IDE --port 0 --device 0 --type dvddrive --medium mini.iso")

## Unmount the iso from the VM
#os.system("VBoxManage storageattach " + VM_name + " --storagectl IDE --port 0 --device 0 --medium none")

## Start the VM
#os.system("vboxmanage startvm " + VM_name + " --type headless")

## Delete the VM
#os.system("vboxmanage shutdown " + VM_name)
#os.system("vboxmanage unregistervm " + VM_name + " --delete")
#print ("https://www.oracle.com/technetwork/articles/servers-storage-admin/manage-vbox-cli-2264359.html")
##print ("shasum < disk.vdi")
