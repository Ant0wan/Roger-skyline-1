#!/bin/sh
echo $1 | sudo -S apt-get install -y apache2
#echo $1 | sudo -S sed -i 's/DocumentRoot \/var\/www\/html/DocumentRoot \/home\/antoine\/www\//g' /etc/apache2/sites-available/000-default.conf
echo $1 | sudo -S mkdir /home/antoine/www/
echo $1 | sudo -S wget -P /home/antoine/www/ https://raw.githubusercontent.com/Ant0wan/Roger-skyline-1/master/web/www/index.html
echo $1 | sudo -S sed -n -i "p;174a </Directory>" /etc/apache2/apache2.conf
echo $1 | sudo -S sed -n -i "p;174a \	Require all granted" /etc/apache2/apache2.conf
echo $1 | sudo -S sed -n -i "p;174a \	AllowOverride None" /etc/apache2/apache2.conf
echo $1 | sudo -S sed -n -i "p;174a \	Options FollowSymLinks" /etc/apache2/apache2.conf
echo $1 | sudo -S sed -n -i "p;174a <Directory /home/antoine/www/>" /etc/apache2/apache2.conf
echo $1 | sudo -S a2enmod ssl
echo $1 | sudo -S a2enmod rewrite
echo $1 | sudo -S mkdir /etc/apache2/ssl
echo $1 | sudo -S openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/apache2/ssl/apache.key -out /etc/apache2/ssl/apache.crt -subj "/C=FR/ST=France/L=Paris"
echo $1 | sudo -S sed -ie "s/ssl\/certs\/ssl-cert-snakeoil.pem/apache2\/ssl\/apache.crt/g" /etc/apache2/sites-available/default-ssl.conf
echo $1 | sudo -S sed -ie "s/ssl\/private\/ssl-cert-snakeoil.key/apache2\/ssl\/apache.key/g" /etc/apache2/sites-available/default-ssl.conf
echo $1 | sudo -S cat /etc/apache2/sites-available/default-ssl.conf | { cat -; } | sudo -S tee -a /etc/apache2/sites-available/000-default.conf
echo $1 | sudo -S sed -i 's/DocumentRoot \/var\/www\/html/DocumentRoot \/home\/antoine\/www\//g' /etc/apache2/sites-available/000-default.conf
echo $1 | sudo -S sed -n -i "p;21a \	Redirect permanent / https://"$2 /etc/apache2/sites-available/000-default.conf
echo $1 | sudo -S service apache2 reload
echo $1 | sudo -S systemctl restart apache2
