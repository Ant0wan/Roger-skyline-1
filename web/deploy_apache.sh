#!/bin/sh
echo $1 | sudo -S apt-get install -y apache2
echo $1 | sudo -S sed -i 's/DocumentRoot \/var\/www\/html/DocumentRoot \/home\/antoine\/www\//g' /etc/apache2/sites-available/000-default.conf
echo $1 | sudo -S sed -n -i 'p;170a <Directory /home/antoine/www/>
	Options FollowSymLinks
	AllowOverride None
	Require all granted
</Directory>' /etc/apache2/apache2.conf
echo $1 | sudo -S service apache2 reload
