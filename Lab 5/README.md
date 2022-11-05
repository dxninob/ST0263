## Info de la materia:
ST0263 - Tópicos Especiales en Telemática

## Estudiante:
Daniela Ximena Niño Barbosa, dxninob@eafit.edu.co

## Profesor:
Edwin Nelson Montoya Munera, emontoya@eafit.edu.co

## Punto 1
### Configuración del cluster
Primero debemos ingresar al servicio EMR en AWS, damos click en Crear Cluster e ingresamos a las ocpiones avanzadas.

Configuramos el cluster con los siguientes parametros:

<img width="676" alt="1 config" src="https://user-images.githubusercontent.com/60080916/200108260-361aad20-68e1-4eb5-b532-fdef3e48150b.PNG">
<img width="675" alt="2 config" src="https://user-images.githubusercontent.com/60080916/200108261-0051cc73-6464-42c1-9da6-915d4ecd8517.PNG">
<img width="700" alt="3 config" src="https://user-images.githubusercontent.com/60080916/200108262-f21e9a49-b4f5-491e-854f-dfd59a4bb5cb.PNG">
<img width="583" alt="4 config" src="https://user-images.githubusercontent.com/60080916/200108263-648fd140-efde-4e12-9363-a0cfbbf741af.PNG">

Seleccionamos la clave con la que funcionará el cluster en este paso:

<img width="612" alt="5 config" src="https://user-images.githubusercontent.com/60080916/200108264-07e9cafc-2411-46ee-ba2e-31f3e72c31c4.PNG">

Entramos al servicio S3 de AWS y creamos el bucket que escribimos en la configuración del cluster:

<img width="944" alt="bucket" src="https://user-images.githubusercontent.com/60080916/200108258-947bee74-48fb-4b79-8f6e-80e71737d622.PNG">

Esperamos a que el cluster se cree, esto demora al rededor de 20 minutos, luego de que esté listo podemos continuar con los siguientes pasos.

En el servicio EMR de AWS, le damos click a nuestro cluster y en la pestaña *Resumen*, encontramos el comando para conectarnos al cluster por SSH.

<img width="790" alt="resumen ssh" src="https://user-images.githubusercontent.com/60080916/200110435-c821a98f-0061-4c13-a156-3bf0bfb03cc3.PNG">

<img width="768" alt="master node" src="https://user-images.githubusercontent.com/60080916/200110436-2b2e15d5-4614-438f-b38a-d3a8cad622f1.PNG">


Después de conectarnos al cluster, podemos probar los siguientes comandos:
```
hdfs dfs -ls /
hdfs dfs -ls /user
```

En el servicio ERM de AWS, nos dirigimos a *Bloquear acceso publico*, donde editamos los puertos para que queden así:

<img width="739" alt="sec groups" src="https://user-images.githubusercontent.com/60080916/200110437-84940c3b-b314-40f7-8f24-f2bfe363e3e7.PNG">
<img width="830" alt="1" src="https://user-images.githubusercontent.com/60080916/200110438-4a3206f7-e733-4790-bbdc-dd2a99de612a.PNG">
<img width="828" alt="2" src="https://user-images.githubusercontent.com/60080916/200110440-1ebd0a0f-c1fc-41a4-9b9b-3d0cbdc30295.PNG">
<img width="823" alt="3" src="https://user-images.githubusercontent.com/60080916/200110441-c968ff78-6a9d-425e-86f6-a7e51d59f386.PNG">


Ahora nos podemos dirigir a *Clusteres* y luego a la pestaña de *Summary* donde podemos moificar el security group para el nodo master:

Ahora nos podemos dirigir a *Clusteres* y luego a la pestaña de *Historial de aplicaciones* donde podemos ver las URL para conectarnos a los diferntes softwares.



<img width="960" alt="6 hive" src="https://user-images.githubusercontent.com/60080916/200108265-34454f6f-8b14-4ee8-a63d-0064ea03f8af.PNG">
<img width="960" alt="7 files" src="https://user-images.githubusercontent.com/60080916/200108266-865faed0-891d-4d33-b4e5-94b64ed2a8a3.PNG">
<img width="960" alt="8 s4" src="https://user-images.githubusercontent.com/60080916/200108251-7abeaebe-4063-45a2-a9e7-14616ccec0e0.PNG">
<img width="960" alt="9 jupyter" src="https://user-images.githubusercontent.com/60080916/200108252-8dadd9ff-3bc0-4bcd-bc72-7f8772f1185a.PNG">
<img width="959" alt="10 spark" src="https://user-images.githubusercontent.com/60080916/200108253-c189cf5d-061d-4a9b-8702-0b85e0e0e2a8.PNG">
<img width="947" alt="11 zeppelin spark" src="https://user-images.githubusercontent.com/60080916/200108254-377bf87e-3c60-40f3-bee7-835865abee04.PNG">
<img width="945" alt="12 zepellin sql" src="https://user-images.githubusercontent.com/60080916/200108256-94a4fcd9-1582-4dfe-87c2-c607ca65e537.PNG">
<img width="960" alt="13 hue jupyter" src="https://user-images.githubusercontent.com/60080916/200108257-e5a6a8a8-ae20-41b8-953c-43090d2d4201.PNG">
<img width="939" alt="terminal" src="https://user-images.githubusercontent.com/60080916/200108259-d47262ea-aac9-4f93-beec-f1085b567c38.PNG">


## Punto 2

## Punto 3
Clonamos el repositorio:
```
git clone https://github.com/dxninob/ST0263-TopicosTelematica.git
```

Entramos a la carpeta del lab 5.3:
```
cd "ST0263-TopicosTelematica/Lab 5/Lab 5.3"
```

Instalamos MRJOB:
```
pip install mrjob
```

Usamos el siguiente comando para ejecutar los ejercicios del punto 1, remplazando la X por el ejercicio que se quiere ejecutar:
```
python files/punto1/pX.py datasets/dataempleados.csv
```

Usamos el siguiente comando para ejecutar los ejercicios del punto 2, remplazando la X por el ejercicio que se quiere ejecutar:
```
python files/punto2/pX.py datasets/dataempresas.csv  
```

Usamos el siguiente comando para ejecutar los ejercicios del punto 3, remplazando la X por el ejercicio que se quiere ejecutar:
```
python files/punto3/pX.py datasets/datapeliculas.csv   
```
