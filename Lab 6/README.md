# Info de la materia:
ST0263 - Tópicos Especiales en Telemática

# Estudiante:
Daniela Ximena Niño Barbosa, dxninob@eafit.edu.co

# Profesor:
Edwin Nelson Montoya Munera, emontoya@eafit.edu.co



# 1. Descripción de la actividad
## 1.1. Aspectos desarrollados de la actividad propuesta
- Ejecutar el wordcount por linea de comando 'pyspark' INTERACTIVO en EMR con datos en HDFS vía ssh en el nodo master.
- Ejecutar el wordcount por linea de comando 'pyspark' INTERACTIVO en EMR con datos en S3 (tanto de entrada como de salida)  vía ssh en el nodo master.
- Ejecutar el wordcount en JupyterHub Notebooks EMR con datos en S3 (tanto datos de entrada como de salida) usando un clúster EMR.
- Replique, ejecute y entienda el notebook Data_processing_using_PySpark.ipynb con los datos respectivos y ejecutelo en AWS EMR.
- Gestionar datos via SQL con HIVE y SparkSQL.
## 1.2. Aspectos NO desarrollados de la actividad propuesta
Todo lo propuesto fue desarrollado.



# 2. Información general
Se usaron los siguientes servicios de AWS:
- EMR: Amazon EMR es una plataforma de clúster administrada que simplifica la ejecución de los marcos de trabajo de Big Data, tales comoApache HadoopyApache Spark, enAWSpara procesar y analizar grandes cantidades de datos.
- S3: Amazon Amazon S3 es un servicio de almacenamiento de objetos que ofrece escalabilidad, disponibilidad de datos, seguridad y rendimiento líderes en el sector. 



