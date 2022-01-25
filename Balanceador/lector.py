#!/usr/bin/python3

import os
import sys

def incluye(ip):
    cadena = "\tserver "+ ip + ';\n'
    with open("/home/ubuntu/balanceador/default.conf", 'r') as file:
        newline=file.readlines()
    #Comprobamos si ya está esa ip
    ya_presente = False
    for i in newline:
        if i == cadena:
            print('La ip ya está incluida en el archivo')
            ya_presente = True
    if not ya_presente:
        for i in newline:
            if i == '\t#SERVIDORES\n':
                newline.insert(newline.index(i) +1 , cadena)

    with open("/home/ubuntu/balanceador/default.conf", "w") as file:
        for i in newline:
            file.writelines(i);

def elimina(ip):
    cadena = "\tserver "+ ip + ';\n'
    with open("/home/ubuntu/balanceador/default.conf", 'r') as file:
        newline=file.readlines()
    for i in newline:
        if i == cadena:
            newline.pop(newline.index(i))
    with open("/home/ubuntu/balanceador/default.conf", "w") as file:
        for i in newline:
            file.writelines(i);


if __name__ == "__main__":
    #incluye(sys.argv[1])

    if sys.argv[1] == "incluye":
        incluye(sys.argv[2])
    else:
        elimina(sys.argv[2])
