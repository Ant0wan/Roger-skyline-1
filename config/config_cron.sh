#!/bin/sh
echo $1 | sudo -S mkdir /etc/cron.update
echo $1 | sudo -S wget -P /etc/cron.update/ https://raw.githubusercontent.com/Ant0wan/Roger-skyline-1/master/config/update
echo $1 | sudo -S chmod 0766 update
echo $1 | sudo -S sed -n -i 'p;14a @reboot		root	test-x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.update )' /etc/crontab
