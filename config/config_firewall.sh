#!/bin/sh
echo $1 | sudo -S apt-get install -y ufw
echo $1 | sudo -S ufw --force reset
echo $1 | sudo -S ufw default deny incoming
echo $1 | sudo -S ufw default deny outgoing
echo $1 | sudo -S ufw allow $2/tcp
echo $1 | sudo -S ufw allow out http
echo $1 | sudo -S ufw allow in http
echo $1 | sudo -S ufw allow out https
echo $1 | sudo -S ufw allow in https
echo $1 | sudo -S ufw allow out $3
echo $1 | sudo -S ufw logging on
echo $1 | sudo -S ufw --force enable
