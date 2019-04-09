#!/bin/bash

## Adding the preseed.cfg file to Initrd
apt-get install -y curl
apt-get install -y bsdtar
apt-get install -y gzip
apt-get install -y genisoimage
curl -O http://ftp.nl.debian.org/debian/dists/stretch/main/installer-amd64/current/images/netboot/mini.iso
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
