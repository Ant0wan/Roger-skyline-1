#!/bin/sh
echo $1 | sudo -S mkdir /etc/cron.update
echo $1 | sudo -S wget -P /etc/cron.update/ https://raw.githubusercontent.com/Ant0wan/Roger-skyline-1/master/config/update
echo $1 | sudo -S chmod 0766 /etc/cron.update/update
echo $1 | sudo -S touch /var/log/update_script.log
echo $1 | sudo -S chmod 0640 /var/log/update_script.log
echo $1 | sudo -S mkdir /etc/cron.watch
echo $1 | sudo -S wget -P /etc/cron.watch/ https://raw.githubusercontent.com/Ant0wan/Roger-skyline-1/master/config/watch_crontab
echo $1 | sudo -S chmod 0766 /etc/cron.watch/watch_crontab
echo $1 | sudo -S touch /var/log/watch_crontab.log
echo $1 | sudo -S chmod 0640 /var/log/watch_crontab.log
echo $1 | sudo -S sed -n -i 'p;14a @reboot		root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.update )' /etc/crontab
echo $1 | sudo -S sed -n -i 'p;14a 00 4	* * 1	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.update )' /etc/crontab
echo $1 | sudo -S sed -n -i 'p;14a 00 0	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.watch )' /etc/crontab
