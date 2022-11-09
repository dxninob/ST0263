# Info de la materia:
ST0263 - Tópicos Especiales en Telemática

# Estudiante:
Daniela Ximena Niño Barbosa, dxninob@eafit.edu.co

# Profesor:
Edwin Nelson Montoya Munera, emontoya@eafit.edu.co


# 1. Breve descripción de la actividad
Realizar las actividades propuestas en un cluster ERM de AWS y los ejercicios de MapReduce propuestos en Python.

## 1.1. Aspectos desarrollados de la actividad propuesta
- Punto 1: Crear un cluster EMR, activar Hue y hacer uso de Jupyter y Zeppelin.
- Punto 2: En un cluster ERM realizar la separación en los directorios hdfs o en los buckets de S3.
- Punto 3: Realizar los ejercicios propuestos de MapReduce con MRJOB en Python.

## 1.1. Aspectos NO desarrollados de la actividad propuesta
Todo ha sido implementado.

# 2. Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
## Punto 1
En AWS se hizo uso del servicio ERM para la creación del cluster y del servicio S3 para la creación de buckets.
## Punto 1
En AWS se hizo uso del servicio ERM para la creación del cluster y del servicio S3 para la creación de buckets.
## Punto 3
Se usaron clases y objetos para el código de los ejercicos.

# 3. Descripción del ambiente de desarrollo y técnico
## Punto 1
### Detalles técnicos
Para este ejercicio fueron usadas las siguientes herramientas:
- AWS: se usó para la creación del cluster ERM.
- Hue: se usó para la gestión de Hadoo.
- JupyterHub: se usó para la creación de Jupyter Notebooks para el uso de Spark.
- Zeppelin: se usó para la creación de notebooks para el uso de Spark y SQL.

### Descripción y como se configura los parámetros del proyecto
- Primero debemos ingresar al servicio EMR en AWS, damos click en Crear Cluster e ingresamos a las ocpiones avanzadas.

- Configuramos el cluster con los siguientes parametros:
<img width="676" alt="1 config" src="https://user-images.githubusercontent.com/60080916/200108260-361aad20-68e1-4eb5-b532-fdef3e48150b.PNG">
<img width="675" alt="2 config" src="https://user-images.githubusercontent.com/60080916/200108261-0051cc73-6464-42c1-9da6-915d4ecd8517.PNG">
<img width="700" alt="3 config" src="https://user-images.githubusercontent.com/60080916/200108262-f21e9a49-b4f5-491e-854f-dfd59a4bb5cb.PNG">
<img width="583" alt="4 config" src="https://user-images.githubusercontent.com/60080916/200108263-648fd140-efde-4e12-9363-a0cfbbf741af.PNG">

- Seleccionamos la clave con la que funcionará el cluster en este paso:
<img width="612" alt="5 config" src="https://user-images.githubusercontent.com/60080916/200108264-07e9cafc-2411-46ee-ba2e-31f3e72c31c4.PNG">

- Entramos al servicio S3 de AWS y creamos el bucket que escribimos en la configuración del cluster:
<img width="944" alt="bucket" src="https://user-images.githubusercontent.com/60080916/200108258-947bee74-48fb-4b79-8f6e-80e71737d622.PNG">

- Esperamos a que el cluster se cree, esto demora al rededor de 20 minutos, luego de que esté listo podemos continuar con los siguientes pasos.

### Detalles del desarrollo
- En el servicio EMR de AWS, le damos click a nuestro cluster y en la pestaña *Resumen*, encontramos el comando para conectarnos al cluster por SSH.
<img width="790" alt="resumen ssh" src="https://user-images.githubusercontent.com/60080916/200110435-c821a98f-0061-4c13-a156-3bf0bfb03cc3.PNG">

- Después de conectarnos al cluster, podemos probar los siguientes comandos:
```
hdfs dfs -ls /
hdfs dfs -ls /user
```
<img width="939" alt="terminal" src="https://user-images.githubusercontent.com/60080916/200108259-d47262ea-aac9-4f93-beec-f1085b567c38.PNG">

