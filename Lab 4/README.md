# Info de la materia:
ST0263 - Tópicos Especiales en Telemática
# Estudiante:
Daniela Ximena Niño Barbosa, dxninob@eafit.edu.co
# Profesor:
Edwin Nelson Montoya Munera, emontoya@eafit.edu.co


# 1. Breve descripción de la actividad
Desplegar un CMS wordpress empleando la tecnología de contenedores, con un nombre de dominio y certificado SSL.  Se utiliza un nginx tanto como frontend para el dominio y certificado y un balanceador de cargas para la capa de aplicación del wordpress.  Se utiliza un servidor de base de datos y otro para archivos (NFS server).


## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor
- Hacer la implementación el Google GCP.
- Evolucionar la aplicación original (lab3) dockerizada monolítica en varios nodos que mejore la disponibilidad de esta aplicación.
- Implementar un balanceador de cargas basado en nginx que reciba el tráfico web https de Internet con múltiples instancias de procesamiento.
- Tener al menos 2 instancias de procesamiento detrás del balanceador de cargas.
- Tener al menos 1 instancia de bases de datos mysql
- Tener al menos 1 instancia de archivos distribuidos en NFS.


## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor
Todo lo propuesto ha sido implementado.



# 2. Información general de diseño
Se usaron contenedores Docker para la instalación de Wordpress, nginx y MySQL en la máquina virtual.



# 3. Descripción del ambiente de desarrollo, técnico y de ejecución
## IP o nombres de dominio
- IP elástica: 35.208.215.54
- Nombre de dominio: lab4.danielanino.tk
- Dominio con certificación SSL: https://lab4.danielanino.tk

## Detalles técnicos
- GCP: se usó para desplegar una máquina virtual.
- Docker: se usó un contenedor para desplegar un wordpress.
- Cerbot: se usó para asiganar un certificado SSL válido.
- Let's Encrypt: se usó para asiganar un certificado SSL válido.
- Nginx: se usó como servidor web HTTP.
- NFS kernel server: se usó para hacer el servidor NFS.
- NFS common: se usó para vincular los wordpress con el servidor NFS.

## Descripción y como se configura el proyecto
Se deben crear cinco VM en GCP.  Cada una se crea así:
- Se ingresa a GCP (console.cloud.google.com).
- Se da click en el *Menú de navegación*.
- Se da click en *Compute Engine*.
- Se da click en *Instancias de VM*.
- Se da click en *CREAR INSTANCIA*.
- Se configura el nombre de la instancia, se elige el tipo de máquina ec2-micro y se habilita el tráfico HTTP y HTTPS.
- Se da click en *CREAR*.

Se configura la IP elástica para cada una de las VM.  Cada IP elástica se configura así:
- Se ingresa a GCP (console.cloud.google.com).
- Se da click en el *Menú de navegación*.
- Se da click en *Red de VPC*.
- Se da click en *Direcciones IP*.
- Se da click en *RESERVAR DIRECCIÓN ESTÁTICA EXTERNA*.
- Se cambian los parámetros para crear la dirección IP elástica.  Se asigna el nombre de la IP, se selecciona la Versión de IP como IPv4 y se asigna la instancia creada anteriormente.
- Se da click en *RESERVAR*.

Para la VM del balanceador de cargas, se configuran los registros DNS en GCP:
- Se ingresa a GCP (console.cloud.google.com).
- En la barra de busqueda superior se ingresa "Servicios de red" y se selecciona la primera opción.
- Se da click en *Cloud DNS*.
- Se da click en "CREAR ZONA".
- Se configuran los parámetros de la zona.
- En *AGREGAR CONJUNTO DE REGISTROS* se deben crear los registros A y CNAME (posteriormente se tendrá que crear el TXT).

Configurar los servidores de nombres en Freenom:
- Nos ubicamos en la administración del dominio.
- Se selecciona "Use custom nameservers (enter below)".
- Se agregan los dominios NS que nos brinda GCP.
<img width="732" alt="4 1 txt" src="https://user-images.githubusercontent.com/60080916/190926691-deefe49d-afd4-4e80-bffa-56e2f04ca7d8.PNG">
<img width="945" alt="4 2 freenom" src="https://user-images.githubusercontent.com/60080916/190926694-5e510441-2ac5-417f-bbc7-3b941c2baec8.PNG">

## Como se lanza el servidor
### Opción 1
Para ingresar a la máquina virtual, nos debemos conectar por SSH:
- Se ingresa a GCP (console.cloud.google.com).
- Se da click en el *Menú de navegación*.
- Se da click en *Compute Engine*.
- Se da click en *Instancias de VM*.
- Buscamos nuestra instancia y damos click en *SSH*.

