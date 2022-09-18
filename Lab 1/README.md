# Info de la materia: ST0263 - Tópicos Especiales en Telemática
#
# Estudiante: Daniela Ximena Niño Barbosa, dxninob@eafit.edu.co
#
# Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#
# Laboratorio 1
#
# 1. Breve descripción de la actividad

Este proyecto consta de un servidor web minimalista sobre Sockets TCP que implementa unicamente el método GET.  Este servidor procesa peticiones HTTP y localiza el recurso solicitado para enviarlo al cliente, es concurrente y está desplegado en una máquina virtual en AWS.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
1. Implementar un Mini-servidor web minimalista, que implemente únicamente el método GET (versión 0.9 del protocolo HTTP). Debe recibir peticiones HTTP y procesarlas. El procesamiento de la petición debe permitir el localizar el recurso solicitado en el sistema de archivos local al mini-servidor. Dicha aplicación debe funcionar de la siguiente forma:
- El mini-servidor debe ser capaz de escuchar peticiones a nivel de sockets TCP en cualquier puerto. Dado que implementa la funcionalidad de un servidor web, debe preferiblemente ejecutarse el puerto 80.
- El mini-servidor debe ser capaz de procesar el mensaje que llega por el socket, el cual es un mensaje HTTP Request, procesar dicho mensaje, localizar en el recurso y en caso de que, el recurso exista enviar dicho objeto por el sockets a través de un HTTP Response. En caso de que el servidor no posea el recurso, debe enviar el mensaje respectivo al cliente vía HTTP response.
2. El mini-servidor debe ser concurrente, es decir, debe permitir conectarse varios browsers al mismo tiempo.
3. El mini-servidor debe decodificar el protocolo HTTP-Request y HTTP-Response en consola, en un modo de resumen de la información. Si hay una opción o parámetro que no es decodificado por el programa, deberá sacar el mensaje ‘Opción o Valor Desconocido’.
4. El servidor deberá ser desplegado en una máquina virtual en AWS Academy, con IP Elástica, oyendo por el puerto estándar 80.
5. El servidor deberá entregar por defecto archivos del tipo .html o .htm, sin embargo, deberá al menos entregar otros tipos de archivos como .pdf u otros formatos.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
Todos los requisitos fueron implementados.





# 2. Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

Se usó el Single Responsibility Principle y Dont Repeat Yourself.



# 3. Descripción del ambiente de desarrollo y técnico
El servidor fue desarrollado en el lenguaje Python.  Se usaron las siguientes librerías:
- socket: para hacer uso de los Sockets TCP.
- threading: para permitir la concurrencia del servidor.
- os: para saber si existe el recurso del HTTP request en el sistema de archivos local.
- datetime, time, wsgiref.handlers: para devolver el header *Date* en el HTTP response.

## Como se ejecuta
Para ejecutar el código se usa el siguiente comando:  
```python Server.py```

## Detalles del desarrollo

**Métodos del código**

- main: imprime imformación del servidor e invoca el método *server_execution()*.
- server_execution: este método asocia el socket con la dirección IP del servidor y el puerto en el que va a correr, acepta las solicitudes de conexion de un cliente TCP y maneja la función multihilos, esto último es para permitir que varios clientes hagan un HTTP request al mismo tiempo.  Este método invoca la función *handler_client_connection*.
- handler_client_connection: este método recibe como parámetro un objeto socket (el cual usamos para enviar y recibir datos del cliente) y la dirección vinculada al socket en el otro extremo de la conexión.  Posteriormente, recibe el HTTP request del cliente y lo decodifica invocando al método *decode_headers*.  Por último, evalua si el método del request es GET para saber si debe buscar el recurso y enviarlo o mandar una respuesta de método invalido.
- decode_headers: este método recibe como parámetro los headers enviados por el cliente HTTP y los decodifica para mostrar esta información en la consola del servidor.  Únicamente decodifica los headers *User-Agent*, *Keep-Alive*, *Host* y *Date*.
- file_type: este método recibe como parámetro el recurso solicitado por el cliente, evalua su extensión y retorna el identificador MIME de dicho recurso.

