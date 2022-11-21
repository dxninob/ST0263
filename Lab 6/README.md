# Info de la materia:
ST0263 - Tópicos Especiales en Telemática

# Estudiante:
Daniela Ximena Niño Barbosa, dxninob@eafit.edu.co

# Profesor:
Edwin Nelson Montoya Munera, emontoya@eafit.edu.co

# Laboratorio 6

# 1. Breve descripción de la actividad
## 1.1. Aspectos desarrollados de la actividad propuesta
- Ejecutar el wordcount por linea de comando 'pyspark' INTERACTIVO en EMR con datos en HDFS vía ssh en el nodo master.
- Ejecutar el wordcount por linea de comando 'pyspark' INTERACTIVO en EMR con datos en S3 (tanto de entrada como de salida)  vía ssh en el nodo master.
- Ejecutar el wordcount en JupyterHub Notebooks EMR con datos en S3 (tanto datos de entrada como de salida) usando un clúster EMR.
- Replique, ejecute y entienda el notebook Data_processing_using_PySpark.ipynb con los datos respectivos y ejecutelo en AWS EMR.

## 1.2. Aspectos NO desarrollados de la actividad propuesta
Todo lo propuesto fue desarrollado.



# 2. Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.



# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
## Detalles técnicos
- Python:
- Spark:
- AWS:

## Detalles del desarrollo.
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


### **Ejecutar el wordcount por linea de comando 'pyspark' INTERACTIVO en EMR con datos en S3 (tanto de entrada como de salida) vía ssh en el nodo master**
- Creamos un bucket S3 y cargamos los datasets desde nuestros archivos.
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
>>> wc.saveAsTextFile("hdfs://dxninob-lab6/wcout2")
```
- Podemos ver los datos de salida en Hue en la carpeta /tmp/wcout2.

- Podemos ver que los datos de salida en S3.

### **Ejecutar el wordcount en JupyterHub Notebooks EMR con datos en S3 (tanto datos de entrada como de salida) usando un clúster EMR**
- Copiamos el notebook del wordcount y lo ejecutamos.
- Podemos ver los datos de salida en Hue en la carpeta /tmp/wcout3.
- Podemos ver que los datos de salida en S3.

### **Replique, ejecute y entienda el notebook Data_processing_using_PySpark.ipynb con los datos respectivos y ejecutelo en AWS EMR**
- Copiamos el notebook Data_processing_using_PySpark.ipynb.
- Guardamos el dataframe en formato csv.
- Guardamos el dataframe en formato parquet.







# 5. Referencias
- https://github.com/st0263eafit/st0263-2022-2/