### Opción 2
Para ingresar a la máquina virtual, nos debemos conectar por SSH:
- Tenemos que tener descargada la clave con la que está asociada nuestra instancia.
- Entramos a la terminal de nuestro computador.
- En la terminal, nos ubicamos en la carpeta donde se encuentra nuestra clave.
- Ejecutamos el comando: ```ssh -i dxninob dxninob@dirIP```

## Detalles del desarrollo
### 1. Balanceador de Cargas
Instalamos certbot, letsencrypt y nginx.  Para esto, ejecutamos los siguientes comandos:
```
sudo apt update
sudo apt install snapd
sudo snap install certbot --classic
sudo apt install letsencrypt -y
sudo apt install nginx -y
```

Configuramos el archivo nginx.conf.  De esta forma podemos entrar al archivo de configuración:
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

Pedimos los certificados SSL con los siguientes comandos:
```
sudo letsencrypt certonly -a webroot --webroot-path=/var/www/letsencrypt -m dxninob@eafit.edu.co --agree-tos -d lab4.danielanino.tk
sudo certbot --server https://acme-v02.api.letsencrypt.org/directory -d *.danielanino.tk --manual --preferred-challenges dns-01 certonly
```
- **Nota:** Cuando ejecutamos este último comando, tenemos que crear el registro TXT como se explicó anteriormente.

Creamos carpetas para nuestro balanceador y los certficados:
```
mkdir /home/dxninob/nginx
mkdir /home/dxninob/nginx/ssl
```

Ejecutamos los siguientes comandos para hacer los registros:
```
sudo su
cp /etc/letsencrypt/live/lab4.danielanino.tk/* /home/dxninob/nginx/ssl/
cp /etc/letsencrypt/live/danielanino.tk/* /home/dxninob/nginx/ssl/
exit
```

Instalamos docker, docker-compose y git:
```
sudo apt install docker.io -y
sudo apt install docker-compose -y
sudo apt install git -y
```

Ponemos a funcionar docker:
```
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -a -G docker dxninob
sudo reboot
```

Clonamos un repositorio de donde usaremos un archivo de configuración:
```
git clone https://github.com/st0263eafit/st0263-2022-2.git
cd st0263-2022-2/docker-nginx-wordpress-ssl-letsencrypt
sudo cp ssl.conf /home/dxninob/wordpress
cd
```

Entramos a la carpeta creada anteriormete y creamos dos archivos:
```
cd nginx
sudo touch docker-compose.yml
sudo touch nginx.conf
```

Entramos al archivo docker-compose.yml:
```
sudo nano nginx.conf
```

Agregamos el siguiente contenido:
```
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

events {
  worker_connections  1024;  ## Default: 1024
}
http {
  upstream loadbalancer{
    server 10.128.0.27:80 weight=5;
    server 10.128.0.30:80 weight=5;
  }
  server {
    listen 80;
    listen [::]:80;
    server_name _;
    rewrite ^ https://$host$request_uri permanent;
  }
  server {
    listen 443 ssl http2 default_server;
    listen [::]:443 ssl http2 default_server;
    server_name _;
    # enable subfolder method reverse proxy confs
    #include /config/nginx/proxy-confs/*.subfolder.conf;
    # all ssl related config moved to ssl.conf
    include /etc/nginx/ssl.conf;
    client_max_body_size 0;
    location / {
      proxy_pass http://loadbalancer;
      proxy_redirect off;
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Host $host;
      proxy_set_header X-Forwarded-Server $host;
      proxy_set_header X-Forwarded-Proto $scheme;
    }
  }
}
```

Entramos al archivo docker-compose.yml:
```
sudo nano docker-compose.yml
```

Agregamos el siguiente contenido:
```
version: '3.1'
services:
  nginx:
    container_name: nginx
    image: nginx
    volumes:
    - ./nginx.conf:/etc/nginx/nginx.conf:ro
    - ./ssl:/etc/nginx/ssl
    - ./ssl.conf:/etc/nginx/ssl.conf
    ports:
    - 80:80
    - 443:443
```

Detenemos nginx:
```
ps ax | grep nginx
netstat -an | grep 80
sudo systemctl disable nginx
sudo systemctl stop nginx
```

Inciamos Docker:
```
cd /home/dxninob/nginx
docker-compose up --build -d
```

### 2. Servidor de Base de Datos
Instalamos docker y docker-compose:
```
sudo apt install docker.io -y
sudo apt install docker-compose -y
```

Creamos un directorio para el docker container y accedemos a este:
```
mkdir docker
cd docker
```