- En el servicio ERM de AWS, nos dirigimos a *Bloquear acceso publico*, donde editamos los puertos para que queden así:
<img width="791" alt="a" src="https://user-images.githubusercontent.com/60080916/200110870-f9a11f74-b9a7-4513-85ac-be5835a349f4.PNG">

- Ahora nos podemos dirigir a *Clusteres* y luego a la pestaña de *Summary* donde podemos modificar el security group para el nodo master:
<img width="768" alt="master node" src="https://user-images.githubusercontent.com/60080916/200110436-2b2e15d5-4614-438f-b38a-d3a8cad622f1.PNG">
<img width="739" alt="sec groups" src="https://user-images.githubusercontent.com/60080916/200110437-84940c3b-b314-40f7-8f24-f2bfe363e3e7.PNG">
<img width="830" alt="1" src="https://user-images.githubusercontent.com/60080916/200110438-4a3206f7-e733-4790-bbdc-dd2a99de612a.PNG">
<img width="828" alt="2" src="https://user-images.githubusercontent.com/60080916/200110440-1ebd0a0f-c1fc-41a4-9b9b-3d0cbdc30295.PNG">
<img width="823" alt="3" src="https://user-images.githubusercontent.com/60080916/200110441-c968ff78-6a9d-425e-86f6-a7e51d59f386.PNG">

- Nos dirigimos a *Clusteres* y luego a la pestaña de *Historial de aplicaciones* donde podemos ver las URL para conectarnos a los diferentes softwares.  Desde ahí nos podemos conectar a Hue, donde podemos ver la siguiente información:
<img width="960" alt="6 hive" src="https://user-images.githubusercontent.com/60080916/200108265-34454f6f-8b14-4ee8-a63d-0064ea03f8af.PNG">
<img width="960" alt="7 files" src="https://user-images.githubusercontent.com/60080916/200108266-865faed0-891d-4d33-b4e5-94b64ed2a8a3.PNG">
<img width="960" alt="8 s4" src="https://user-images.githubusercontent.com/60080916/200108251-7abeaebe-4063-45a2-a9e7-14616ccec0e0.PNG">

- Nos dirigimos nuevamente a *Clusteres* y luego a la pestaña de *Historial de aplicaciones* y con la URL nos conectamos a JupyterHub.
<img width="960" alt="9 jupyter" src="https://user-images.githubusercontent.com/60080916/200108252-8dadd9ff-3bc0-4bcd-bc72-7f8772f1185a.PNG">

- Creamos un notebook para probar Spark:
<img width="959" alt="10 spark" src="https://user-images.githubusercontent.com/60080916/200108253-c189cf5d-061d-4a9b-8702-0b85e0e0e2a8.PNG">

- Nos dirigimos nuevamente a *Clusteres* y luego a la pestaña de *Historial de aplicaciones* y con la URL nos conectamos a Zeppelin.  Creamos un notebook para probar Spark y SQL
<img width="947" alt="11 zeppelin spark" src="https://user-images.githubusercontent.com/60080916/200108254-377bf87e-3c60-40f3-bee7-835865abee04.PNG">
<img width="945" alt="12 zepellin sql" src="https://user-images.githubusercontent.com/60080916/200108256-94a4fcd9-1582-4dfe-87c2-c607ca65e537.PNG">

- Por último, si nos devolvemos a Hue, podemos ver los notebooks que hemos creado, porque estos son persistentes.
<img width="960" alt="13 hue jupyter" src="https://user-images.githubusercontent.com/60080916/200108257-e5a6a8a8-ae20-41b8-953c-43090d2d4201.PNG">






## Punto 2
### Detalles técnicos
Para este ejercicio fueron usadas las siguientes herramientas:
- AWS: se usó para la creación del cluster ERM.
- Hue: se usó para la gestión de Hadoo.

