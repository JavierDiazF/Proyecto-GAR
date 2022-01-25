
IP=$1
FILE="/home/ubuntu/redireccion/clave/manager-vm"

sudo bash -c 'echo -e "Match Address '${IP}' \n \t ForceCommand ssh -i '${FILE}' diego@35.184.140.141" >> /etc/ssh/sshd_config'

sudo service ssh restart