# 3. Descripción del ambiente de desarrollo y técnico
## Detalles del desarrollo
- Nos conectamos al nodo master del EMR.
### **Ejecutar el wordcount por linea de comando 'pyspark' INTERACTIVO en EMR con datos en HDFS vía ssh en el nodo master**
- Cargamos los datasets en el nodo.
```
git clone https://github.com/st0263eafit/st0263-2022-2.git
```
- Creamos la carpeta /user/hadoop/datasets en Hue con hdfs.
```
hdfs dfs -mkdir /user/hadoop/datasets
```
- Copiamos los datasets a Hue con hdfs.
```
hdfs dfs -copyFromLocal st0263-2022-2/bigdata/datasets/* /user/hadoop/datasets
```
- Ejecutamos el wordcount con los siguientes comandos.
```
pyspark
>>> files_rdd = sc.textFile("hdfs:///user/hadoop/datasets/gutenberg-small/*.txt")
>>> wc_unsort = files_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
>>> wc = wc_unsort.sortBy(lambda a: -a[1])
>>> for tupla in wc.take(10):
...  print(tupla)
...
```
- Guardamos los datos de salida en Hue con hdfs.
```
>>> wc.saveAsTextFile("hdfs:///tmp/wcout1")
```
- Podemos ver los datos de salida en Hue en la carpeta /tmp/wcout1.
![WhatsApp Image 2022-11-20 at 9 48 38 PM](https://user-images.githubusercontent.com/60080916/202973583-f8f5c405-23f2-4d34-a5e4-9c05fc43b481.jpeg)


### **Ejecutar el wordcount por linea de comando 'pyspark' INTERACTIVO en EMR con datos en S3 (tanto de entrada como de salida) vía ssh en el nodo master**
- Creamos un bucket S3 y cargamos los datasets desde nuestros archivos.
![WhatsApp Image 2022-11-20 at 9 48 56 PM](https://user-images.githubusercontent.com/60080916/202973730-0e4ae175-f0fa-4973-8d37-2b7a0fe29a6f.jpeg)

- Ejecutamos el wordcount con los siguientes comandos.
```
>>> files_rdd = sc.textFile("s3://dxninob-lab6/datasets/gutenberg-small/*.txt")
>>> wc_unsort = files_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
>>> wc = wc_unsort.sortBy(lambda a: -a[1])
>>> for tupla in wc.take(10):
...  print(tupla)
...
```
- Guardamos los datos de salida en Hue con hdfs.
```
>>> wc.saveAsTextFile("hdfs:///tmp/wcout2")
```
- Guardamos los datos de salida en S3.
```
>>> wc.saveAsTextFile("s3://dxninob-lab6/wcout2")
```
- Podemos ver los datos de salida en Hue en la carpeta /tmp/wcout2.
![WhatsApp Image 2022-11-20 at 9 59 47 PM](https://user-images.githubusercontent.com/60080916/202973744-98647a14-3f14-45ae-be74-2e5c9900aa9c.jpeg)

- Podemos ver que los datos de salida en S3.
![WhatsApp Image 2022-11-20 at 10 04 50 PM](https://user-images.githubusercontent.com/60080916/202973948-1cd75d05-6e34-4e88-befd-2c6216d08947.jpeg)

### **Ejecutar el wordcount en JupyterHub Notebooks EMR con datos en S3 (tanto datos de entrada como de salida) usando un clúster EMR**
- Copiamos el notebook del wordcount y lo ejecutamos.
![WhatsApp Image 2022-11-20 at 10 11 24 PM](https://user-images.githubusercontent.com/60080916/202974112-741803dc-1fa2-4618-b274-e652abdc1124.jpeg)

- Podemos ver los datos de salida en Hue en la carpeta /tmp/wcout3.
![WhatsApp Image 2022-11-20 at 10 19 44 PM](https://user-images.githubusercontent.com/60080916/202974095-b9486be8-3941-40f6-911c-65ff4612b8f4.jpeg)

- Podemos ver que los datos de salida en S3.
![WhatsApp Image 2022-11-20 at 10 20 46 PM](https://user-images.githubusercontent.com/60080916/202974050-a40df9b0-0694-491b-8c66-2e0578a5b935.jpeg)



### **Replique, ejecute y entienda el notebook Data_processing_using_PySpark.ipynb con los datos respectivos y ejecutelo en AWS EMR**
- Copiamos el notebook Data_processing_using_PySpark.ipynb.
- Ejecutamos las celdas del notebook.
<img width="736" alt="1" src="https://user-images.githubusercontent.com/60080916/203146107-c1b947b4-c758-4b24-9a45-3cadd3f0cee9.PNG">
<img width="725" alt="2" src="https://user-images.githubusercontent.com/60080916/203146108-3f7bed3e-0c95-4f7e-96dd-616eec58c4f4.PNG">
<img width="792" alt="3" src="https://user-images.githubusercontent.com/60080916/203146110-7ddcd504-7bbb-4274-8299-bcb33f84dc33.PNG">
<img width="796" alt="4" src="https://user-images.githubusercontent.com/60080916/203146111-05b70e48-af53-4a3c-b7af-644dd6ff2d3f.PNG">
<img width="788" alt="5" src="https://user-images.githubusercontent.com/60080916/203146082-befafef0-5d60-41cf-92bd-dc621219d1b0.PNG">
<img width="874" alt="6" src="https://user-images.githubusercontent.com/60080916/203146088-7fa8a6ef-1d80-45bb-a736-8421876d5324.PNG">
<img width="881" alt="7" src="https://user-images.githubusercontent.com/60080916/203146089-d237bf5b-53c7-4662-86be-09034a473d27.PNG">
<img width="802" alt="8" src="https://user-images.githubusercontent.com/60080916/203146093-9e51bf55-6a26-4619-ae01-7c76f0215ad2.PNG">
<img width="877" alt="9" src="https://user-images.githubusercontent.com/60080916/203146095-a5c14d41-fe06-46fa-93d9-3aec87920f20.PNG">
<img width="807" alt="10" src="https://user-images.githubusercontent.com/60080916/203146098-4334be25-6459-401f-8142-74b609a66d29.PNG">
<img width="879" alt="11" src="https://user-images.githubusercontent.com/60080916/203146102-2f44ff36-1937-41e7-8a6d-558198729445.PNG">
<img width="876" alt="12" src="https://user-images.githubusercontent.com/60080916/203146103-95c8b074-e1f8-4bdc-acd5-f68caf3d15a3.PNG">
<img width="796" alt="13" src="https://user-images.githubusercontent.com/60080916/203146105-ffb5d775-27a1-4ccb-a434-84b4f4256a7c.PNG">



- Guardamos el dataframe en formato csv.
<img width="883" alt="csv" src="https://user-images.githubusercontent.com/60080916/203144045-d162296a-04e7-4499-bbcf-aea25c2c7ae4.PNG">

- Guardamos el dataframe en formato parquet.
<img width="883" alt="parquet" src="https://user-images.githubusercontent.com/60080916/203144042-fe7dc657-d088-4784-b39d-7103c56bb6d7.PNG">

- Podemos ver que el dataframe quedó guardado en S3 en ambos formatos.
![WhatsApp Image 2022-11-20 at 11 33 46 PM](https://user-images.githubusercontent.com/60080916/203143615-314ba10c-79e7-4037-8ee4-5bcc3c166e6e.jpeg)


### **Gestionar datos via SQL con HIVE y SparkSQL**
- Nos conectamos a Hue y en el editor seleccionamos Hive.
- Creamos la tabla HDI con los siguientes comandos.
```
CREATE EXTERNAL TABLE HDI (id INT, country STRING, hdi FLOAT, lifeex INT, mysch INT, eysch INT, gni INT) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
STORED AS TEXTFILE 
LOCATION 's3://dxninob-lab6/datasets/onu/hdi/';
```
- Consultamos en la tabla HDI los gni mayores a 2000.
```
show tables;
describe hdi;
select * from hdi;
select country, gni from hdi where gni > 2000;
```
![WhatsApp Image 2022-11-21 at 12 17 26 AM](https://user-images.githubusercontent.com/60080916/202976343-4dfacf48-d3dc-47af-ad15-6e884162f64b.jpeg)

- Creamos la tabla EXPO con los siguientes comandos.
```
CREATE EXTERNAL TABLE EXPO (country STRING, expct FLOAT) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
STORED AS TEXTFILE 
LOCATION 's3://dxninob-lab6/datasets/onu/export/';
```
- Ejecutamos el join de las dos tablas.
```
SELECT h.country, gni, expct FROM HDI h JOIN EXPO e ON (h.country = e.country) WHERE gni > 2000;
```
![WhatsApp Image 2022-11-21 at 12 21 55 AM](https://user-images.githubusercontent.com/60080916/202976434-4535bf9f-0004-4f7d-bb56-c34f6ae87986.jpeg)

- Creamos una tabla para realizar el wordcount con los siguientes comandos.
```
CREATE EXTERNAL TABLE docs (line STRING) 
STORED AS TEXTFILE 
LOCATION 's3://dxninob-lab6/datasets/gutenberg-small/';
```
- Hacemos el wordcount ordenado por palabra.
```
SELECT word, count(1) AS count FROM (SELECT explode(split(line,' ')) AS word FROM docs) w 
GROUP BY word 
ORDER BY word DESC LIMIT 10;
```
![WhatsApp Image 2022-11-21 at 12 24 12 AM](https://user-images.githubusercontent.com/60080916/202976499-239208e0-7a83-42bd-b752-cedbc60a72bf.jpeg)

- Hacemos el wordcount ordenado por frecuencia de menor a mayor.
```SELECT word, count(1) AS count FROM (SELECT explode(split(line,' ')) AS word FROM docs) w 
GROUP BY word 
ORDER BY count DESC LIMIT 10;
```
![WhatsApp Image 2022-11-21 at 12 24 54 AM](https://user-images.githubusercontent.com/60080916/202976708-1f258e76-e88b-4c2a-b7bf-7cfe8d7c8483.jpeg)



# 4. Referencias
- https://github.com/st0263eafit/st0263-2022-2/
