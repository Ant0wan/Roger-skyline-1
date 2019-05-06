# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    shutdown.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/25 18:26:40 by abarthel          #+#    #+#              #
#    Updated: 2019/05/06 12:33:57 by abarthel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from os import system

def shutdown_vm(VM_name):
    system("vboxmanage controlvm " + VM_name + " acpipowerbutton")
