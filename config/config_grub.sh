#!/bin/sh
echo $1 | sudo -S sed -i 's/GRUB_TIMEOUT=5/GRUB_TIMEOUT=0/g'
echo $1 | sudo -S update-grub
