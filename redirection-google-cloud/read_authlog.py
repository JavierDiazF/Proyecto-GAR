from pathlib import Path 
import os 


#CONSTANTS
FILE_NAME = "/var/log/auth.log"
NUMBER_WORDS_LINE_FAILED_PASSWORD = 15

#GLOBAL VARIABLES
bytes_file = 0




def read_file(file_name):
    auth_file = open(file_name, 'r')
    try:
        auth_file.seek(bytes_file)
        for line in auth_file:
            word_list = line.split('\n')[0].split() #split by space
            number_words = len(word_list)
            if number_words == NUMBER_WORDS_LINE_FAILED_PASSWORD:
                #print (line.split('\n')[0])
                if word_list[5] == "Connection" and word_list[6] == "closed" and word_list[8] == "authenticating":
                    ip = word_list[11]
                    #print(ip)
                    command = "echo  "+ ip + " >> /home/ubuntu/redireccion/ip_addresses.txt" 
                    os.system(command) 
            

    
    finally:
        auth_file.close()


if __name__ == "__main__":
    while True:
        file_size = Path(FILE_NAME).stat().st_size
        if bytes_file < file_size:
            read_file(FILE_NAME)

        bytes_file = file_size