## Detalles técnicos

**Posibles respuestas HTTP**

Estos son los posibles códigos de respuesta del servidor:
- HTTP/1.1 200 OK: en caso de que el método del request sea GET y el recurso exista, se envía este código de respuesta, acompañado de los headers *Date*, *Server* y *Content-Type* y el contenido del recurso.
- HTTP/1.1 404 Not Found: en caso de que el método del request sea GET pero el recurso no exista, se envía este código de respuesta, acompañado de los headers *Date* y *Server*. 
- HTTP/1.1 405 Method Not Allowed: en caso de que el método del request sea no sea GET, se envía este código de respuesta, acompañado de los headers *Date* y *Server*.

## Descripción y como se configura los parámetros del proyecto
Los parámetros se configuran en el archivo constants.py.  Estos son los parámetros que se pueden configurar:
- PORT: puerto en el que corre el servidor.  En este caso lo declaramos como 80.
- ENCONDING_FORMAT: formato de codificación y decodificación del servidor.  En este caso lo declaramos como "utf-8".
- RECV_BUFFER_SIZE: establece el número de bytes que almacenacenamos en cada operación de lectura del recurso que se va a enviar al cliente.  En este caso lo declaramos como 2048.
- IP_SERVER: establece las direcciones IP que pueden comunicarse con el servidor.  En este caso lo declaramos como "localhost".
- DOCUMENT_ROOT: carpeta en la que se encuentran los recusos que se pueden mostrar al cliente.  En este caso lo declaramos como 'recusos/'.
- ELASTIC_IP: dirección elastica donde se encuentra el servidor.  En este caso la declaramos '174.129.206.167'.

## Opcional - detalles de la organización del código por carpetas o descripción de algún archivo.
Cuando se hace un request al servidor, este busca el archivo de la petición en la carpeta */recursos*.  Esto se hace con el propósito de que un cliente no pueda acceder al código del servidor.  Por lo tanto si se hace una petición del recurso */carpeta/test.htm*, el servidor internamente va a buscar */recursos/carpeta/test.htm*.

De esta manera están organizados los recursos:

.  
├── constants.py  
├── nohup.out  
├── recursos  
│   ├── carpeta  
│   │   └── test.htm  
│   ├── index.html  
│   ├── test.html  
│   ├── test.jpg  
│   ├── test.json  
│   ├── test.pdf  
│   ├── test.png  
│   ├── test.txt  
└── Server.py  

Entonces para hacerle un request al servidor, desde un browser se puede escribir las siguientes direcciones para acceder a los recursos:

- http://localhost/ (por defecto abre el archivo index.html)
- http://localhost/carpeta/test.htm
- http://localhost/test.html
- http://localhost7/test.jpg
- http://localhost/test.json
- http://localhost/test.pdf
- http://localhost/test.png
- http://localhost/test.txt

O desde una aplicación como Postman, se puede seleccionar el método GET y escribir localhost seguido del recurso, así:

<img width="639" alt="a" src="https://user-images.githubusercontent.com/60080916/184507164-cf421053-2eb0-4785-af44-13bdff81ba45.PNG">

## 
## Opcionalmente - si quiere mostrar resultados o pantallazos 
Como se ve desde el servidor:  
<img width="530" alt="compserver" src="https://user-images.githubusercontent.com/60080916/184506983-5325c983-a95d-47f9-a875-d2da382ae982.PNG">

Como se ve desde el cliente (headers):  
<img width="640" alt="compclient1" src="https://user-images.githubusercontent.com/60080916/184506984-e18f43f8-fc96-40b0-a809-6e6e619e3ba0.PNG">

Como se ve desde el cliente (body):  
<img width="641" alt="compclient2" src="https://user-images.githubusercontent.com/60080916/184506985-6b60ee48-e512-4256-aba6-2aff9b988745.PNG">




