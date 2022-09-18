# Info de la materia:
ST0263 - Tópicos Especiales en Telemática
# Estudiante:
Daniela Ximena Niño Barbosa, dxninob@eafit.edu.co
# Profesor:
Edwin Nelson Montoya Munera, emontoya@eafit.edu.co


# 1. Breve descripción de la actividad
Desarrollar habilidades en el proceso de creación, despliegue y gestión de aplicaciones utilizando contenedores y aprender a asignar un certificado ssl válido a un dominio en Let's Encrypt.


## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor
- Desplegar un servidor de wordpress en una máquina virtual usando contenedores Docker.
- Asignarle un nombre de dominio a la dirección IP elástica del servidor.
- Asgnarle al nombre de dominio del servidor, un certificado ssl válido.


## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor
Todo lo propuesto ha sido implementado.


# 2. Información general de diseño
Se usaron contenedores Docker para la intalación de Wordpress en la máquina virtual.


# 3. Descripción del ambiente de desarrollo, técnico y de ejecución
## IP o nombres de dominio
- IP elástica: 35.209.90.230
- Nombre de dominio: danielanino.tk
- Dominio con certificación SSL: https://www.danielanino.tk


## Detalles técnicos
- GCP: se usó para desplegar una máquina virtual.
- Docker: se usó un contenedor para desplegar un wordpress.
- Cerbot: se usó para asiganar un certificado SSL válido.
- Let's Encrypt: se usó para asiganar un certificado SSL válido.
- Nginx: se usó como servidor web HTTP.


## Descripción y como se configura el proyecto
Crear una instancia en GCP:
- Se ingresa a GCP (console.cloud.google.com).
- Se da click en el *Menú de navegación*.
- Se da click en *Compute Engine*.
- Se da click en *Instancias de VM*.
- Se da click en *CREAR INSTANCIA*.
- Se configura el nombre de la instancia, se elige el tipo de máquina ec2-micro y se habilita el tráfico HTTP y HTTPS.
- Se da click en *CREAR*.
<img width="728" alt="1 instancia" src="https://user-images.githubusercontent.com/60080916/190926653-de1c6c03-bd2d-4d93-8b30-ba88342398d5.PNG">

Configurar la IP elástica de la máquina virtual:
- Se ingresa a GCP (console.cloud.google.com).
- Se da click en el *Menú de navegación*.
- Se da click en *Red de VPC*.
- Se da click en *Direcciones IP*.
- Se da click en *RESERVAR DIRECCIÓN ESTÁTICA EXTERNA*.
- Se cambian los parámetros para crear la dirección IP elástica.  Se asigna el nombre de la IP, se selecciona la Versión de IP como IPv4 y se asigna la instancia creada anteriormente.
- Se da click en *RESERVAR*.
<img width="766" alt="2 elastica" src="https://user-images.githubusercontent.com/60080916/190926666-efd4b474-09e4-46b8-8fcf-f564f5eed82a.PNG">

Configurar los registros DNS en GCP:
- Se ingresa a GCP (console.cloud.google.com).
- En la barra de busqueda superior se ingresa "Servicios de red" y se selecciona la primera opción.
- Se da click en *Cloud DNS*.
- Se da click en "CREAR ZONA".
- Se configuran los parámetros de la zona.
- En *AGREGAR CONJUNTO DE REGISTROS* se deben crear los registros A y CNAME (posteriormente se tendrá que crear el TXT).
<img width="726" alt="3 registros" src="https://user-images.githubusercontent.com/60080916/190926678-07db2c95-daf5-4272-b94a-ddde1aaafa4b.PNG">

Configurar los servidores de nombres en Freenom:
- Nos ubicamos en la administración del dominio.
- Se selecciona "Use custom nameservers (enter below)".
- Se agregan los dominios NS que nos brinda GCP.
<img width="732" alt="4 1 txt" src="https://user-images.githubusercontent.com/60080916/190926691-deefe49d-afd4-4e80-bffa-56e2f04ca7d8.PNG">
<img width="945" alt="4 2 freenom" src="https://user-images.githubusercontent.com/60080916/190926694-5e510441-2ac5-417f-bbc7-3b941c2baec8.PNG">


