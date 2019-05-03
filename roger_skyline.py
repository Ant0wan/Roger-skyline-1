#!/usr/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    roger_skyline.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/04/12 14:40:52 by abarthel          #+#    #+#              #
#    Updated: 2019/04/12 14:40:52 by abarthel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from os import system, getcwd
from src.parser import parser
from src.createvm import configure_vm
from src.shutdown import shutdown_vm
from src.install_os import install_os
from src.delete import delete_vm
from src.start import start_vm
from src.secure import secure_vm
from src.secure import rsa_gen

info = "info"
path = getcwd()

def main(arg):
    dinfo = parser(info)
    if arg == 'stop':
        shutdown_vm(dinfo['VM_name'])
    elif arg == 'start':
        start_vm(dinfo['VM_name'])
    elif arg == 'delete':
        shutdown_vm(dinfo['VM_name'])
        delete_vm(dinfo['VM_name'])
    else:
        configure_vm(dinfo)
        rsa_gen()
        install_os(dinfo['VM_name'])
        secure_vm(dinfo['VM_name'])

if __name__ == '__main__':
    i = 0
    while sys.argv[i:]:
        i += 1
    if i > 2:
        print(__name__ + ' cannot take more than 2 arguments.\nUsage: ' \
                + __name__ + \
                ' [option]\nOptions:\n\tstart\tstarts the VM' + \
                '\n\tstop\tpoweroff the VM' + \
                '\n\tdelete\tstops and deletes the VM with its disk\n')
    elif i == 1:
        main("")
    elif i == 2:
        main(sys.argv[1])
