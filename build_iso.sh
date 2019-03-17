#!/bin/bash

## Adding the preseed.cfg file to Initrd
mkdir DESTINATION
bsdtar -C DESTINATION -xf preseed-mini.iso
chmod +w DESTINATION/initrd.gz
gunzip DESTINATION/initrd.gz
echo preseed.cfg | cpio -H newc -o -A -F initrd
gzip initrd
chmod -w DESTINATION/initrd.gz

## Fixing the md5sum
md5sum `find -follow -type f` > md5sum.txt
genisoimage -r -J -b isolinux.bin -c boot.cat -no-emul-boot -boot-load-size 4 -boot-info-table -o preseed-mini.iso ./DESTINATION/
