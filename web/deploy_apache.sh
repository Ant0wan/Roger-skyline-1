#!/bin/sh
echo $1 | sudo -S apt-get install -y apache2
echo $1 | sudo -S sed -i 's/DocumentRoot \/var\/www\/html/DocumentRoot \/home\/antoine\/www\//g' /etc/apache2/sites-available/000-default.conf
