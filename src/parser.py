# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parser.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/04/12 18:02:46 by abarthel          #+#    #+#              #
#    Updated: 2019/04/12 18:38:46 by abarthel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def parser(dict_):
    info = open("info")
    for line in info:
        line = line.split(" = ")
        dict_[line[0]] = line[1].strip("\n")