### Detalles del desarrollo
#### Pasar archivos del cluster a Hue
- Entramos al nodo master como fue explicado anteriormente.
- Ejecutamos el siguiente comando:
```
sudo su
```
- Probamos los siguientes comandos para ver el contenido que existe en Hue.
```
hdfs dfs -ls /
hdfs dfs -ls /user
hdfs dfs -ls /user/hadoop
```
- Creamos las siguientes carpetas ye entramos:
```
mkdir /datasets
mkdir /datasets/otros
cd /datasets/otros
```
- Creamos los archivos datapeliculas.txt, dataempresas.txt y dataempleados.txt manualmente.
- Creamos el directorio datasets en Hue.
```
hdfs dfs -mkdir /user/hadoop/datasets
```
- Copiamos los archivos creados anteriormente a Hue.
```
hdfs dfs -put /datasets/otros/*.txt /user/hadoop/datasets
hdfs dfs -copyFromLocal /datasets/otros/*.txt /user/hadoop/datasets
```
- Podemos ver que los archivos que estaban en la instancia ahora están en Hue.
<img width="691" alt="1" src="https://user-images.githubusercontent.com/60080916/200752234-60352c08-e592-4d66-9cab-7dded7e6d5ef.PNG">



#### Pasar archivos de Hue al cluster
- Creamos el directorio mis_datasets:
```
mkdir /mis_datasets
```
- Copiamos los archivos de Hue a la instancia en la carpeta mis_datasets.
```
hdfs dfs -get /user/hadoop/datasets/*.txt /mis_datasets
hdfs dfs -copyToLocal /user/hadoop/datasets/*.txt /mis_datasets
```
- Ahora podemos ver que los archivos de Hue están en la instancia con el siguiente comando:
```
ls -l mis_datasets
```

#### Pasar archivos de Hue a AWS S3
- Entramos a S3 en Hue y creamos un Bucket.
<img width="906" alt="3" src="https://user-images.githubusercontent.com/60080916/200750881-360fc1ad-e336-4c33-a437-701da3d65ce7.PNG">

- Damos click en upload y subimos los archivos datapeliculas.txt, dataempresas.txt y dataempleados.txt, debería quedar así:
<img width="691" alt="4" src="https://user-images.githubusercontent.com/60080916/200750888-46a90562-9c4c-4e2c-9bd4-0a5ea6fda935.PNG">

- Ingresamos a AWS al servicio S3 y debemos ver el bucket con los respectivos archivos.
<img width="762" alt="5" src="https://user-images.githubusercontent.com/60080916/200750892-13addfdd-67a1-4de4-a484-69fcc9e6b60e.PNG">

#### Pasar archivos del cluster a AWS S3
- Creamos un bucket en AWS S3.
<img width="733" alt="7" src="https://user-images.githubusercontent.com/60080916/200752044-cb87601b-2a0b-4924-a2de-6d66498156ca.PNG">

- Ejecutamos los siguientes comandos en la instancia:
```
aws s3 cp /datasets/otros/datapeliculas.txt s3://lab5v2dxninob
aws s3 cp /datasets/otros/dataempresas.txt s3://lab5v2dxninob
aws s3 cp /datasets/otros/dataempleados.txt s3://lab5v2dxninob
```
- Entramos a AWS S3 y podemos ver que los archivos se encuntran allí.
<img width="759" alt="8" src="https://user-images.githubusercontent.com/60080916/200752048-154bf5d3-bd88-4522-9b3a-786d2ff0fc00.PNG">


## Punto 3
### Detalles técnicos
- Python: se usó python como lenguaje de programación para la solución.
- MRJOB: se usó esta librería para el uso de MapReduce en Pyhton.

### Como se compila y ejecuta.
- Clonamos el repositorio
```
git clone https://github.com/dxninob/ST0263-TopicosTelematica.git
```

- Entramos a la carpeta del lab 5.3
```
cd "ST0263-TopicosTelematica/Lab 5/Lab 5.3"
```

- Instalamos MRJOB
```
pip install mrjob
```

- Usamos el siguiente comando para ejecutar los ejercicios del punto 1, remplazando la X por el ejercicio que se quiere ejecutar:
```
python files/punto1/pX.py datasets/dataempleados.csv
```

- Usamos el siguiente comando para ejecutar los ejercicios del punto 2, remplazando la X por el ejercicio que se quiere ejecutar:
```
python files/punto2/pX.py datasets/dataempresas.csv  
```

- Usamos el siguiente comando para ejecutar los ejercicios del punto 3, remplazando la X por el ejercicio que se quiere ejecutar:
```
python files/punto3/pX.py datasets/datapeliculas.csv   
```
