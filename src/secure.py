# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    secure.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/25 18:26:40 by abarthel          #+#    #+#              #
#    Updated: 2019/05/06 12:33:32 by abarthel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from os import system
from time import sleep
from src.start import start_vm
from src.shutdown import shutdown_vm

## Secure the VM
def secure_vm(dinfo):
    sleep(5)
    system("vboxmanage startvm " + dinfo['VM_name'] + " --type headless")
    while system("ping -c 1 -t 1 " + dinfo['ip_vm'] + " >/dev/null"):
        sleep(1)
    load_scripts(dinfo)
    shutdown_vm(dinfo['VM_name'])
    print ("\nThe VM has been successfully secured." \
            "\nThe VM is now powered off.")

def load_scripts(dinfo):
    system("ssh -o 'StrictHostKeyChecking no' -i ~/.ssh/id_rsa " + \
            dinfo['user'] + "@" + dinfo['ip_vm'] + \
            " 'sh -s' < config/config_ssh.sh")
    print ("\nSSH has been configured.")
    system("ssh -p " + dinfo['ssh_port'] + " " + \
            dinfo['user'] + "@" + dinfo['ip_vm'] + \
            " 'sh -s' < config/config_network.sh")
    print ("\nNetwork has been configured.")

def rsa_gen():
    system("ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa -N ''")
    system("mv ~/.ssh/id_rsa.pub ~/Roger-skyline-1/config/authorized_keys")
    system("git add config/authorized_keys" \
            "&& git commit -m 'upload ssh pub key'" \
            " && git push")
