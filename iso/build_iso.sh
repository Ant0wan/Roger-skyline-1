#!/bin/bash
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    build_iso.sh                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/04/10 13:02:22 by abarthel          #+#    #+#              #
#    Updated: 2019/04/10 13:02:22 by abarthel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

##
## CAUTION: This script will not run on 42's Macs. Run it on a Debian virtual
## machine as a root/sudo user.
##
## DESCRIPTION: The script will update packages concerning the tools needed
## for the image build.
## It will first download the mini.iso - a Debian version -  then modify it
## with the pressed.cfg and isolinux.cfg files in the current directory.
##

# Update packages
apt-get install -y curl
apt-get install -y bsdtar
apt-get install -y gzip
apt-get install -y genisoimage

# Download mini.iso
curl -O http://ftp.nl.debian.org/debian/dists/stretch/main/installer-amd64/current/images/netboot/mini.iso

# Extract, modify then build the iso
mkdir ./DESTINATION/
bsdtar -C ./DESTINATION/ -xf mini.iso
chmod +w -R ./DESTINATION/
cd ./DESTINATION/
gunzip initrd.gz
echo ../preseed.cfg | cpio -H newc -o -A -F initrd
gzip initrd
cp -f ../isolinux.cfg ./
cd ..
chmod -w -R ./DESTINATION/
cd ./DESTINATION/
md5sum `find -follow -type f` > md5sum.txt
cd ..
genisoimage -r -J -b isolinux.bin -c boot.cat -no-emul-boot -boot-load-size 4 -boot-info-table -o preseed-mini.iso ./DESTINATION/
rm -rf ./DESTINATION/ mini.iso
