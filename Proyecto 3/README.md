# Info de la materia:
ST0263 - Tópicos Especiales en Telemática

# Estudiante:
Daniela Ximena Niño Barbosa, dxninob@eafit.edu.co

# Profesor:
Edwin Nelson Montoya Munera, emontoya@eafit.edu.co



# 1. Descripción de la actividad
## 1.1. Aspectos desarrollados de la actividad propuesta
- Almacenar los datos en Google Drive
- Almacenar los datos en AWS S3
- Cargar los datos desde Google Drive
- Cargar los datos desde AWS S3
- Análisis exploratorio de los datos con dataframes
- Preguntas adicionales
- Guardar los datos en un bucket público

## 1.2. Aspectos NO desarrollados de la actividad propuesta
Todos fue desarrollado.



# 2. Información general
- AWS: se usó Amazon Web Services como plataforma de computación en la nube.
- S3: se usó el servicio S3 de AWS para la creación de buckets.
- Google Drive: se usó Google Drive para el almacenamiento de archivos.
- Google Colab: se usó Google Colab para la ejecución de código de Python.
- Spark y PySpark: se usaron Spark y PySpark para el uso de dataframes.
- SQL: se usó SQL para hacer consultas de datos.



# 3. Descripción del ambiente de desarrollo y técnico
## Detalles del desarrollo
### **Almacenar los datos en Google Drive**
- Descargamos el repositorio de la materia en ZIP.
<img width="626" alt="zip" src="https://user-images.githubusercontent.com/60080916/203452229-28adcdd6-0b60-448f-bae5-78acdd2d84dd.PNG">

- Extraemos la carpeta y le cambiamos el nombre a st0263-2266.

- Subimos la carpeta a Google Drive.
<img width="723" alt="Drive" src="https://user-images.githubusercontent.com/60080916/203452485-3d7873ea-e289-46df-86ea-002de9ffa1a8.PNG">



### **Almacenar los datos en AWS S3**
- Abrimos el servicio S3 de AWS.

- Damos click en Crear bucket.
<img width="720" alt="Bucket 1" src="https://user-images.githubusercontent.com/60080916/203452523-fbb4075c-8289-40c8-98a9-8bdf5c7785d4.PNG">

- Nombramos el bucket y le damos click en Crear bucket.
<img width="512" alt="Bucket 2" src="https://user-images.githubusercontent.com/60080916/203452525-2ed8fdf5-eb21-4d31-9f16-21ce7262a8bf.PNG">

- Entramos al bucket y damos click en Cargar.
<img width="738" alt="Bucket 3" src="https://user-images.githubusercontent.com/60080916/203452524-09eedca9-416d-47c7-8afe-04b0fadb1f32.PNG">

- Entramos al bucket y podemos ver la carpeta de datasets cargada.
<img width="740" alt="Bucket 4" src="https://user-images.githubusercontent.com/60080916/203455209-443e0397-fe63-4af7-8e83-b0831c799d71.PNG">



### **Cargar los datos desde Google Drive**
- Ejecutamos las celdas de configuración de Spark y PySpark en Google Colab.
<img width="914" alt="conf" src="https://user-images.githubusercontent.com/60080916/203457250-a92d82bb-1284-403c-a836-05c75545fd9a.PNG">

- Creamos los objetos spark y sc.
<img width="890" alt="obj gc" src="https://user-images.githubusercontent.com/60080916/203459138-915580d8-a575-48d9-99bb-d46ac6809b21.PNG">

- Podemos verificar que se crearon los objetos.
<img width="421" alt="obj 2" src="https://user-images.githubusercontent.com/60080916/203459458-9123d3f0-e190-4cc0-a53a-f867055a3245.PNG">

- Damos permisos a Google Colab para que se conecte a Google Drive.
<img width="878" alt="cargar gc" src="https://user-images.githubusercontent.com/60080916/203459316-379e12f7-873f-42b8-a168-731be20763a8.PNG">

- Cargamos los datos desde Google Drive.
<img width="855" alt="permisos" src="https://user-images.githubusercontent.com/60080916/203459318-a6011683-231c-4a52-8802-171e9911a215.PNG">



### **Cargar los datos desde AWS S3**
- Ejecutamos las celdas de configuración de Spark y PySpark en Google Colab.
<img width="914" alt="conf" src="https://user-images.githubusercontent.com/60080916/203457250-a92d82bb-1284-403c-a836-05c75545fd9a.PNG">

