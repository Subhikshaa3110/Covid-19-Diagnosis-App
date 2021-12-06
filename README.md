# Covid-19-Diagnosis-App
Dataset and model - https://drive.google.com/drive/folders/1tjESwgrVvVfyw3SVYM-f9iAJTj_pLRBq?usp=sharing <br><br>
Covid-19 Diagnosis using Chest X-ray Images. Machine Learning Project which creates an image classifier using Keras by implementing a Convolution Neural Network(CNN) to differentiate between Chest X-rays images with a COVID-19 infectious person versus Normal Healthy people. The dataset contains the lungs X-ray images of both groups(COVID-19 and Healthy patients).
<li>Imported necessary libraries and Data Exploration
<li>Data visualization, displayed 10 Chest X-ray images of Covid-19 and Normal Healthy People using Matplotlib.
<li>Data Pre-processing and Augmentation, technique which is used to artificially expand the size of a training dataset by creating modified versions of images in the dataset.
<li>Training deep learning neural network models on more data can result in more skillful models, and the augmentation techniques can create variations of the images that can improve the ability of the fit models to generalize what they have learned to new images.
<li>ImageDataGenerator, a Keras Deep Learning library can be used for an image dataset which is located on disk in a specified directory, where images in that directory are organized into subdirectories according to their class.It can also be used to specify the validation dataset and the test dataset.
<li>Building the model, Sequential model is used to build the model layer by layer and many layers can be added to the model using add function
<li>Conv2D layer creates a convolution kernel that winds with layers input which helps produce a tensor of outputs.
<li>Max Pooling to reduce the spatial dimensions of the output volume.
<li>Dropout is used to dropout some percentage of features or the probability at which outputs of the layer are retained. and implemented per layer in neural network
<li>Dense layer receives output from every neuron of its preceding layer i.e, neurons of the layer are connected to every neuron of its preceding layer.
<li>Compiled the model using Adam optimization algorithm, accuracy as evaluation metrics and binary cross entropy as loss measure.
<li>Trained the model using training data and validation data and calculated accuracy and loss at each epoch
<li>Plotted graphs using Matplotlib to visualize the loss between training and validation data, accuracy between training and validation data
<li>Evaluated the model using test dataset and displayed the accuracy and cross entropy loss
<li>Performed prediction on new data and stored the model into model.h5 file
<li>Python web framework Flask is used to display the Covid-19 Diagnosis as an application.
  
Output:<br><br>
  The user should enter the patient details and upload the chest X-ray image<br><br>
  ![op-page1](https://user-images.githubusercontent.com/64024900/144715666-6e1877f7-7bb5-4aad-a5c5-74d597639f05.png)
<br><br>
  Covid-19 Prediction report is displayed along with patient details<br><br>
  ![op-page2](https://user-images.githubusercontent.com/64024900/144715677-42714d09-c7de-4a1a-85ea-84f2e0fe2700.png)
# Contributors
  <li> S Subhikshaa
  <li> Abinaya U
