#!/bin/sh
TCP_PORTS="1,7,9,11,15,70,79,80,109,110,111,119,138,139,143,512,513,514,515,540,635,1080,1524,2000,2001,4000,4001,5742,6000,6001,6667,12345,12346,20034,27665,30303,32771,32772,32773,32774,31337,40421,40425,49724,54320"
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
for i in $TCP_PORTS
do
	echo $1 | sudo -S ufw allow in $i
done
echo $1 | sudo -S ufw logging on
echo $1 | sudo -S ufw --force enable