## Como se lanza el servidor
Para ingresar a la máquina virtual, nos debemos conectar por SSH:
- Se ingresa a GCP (console.cloud.google.com).
- Se da click en el *Menú de navegación*.
- Se da click en *Compute Engine*.
- Se da click en *Instancias de VM*.
- Buscamos nuestra instancia y damos click en *SSH*.


## Detalles del desarrollo
### Instalar certbot, letsencrypt y nginx
Ejecutamos los siguientes comandos:
```
sudo apt update
sudo apt install snapd
sudo snap install certbot --classic
sudo apt install letsencrypt -y
sudo apt install nginx -y
```

### Configurar nginx.conf
Entramos al archivo de configuración:
```
sudo nano /etc/nginx/nginx.conf
```

Cambiamos el contenido por el siguiente:
```
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

events {
    worker_connections  1024;  ## Default: 1024
}
http {
    server {
        listen  80 default_server;
        server_name _;
        location ~ /\.well-known/acme-challenge/ {
            allow all;
            root /var/www/letsencrypt;
            try_files $uri = 404;
            break;
        }
    }
}
```

Guardamos la configuración de nginx:
```
sudo mkdir -p /var/www/letsencrypt
sudo nginx -t
sudo service nginx reload
```

### Pedir los certificados SSL
Ejecutamos los siguientes comandos:
```
sudo letsencrypt certonly -a webroot --webroot-path=/var/www/letsencrypt -m dxninob@eafit.edu.co --agree-tos -d www.danielanino.tk
sudo certbot --server https://acme-v02.api.letsencrypt.org/directory -d *.danielanino.tk --manual --preferred-challenges dns-01 certonly
```
Cuando ejecutamos este último comando, tenemos que crear el registro TXT como se explica más adelante.

Creamos carpetas para nuestro wordpress y los certficados:
```
mkdir /home/dxninob/wordpress
mkdir /home/dxninob/wordpress/ssl
```

Ejecutamos los siguientes comandos para hacer los registros:
```
sudo su
cp /etc/letsencrypt/live/www.danielanino.tk/* /home/dxninob/wordpress/ssl/
cp /etc/letsencrypt/live/danielanino.tk/* /home/dxninob/wordpress/ssl/
```

### Crear el Wordpress
Instalamos docker, docker-compose y git:
```
sudo apt install docker.io -y
sudo apt install docker-compose -y
sudo apt install git -y
```

Poner a funcionar docker:
```
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -a -G docker dxninob
sudo reboot
```

Clonamos un repositorio de donde usaremos los archivos de configuración:
```
git clone https://github.com/st0263eafit/st0263-2022-2.git
cd st0263-2022-2/docker-nginx-wordpress-ssl-letsencrypt
sudo cp docker-compose.yml /home/dxninob/wordpress
sudo cp nginx.conf /home/dxninob/wordpress
sudo cp ssl.conf /home/dxninob/wordpress
```

Detenemos nginx:
```
ps ax | grep nginx
netstat -an | grep 80
sudo systemctl disable nginx
sudo systemctl stop nginx
```

Inciamos el servidor Wordpress:
```
cd /home/dxninob/wordpress
docker-compose up --build -d
```


## Como un usuario lo utilizaría
El usuario solo debe acceder a la URL https://www.danielanino.tk desde cualquier browser.


## Resultados
Podemos ver que la URL empieza por https://
<img width="960" alt="5 pagina" src="https://user-images.githubusercontent.com/60080916/190926718-9cf081d5-0530-446b-98c3-e3f326e90367.PNG">

Podemos ver el certificado SSL:
<img width="960" alt="6 ssl" src="https://user-images.githubusercontent.com/60080916/190926736-a28dfcd8-6c93-40ff-80af-0e7b0c99ac5c.PNG">


# 5. Información relevante
## Referencias:
https://github.com/st0263eafit/st0263-2022-2/tree/main/docker-nginx-wordpress-ssl-letsencrypt