# 4. Descripción del ambiente de EJECUCIÓN (en producción)
El servidor fue desarrollado en el lenguaje Python.  Se usaron las siguientes librerías:
- socket: para hacer uso de los Sockets TCP.
- threading: para permitir la concurrencia del servidor.
- os: para saber si existe el recurso del HTTP request en el sistema de archivos local.
- datetime, time, wsgiref.handlers: para devolver el header *Date* en el HTTP response.

# IP o nombres de dominio en nube o en la máquina servidor.
174.129.206.167

## Descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
Los parámetros se configuran en el archivo constants.py.  Estos son los parámetros que se pueden configurar:
- PORT: puerto en el que corre el servidor.  En este caso lo declaramos como 80.
- ENCONDING_FORMAT: formato de codificación y decodificación del servidor.  En este caso lo declaramos como "utf-8".
- RECV_BUFFER_SIZE: establece el número de bytes que almacenacenamos en cada operación de lectura del recurso que se va a enviar al cliente.  En este caso lo declaramos como 2048.
- IP_SERVER: establece las direcciones IP que pueden comunicarse con el servidor.  En este caso lo declaramos como "0.0.0.0".
- DOCUMENT_ROOT: carpeta en la que se encuentran los recusos que se pueden mostrar al cliente.  En este caso lo declaramos como 'recusos/'.
- ELASTIC_IP: dirección elastica donde se encuentra el servidor.  En este caso la declaramos '174.129.206.167'.

## Como se lanza el servidor.
El código del servidor está en un archivo llamado *Server.py*.  Lo ejecutamos con el siguiente comando en la máquina virtual de AWS:  
```sudo python3 Server.py```

O si queremos que se quede ejecutando aunque nos salgamos de la terminal, usamos los siguientes comandos:  
```sudo nohup python3 Server.py```  
```bg```  

Si el puerto 80 está ocupado, tenemos que usar estos comandos para matar el proceso que esté corriendo en este puerto:  
```sudo lsof -i -P -n```  
Buscamos el pid del proceso y corremos este comando:  
``` sudo kill -9 [PID DEL PROCESO]``` 

## Una mini guia de como un usuario utilizaría el software o la aplicación
Para hacerle un request al servidor, desde un browser se puede escribir la dirección IP del servidor seguida del recurso.  Estas son las direcciones de los recursos a los que se puede acceder:
- http://174.129.206.167/ (por defecto abre el archivo index.html)
- http://174.129.206.167/carpeta/test.htm
- http://174.129.206.167/test.html
- http://174.129.206.167/test.jpg
- http://174.129.206.167/test.json
- http://174.129.206.167/test.pdf
- http://174.129.206.167/test.png
- http://174.129.206.167/test.txt

O desde una aplicación como Postman, se puede seleccionar el método GET y escribir la dirección IP del servidor seguido del recurso, así:

<img width="639" alt="Req" src="https://user-images.githubusercontent.com/60080916/184506837-8a944aee-c27d-4eff-851c-3e86a4edadf6.PNG">

## Opcionalmente - si quiere mostrar resultados o pantallazos 
Como se ve desde el servidor:  
<img width="391" alt="Server" src="https://user-images.githubusercontent.com/60080916/183756800-34c29cd5-b9c2-48ac-a211-ea8a589c1b96.PNG">

Como se ve desde el cliente (headers):  
<img width="555" alt="Cliente 2" src="https://user-images.githubusercontent.com/60080916/183757290-ef174ac4-d0c2-43b9-b94a-d356420100c2.PNG">  

Como se ve desde el cliente (body):  
<img width="553" alt="Cliente 1" src="https://user-images.githubusercontent.com/60080916/183757286-88766e3f-c3dd-4b8d-a14c-c529df326566.PNG">

# 5. otra información que considere relevante para esta actividad.
# Referencias:
## Para este proyecto se usó como plantilla un código de la clase de Telemática dictada por el profesor Juan Carlos Montoya en la Universidad EAFIT (no tiene URL porque se subió a Interactiva).

#### versión README.md -> 1.0 (2022-agosto)
