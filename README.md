# DeepFlood

**Integrantes:** Jorge Andrés Herrera Monsalve y Aaron Dali Lopez Fortich

En este proyecto, se entrena un modelo de segmentación semántica para identificar áreas de inundación en Cartagena utilizando DeepLabV3.

## Repo structure

* El archivo principal de ejecución es ***main.py***, donde se registran todos los entrenamientos y predicciones hechas por el modelo.
* La carpeta ***segmentation_data*** contiene los archivos y datos usados para el entrenamiento. Estos están divididos en subcarpetas descritas a continuación:
  
  > ***Image***: contiene las imágenes de entrenamiento
  
  > ***Mask***: contiene las máscaras binarias de segmentación para cada una de las fotos
  
  > ***labelme_json***: contiene los archivos JSON que describen las etiquetas y la posición de los vértices de los polígonos creados para la segmentación en LabelMe
  
  > ***labelme_to_masks.py***: pequeño script creado para transformar los JSON en máscaras binarias en formato PNG
  
  > ***metadata.csv***: archivo CSV que indica la relación entre la imagen y su respectiva máscara binaria

💡 **Nota:** La recolección de datos, creación de polígonos, etiquetado y binarización de máscaras fueron realizados desde cero, considerando el entorno particular de Cartagena, Colombia.

* El archivo ***DeepLab-FloodArea.png*** es una demostración de la arquitectura DeepLabV3 usada en el modelo. Incluye detalles paso a paso.
* El archivo ***requirements.txt*** contiene las dependencias principales necesarias para que el código funcione.