Creamos dos archivos de configuración:
```
sudo touch Dockerfile
sudo touch docker-compose.yaml
```

Ingresamos al Dockerfile:
```
sudo nano Dockerfile
```

Ingresamos este contenido en el archivo:
```
FROM mysql:8.0
```

Ingresamos al docker-compose.yaml:
```
sudo nano docker-compose.yaml
```

Ingresamos este contenido en el archivo:
```
version: "3.7"
services:
  mysql:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: dbserver
    restart: always
    ports:
      - 3306:3306
    environment:
      MYSQL_ROOT_PASSWORD: "1234"
      MYSQL_DATABASE: "wordpressdb"
    volumes:
      - ./schemas:/var/lib/mysql:rw
volumes:
  schemas: {}
```

Ponemos a funcionar docker:
```
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -a -G docker dxninob
sudo reboot
```

Corremos el contenedor docker y accedemos a MySQL:
```
cd docker
sudo docker-compose up --build -d
sudo docker exec -it dbserver mysql -p
```

Creamos la base de datos:
```
CREATE DATABASE wpdb;
```

Creamos un usuario para la base de datos y le permitimos todos los privilegios:
```
CREATE USER 'dxninob' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON *.* TO 'dxninob'@'%';
exit
```

### 3. Servidor NFS
Instalamos nfs-kernel-server:
```
sudo apt update
sudo apt install nfs-kernel-server
sudo apt install ufw
```

Crear carpeta para compartir archivos en el servidor NFS:
```
sudo mkdir -p /mnt/nfs_share
```

Entramos al archivo /etc/exports:
```
sudo nano /etc/exports
```

Agregamos la siguiente linea al final :
```
/mnt/nfs_share 10.128.0.0/20(rw,sync,no_subtree_check)
```

Exportamos el nuevo NFS:
```
sudo exportfs
```

Actualizamos las reglas de firewall:
```
sudo systemctl restart nfs-kernel-server
sudo ufw allow from 10.128.0.0/20 to any port nfs
sudo ufw enable
sudo ufw status
sudo ufw allow 22
```

### 4. Servidores de Wordpress
El siguiente paso a paso se debe realizar para las dos instancias.  
Instalamos nfs-common, docker y docker-compose:
```
sudo apt update
sudo apt install nfs-common -y
sudo apt install docker.io -y
sudo apt install docker-compose -y
```

Entramos al archivo  /etc/fstab:
```
sudo nano /etc/fstab
```

Agregamos la siguiente línea:
```
10.128.0.32:/mnt/nfs_share /var/www/html nfs auto 0 0
```

Hacemos la conexión al servidor NFS:
```
sudo mount -a
```

- **Nota:** Si creamos un archivo en la carpeta /var/www/html en cualquiera de las dos intancias, se va a ver automaticamente en la otra instancia y en la carpeta /mnt/nfs_share del servidor NFS.

Habilitamos docker:
```
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -a -G docker dxninob
sudo reboot
```

Creamos un directorio para el docker container:
```
mkdir docker
```

Creamos un archivo docker-compose.yaml e ingresamos:
```
sudo touch docker-compose.yaml
sudo nano docker-compose.yaml
```

Ingresamos el siguiente contenido:
```
version: '3.7'
services:
  wordpress:
    container_name: wordpress
    image: wordpress:latest
    restart: always
    environment:
      WORDPRESS_DB_HOST: 10.128.0.20:3306
      WORDPRESS_DB_USER: dxninob
      WORDPRESS_DB_PASSWORD: 1234
      WORDPRESS_DB_NAME: wpdb
    volumes:
      - /var/www/html:/var/www/html
    ports:
      - 80:80
volumes:
  wordpress:
```

Corremos el contenedor:
```
sudo docker-compose up --build -d
```


## Como un usuario lo utilizaría
El usuario solo debe acceder a la URL https://lab4.danielanino.tk desde cualquier browser.


## Resultados
Podemos ver el certificado SSL

Podemos ingresas al Wordpress desde dos direcciones IP diferentes


Si hacemos un cambio en un Wordpress, se hace automaticamente solo en el otro Wordpress


# 5. Información relevante
## Referencias:
- Se usó código de un trabajo realizado el semestre pasado en la clase de Telemática
- https://github.com/st0263eafit/st0263-2022-2/tree/main/docker-nginx-wordpress-ssl-letsencrypt  
- https://www.youtube.com/watch?v=N3xWxZt8x2s
- https://www.serverlab.ca/tutorials/linux/web-servers-linux/how-to-scale-wordpress-sites-using-nfs/
- https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/How-to-setup-an-Nginx-load-balancer-example
