# DeepFlood
In this project, a semantic segmentation model is trained to identify flood areas in Cartagena using DeepLabV3. 

# Repo structure
* The main execution file is ***main.py***, where all the training and predictions made by the model are recorded.
* The segmentation_data folder contains the files and data used for training. These are divided into subfolders described below:
  >***Image***: contains the training images
  
  >***Mask***: contains the binary segmentation masks for each of the photos
  
  >***labelme_json***: This contains the JSON files that describe the labels and the position of the vertices of the polygons created for segmentation in LabelMe
  
  >***labelme_to_masks.py***: it is a small script created with the purpose of transforming json into binary masks in png format
  
  >***metadata.csv***: CSV file indicating the relationship between the image and its respective binary mask
  
💡 ***Note:*** Data collection, polygon creation, labeling, and mask binarization were all done from scratch, considering the unique setting of Cartagena, Colombia.

* The file ***DeepLab-FloodArea.png*** is a demonstration of the DeepLabV3 architecture used in the model. It includes step-by-step details.
* The ***requirements.txt*** file contains the main dependencies needed for the code to run.
