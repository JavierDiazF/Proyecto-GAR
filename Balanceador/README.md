# Balanceador

Se encarga de repartir la carga entre los servidores web, que se encuentran en la red interna privada de Google Cloud
Estos servidores web arrancan el servicio con el siguiente comando, que usa el rsyslog para notificar al balanceador:

`docker run --log-driver syslog --log-opt syslog-address=udp://10.0.0.2:514 --log-opt tag=docker --rm -p80:5000 -e HOSTNAME=$HOSTNAME -it javierdf/servidor_web`

## Archivos:

- balanceador/default.conf: Archivo que defineel servicio de balanceo de carga. Lo montamos en el contenedor nginx con el siguiente comando:

`docker run --name balanceador --log-driver syslog --log-opt syslog-address=udp://10.0.0.2:514 --log-opt tag=balanceador -p80:80 --rm -v $(pwd)/balanceador/default.conf:/etc/nginx/conf.d/default.conf nginx`

- telegraf.conf: Debe situarse en el directorio /etc/rsyslog.d/ y es el que configura el balanceador para que escuche los mensajes de rsyslog

- swatchdog/docker.conf: Archivo de configuración de swatchdog. Previamente debemos haber instalado swacthdog con`sudo apt install swatch`. 
    Indica al balanceador que cuando se lea una nueva entrada en el archivo que guarda los logs generados por los servidores `/var/log/remote/docker.conf`, actualice el archivo de configuración del balanceador y reinicie el docker nginx
    Lo arrancamos con el siguiente comando:

    `swatchdog -c swatchdog/docker.conf -t /var/log/remote/docker.log --daemon`

- lector.py: Reescribe el archivo que define los servidores disponibles para el reparto de carga.
    Así añade o elimina los servidores en función de si están disponibles o no
