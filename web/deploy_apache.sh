#!/bin/sh
echo $1 | sudo -S apt-get install -y apache2
echo $1 | sudo -S sed -i 's/DocumentRoot \/var\/www\/html/DocumentRoot \/home\/antoine\/www\//g' /etc/apache2/sites-available/000-default.conf
echo $1 | sudo -S mkdir /home/antoine/www/
echo $1 | sudo -S wget -P /home/antoine/www/ https://raw.githubusercontent.com/Ant0wan/Roger-skyline-1/master/web/www/index.html
echo $1 | sudo -S sed -n -i "p;174a </Directory>" /etc/apache2/apache2.conf
echo $1 | sudo -S sed -n -i "p;174a \	Require all granted" /etc/apache2/apache2.conf
echo $1 | sudo -S sed -n -i "p;174a \	AllowOverride None" /etc/apache2/apache2.conf
echo $1 | sudo -S sed -n -i "p;174a \	Options FollowSymLinks" /etc/apache2/apache2.conf
echo $1 | sudo -S sed -n -i "p;174a <Directory /home/antoine/www/>" /etc/apache2/apache2.conf
echo $1 | sudo -S service apache2 reload
