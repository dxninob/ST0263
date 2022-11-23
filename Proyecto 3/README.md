# Info de la materia:
ST0263 - Tópicos Especiales en Telemática

# Estudiante:
Daniela Ximena Niño Barbosa, dxninob@eafit.edu.co

# Profesor:
Edwin Nelson Montoya Munera, emontoya@eafit.edu.co



# 1. Descripción de la actividad
## 1.1. Aspectos desarrollados de la actividad propuesta
## 1.2. Aspectos NO desarrollados de la actividad propuesta



# 2. Información general



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
<img width="728" alt="Spark obj" src="https://user-images.githubusercontent.com/60080916/203457217-6c4de0b8-3a65-4a50-809b-089b7fc55668.PNG">
  - Nota: para crearlos vamos a necesitar ingresar unos datos de nuestra cuenta de AWS, estos se renuevan cada tres horas por lo que se deben cambiar constantemente.
<img width="728" alt="AWS Details" src="https://user-images.githubusercontent.com/60080916/203457260-541f05be-755a-4b1e-9ab4-9f92c95b178e.PNG">
- Podemos verificar que se crearon los objetos.
<img width="471" alt="obj" src="https://user-images.githubusercontent.com/60080916/203458239-6000fa30-80b9-47ee-af9a-751b1e768ed0.PNG">
- Cargamos los archivos desde AWS usando la URI de nuestro bucket.
<img width="904" alt="Cargar AWS" src="https://user-images.githubusercontent.com/60080916/203459010-2255a44d-6a55-4ee2-aa7f-19518272a72e.PNG">




### **Análisis exploratorio de los datos con dataframes**
- Columnas
- Tipos de datos
- Seleccionar algunas columnas
- Renombrar columnas
- Agregar columnas
- Borrar columnas
- Filtrar datos
- Ejecutar alguna función UDF o lambda sobre alguna columna creando una nueva

```
codigo
```
### **Preguntas adicionales**



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
