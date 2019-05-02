#!/bin/sh
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    network_n_security.sh                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/05/02 14:07:35 by abarthel          #+#    #+#              #
#    Updated: 2019/05/02 14:07:35 by abarthel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

SUDO_PSSWD='root'

## Change SSH ports
# Server
echo $SUDO_PSSWD | sudo -S sed -n -i 'p;13a Port 2266'  /etc/ssh/sshd_config >/dev/null
# Client
echo $SUDO_PSSWD | sudo -S sed -n -i 'p;41a Port 2266'  /etc/ssh/ssh_config >/dev/null

## Change netmask
echo "root" | sudo -S sed -n -i 'p;14a \\tnetmask 255.255.255.252'  /etc/network/interfaces