- Creamos los objetos spark y sc.
   -  Nota: para crearlos vamos a necesitar ingresar unos datos de nuestra cuenta de AWS, estos se renuevan cada tres horas por lo que se deben cambiar constantemente.
<img width="728" alt="Spark obj" src="https://user-images.githubusercontent.com/60080916/203457217-6c4de0b8-3a65-4a50-809b-089b7fc55668.PNG">
<img width="728" alt="AWS Details" src="https://user-images.githubusercontent.com/60080916/203457260-541f05be-755a-4b1e-9ab4-9f92c95b178e.PNG">

- Podemos verificar que se crearon los objetos.
<img width="471" alt="obj" src="https://user-images.githubusercontent.com/60080916/203458239-6000fa30-80b9-47ee-af9a-751b1e768ed0.PNG">

- Cargamos los archivos desde AWS usando la URI de nuestro bucket.
<img width="904" alt="Cargar AWS" src="https://user-images.githubusercontent.com/60080916/203459010-2255a44d-6a55-4ee2-aa7f-19518272a72e.PNG">



### **Análisis exploratorio de los datos con dataframes**
- Columnas
<img width="260" alt="2 1" src="https://user-images.githubusercontent.com/60080916/203463666-132c9a78-3bdf-4912-a2ab-29d69baff96a.PNG">

- Tipos de datos
<img width="267" alt="2 2" src="https://user-images.githubusercontent.com/60080916/203463669-1191c795-5175-4609-b459-7fbea6294df9.PNG">

- Seleccionar algunas columnas
<img width="478" alt="2 3" src="https://user-images.githubusercontent.com/60080916/203463671-f72b3b5a-5690-41d6-9194-c4b14bb45045.PNG">
<img width="479" alt="2 3 2" src="https://user-images.githubusercontent.com/60080916/203463673-bc4ecd69-af76-4788-9c94-7ca72c89f24f.PNG">

- Renombrar columnas
<img width="735" alt="2 4" src="https://user-images.githubusercontent.com/60080916/203463674-99f24ee1-bb96-4e97-80a3-ebed7cc6cb4f.PNG">

- Agregar columnas
<img width="922" alt="2 5 1" src="https://user-images.githubusercontent.com/60080916/203463675-28923520-4b47-425a-bfc9-13ef75fd5384.PNG">
<img width="432" alt="2 5 2" src="https://user-images.githubusercontent.com/60080916/203463676-7aa620a6-a2f2-46f2-a531-5506eac382db.PNG">
<img width="920" alt="2 5 3" src="https://user-images.githubusercontent.com/60080916/203463678-fa213136-9335-4d9a-b5a6-85899629d6d9.PNG">

- Borrar columnas
<img width="637" alt="2 6" src="https://user-images.githubusercontent.com/60080916/203463679-a77900ab-9b77-4424-a4f6-1ce71e4db6b1.PNG">

- Filtrar datos
<img width="920" alt="2 7 1" src="https://user-images.githubusercontent.com/60080916/203463681-78401f68-fc8d-4a51-a8ed-36f5c81def4e.PNG">
<img width="878" alt="2 7 2" src="https://user-images.githubusercontent.com/60080916/203463683-ad8f4637-0e9b-4956-8a2f-58aaeec3855b.PNG">

- Ejecutar alguna función UDF o lambda sobre alguna columna creando una nueva
<img width="919" alt="2 8 1" src="https://user-images.githubusercontent.com/60080916/203463658-1ad46f10-2c53-4c01-8be1-ad1080d95a8e.PNG">
<img width="920" alt="2 8 2" src="https://user-images.githubusercontent.com/60080916/203463661-ccef16b2-7dcc-4536-8393-dc22400e59eb.PNG">
<img width="919" alt="2 8 3" src="https://user-images.githubusercontent.com/60080916/203463663-c1b63361-3515-46cb-84fe-a4919b8a2ae2.PNG">
<img width="925" alt="2 8 4" src="https://user-images.githubusercontent.com/60080916/203463665-bc201cf4-8fdd-4ef8-aadd-8588e410fce7.PNG">



