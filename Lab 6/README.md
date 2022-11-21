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
- Guardamos el dataframe en formato csv.
- Guardamos el dataframe en formato parquet.

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
