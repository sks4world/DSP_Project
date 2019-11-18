#######################################################################################################################################
# DATASCIENCE PROJECT ON MACHINE LEARNING TO CLASSIFY RECEIPTS
#######################################################################################################################################

The project repository contains the following:
1. Data preprocessing code in ipynb format
2. Machine Learning code in ipynb format
3. Project Paper 
4. Project description Video
5. Data files used for machine learning (posted to Box account due to large folder size and link provided in github)

The path in the ipynb file is made generic to execute from another jupyter notebook environment. However, the file_path variable has to be set to the location where the data files are kept

This project scans the receipts and classifies as publix or walmart receipts and Milk or Non-Milk Receipts.

Notebook1: Preprocessing- This file adds gaussian blur and finds the edges and crops the image from its background.Also it adds bounding boxes around he text which makes easy for cnn to identify text. Needs pyimagesearch folder for dependencies. Other dependencies have to be installed using pi(few are specified in notebook)

Notebook2: This file has the cnn model building steps with Keras. We can change the hyperparameters and also data to increase accuracy. Currecnt accuracy after all epoches have run is 62%

Yet to do: Data preprocessing gives the cropped image with bounding boxes. But its not fed to cnn model. We have to find ways to feed images from preprocessing step to model step

Directions to run the code: step1: For datapreprocessing please run the file data_preprocessing.ipynb file: It does following functionaities: Files uploaded into the raw_images will be cropped and saved into the processed files. You can try out by adding receipt files to the raw_images folder(Receipt need to have 4 corners) Runs the photocrop.py to get the core areas of the receipt and saves them to processed folder. This methodology is implemented for cleaning data files and feeding it to next steps in the pipeline(Data Augmentation) Step2: Run the project_model.ipynb file to run different models by augmenting the dataset.(please change the number of files to be generated for generating different amount of data and split the dataset to train and test and mentioned in the comments, default is set to 1 ).

Please replace generate folder with https://usf.app.box.com/s/c15l4pmatcqx82kp3jjap7kvaci8q1yf with name generate retained. The dataset in the box url has images already generated by augmentation.