### **Preguntas adicionales**
- Los 10 departamentos con más casos de covid en Colombia ordenados de mayor a menor.
<img width="543" alt="3 1 1" src="https://user-images.githubusercontent.com/60080916/203469069-06a1ff97-7b29-40c3-8cde-cba886b52595.PNG">
<img width="543" alt="3 1 2" src="https://user-images.githubusercontent.com/60080916/203469070-0f900a5d-7bd0-4f0c-821c-cfcb930f86cf.PNG">

- Las 10 ciudades con más casos de covid en Colombia ordenados de mayor a menor.
<img width="533" alt="3 2 1" src="https://user-images.githubusercontent.com/60080916/203469071-a96cb46d-21fd-436e-b6b0-c80e4e4e4dd0.PNG">
<img width="535" alt="3 2 2" src="https://user-images.githubusercontent.com/60080916/203469057-6664810e-7658-4c27-b991-4fe911904d6d.PNG">

- Los 10 días con más casos de covid en Colombia ordenados de mayor a menor.
<img width="535" alt="4 3 1" src="https://user-images.githubusercontent.com/60080916/203469059-b50feede-a8b2-4982-8ada-bbe6e68cf64b.PNG">
<img width="534" alt="3 3 2" src="https://user-images.githubusercontent.com/60080916/203469060-1d4d10ed-f0ee-4e60-8645-d6be437645a2.PNG">

- Distribución de casos por edades de covid en Colombia.
<img width="543" alt="3 4 1" src="https://user-images.githubusercontent.com/60080916/203469061-482280ed-33b7-487e-93c4-bd6ea94816f4.PNG">
<img width="537" alt="3 4 2" src="https://user-images.githubusercontent.com/60080916/203469062-b8da6d35-112e-4a23-bc05-ca5ed902398c.PNG">

- Realice la pregunda de negocio que quiera sobre los datos y respondala con la correspondiente programación en spark.
<img width="530" alt="p1" src="https://user-images.githubusercontent.com/60080916/203469507-e71db47f-ee8d-43eb-a6d5-7c2b62a598be.PNG">
<img width="705" alt="3 5 1" src="https://user-images.githubusercontent.com/60080916/203469065-ab2029c8-a670-4b24-aa8f-5966d249422c.PNG">
<img width="641" alt="P2" src="https://user-images.githubusercontent.com/60080916/203469505-c29afb58-0977-4507-bd53-43e5ff122e70.PNG">
<img width="539" alt="3 5 2" src="https://user-images.githubusercontent.com/60080916/203469066-13e6514c-6e69-46a0-ae7a-cfcd7c7dd445.PNG">
<img width="535" alt="3 5 3" src="https://user-images.githubusercontent.com/60080916/203469068-3b5d39b8-4e1a-44fd-be02-170ee6768396.PNG">



### **Guardar los datos en un bucket público**
Para especificar donde guardar los archivos, tenemos que hacer uso de la URI de nuestro bucket de S3, el cual debe estar ubicado en la carpeta donde vamos a guardar los archivos.

- Guardamos el dataframe del punto 3.1.
<img width="501" alt="31" src="https://user-images.githubusercontent.com/60080916/203455889-97839730-c312-4703-98fc-c4b07661d3d5.PNG">

- Guardamos el dataframe del punto 3.2.
<img width="501" alt="32" src="https://user-images.githubusercontent.com/60080916/203455882-f1287d64-de92-423d-be61-5442b1e4cfe3.PNG">

- Guardamos el dataframe del punto 3.3.
<img width="502" alt="33" src="https://user-images.githubusercontent.com/60080916/203455884-cd3d0cc1-71b6-43ed-9bcc-5093835dcab3.PNG">

- Guardamos el dataframe del punto 3.4.
<img width="501" alt="34" src="https://user-images.githubusercontent.com/60080916/203455886-c7240928-eba8-420d-ac88-52ce358e5be2.PNG">

- Guardamos los dataframes del punto 3.5.
<img width="500" alt="35" src="https://user-images.githubusercontent.com/60080916/203455887-912f66f5-f47d-480f-a2fa-1b722845520a.PNG">

- Entramos al bucket y podemos ver los archivos guardados.
<img width="745" alt="Bucket resultados" src="https://user-images.githubusercontent.com/60080916/203452894-12fa8055-6657-4ae9-aa73-16f6e64c4635.PNG">



# 4. Referencias
- https://github.com/st0263eafit/st0263-2022-2/
