from pathlib import Path
import subprocess
import os

#variables gloables
bytes_file=0
ip_addresses = {}
ip_sent = {} 


def visualizar_ip():
    for ip in ip_addresses:
        print (ip.strip('\n'), ":", ip_addresses[ip], ip_sent[ip])



#funcion para leer archivo 
def read_file(filename):
    ip_file = open(filename, 'r')
    try: 
        ip_file.seek(bytes_file)
        for ip in ip_file:
            if not ip_addresses or ip_addresses.get(ip)==None:
                ip_addresses[ip] = int (1)
                ip_sent[ip] = int (0)
            else:
                ip_addresses[ip]=ip_addresses.get(ip) + 1
    finally:
        ip_file.close()




#funcion para enviar una direccion ip cuando esté repetida más de 3 veces (más de 3 intentos de conxión ssh fallidos)
#Cunado la direccin ip 
def redirect_ip():
    for ip in ip_addresses:
        if ip_addresses.get(ip)>=3:
            #si la ip no ha sido enviada
            if ip_sent.get(ip) == 0:
                #llamar a redirect.sh y enviarle direccion ip
                command = './redirect.sh ' + ip.strip('\n')
                os.system(command)
                ip_sent[ip]=int(1) #poner la direccion ip como enviada #flag_enviado
    

if __name__ == '__main__':
    filename = 'ip_addresses.txt'
    while True:
        file_size = Path(filename).stat().st_size
        if bytes_file < file_size:
            read_file(filename)
            redirect_ip()
            visualizar_ip()
            
        bytes_file = file_size
    
        
            
    
