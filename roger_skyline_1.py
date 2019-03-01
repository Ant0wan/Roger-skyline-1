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

# Get the path
path = os.getcwd()

# Virtual Machine Info
VM_name = "MiniDebian"
VM_type = "Debian_64"
cpu = 4
RAM = 4096
NAT2 = "en0"

# Get the Debian iso
os.system("curl -O http://ftp.nl.debian.org/debian/dists/stretch/main/installer-amd64/current/images/netboot/mini.iso")

#print ("shasum < disk.vdi")
os.system("VBoxManage createvm --name MiniDebian --ostype Debian_64 --register")
os.system("VBoxManage modifyvm " + VM_name + " --cpus " + str(cpu) + " --memory " + str(RAM))
os.system("VBoxManage modifyvm " + VM_name + " --nic2 bridged  --bridgeadapter1 " + NAT2)

print ("https://www.oracle.com/technetwork/articles/servers-storage-admin/manage-vbox-cli-2264359.html")
