# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parser.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/04/12 18:02:46 by abarthel          #+#    #+#              #
#    Updated: 2019/04/17 09:39:30 by abarthel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def parser(filename):
    dinfo = {}
    info = open(filename)
    for line in info:
        line = line.split(" = ")
        dinfo[line[0]] = line[1].strip("\n")
    return (dinfo)
