# ml_zoomcamp_midterm_student_dropout

## ML project for ML Zoomcamp 2023 midterm project

In this project I have build a RandomForest Classifier model for students dropout prediction

This project is based on the Dropout Analysis for School Education dataset:

[Dataset info](https://www.kaggle.com/code/jeevabharathis/student-dropout-analysis-for-school-education)

[Details here](https://www.mdpi.com/2306-5729/7/11/146)

*Main purpose is to predict the chance of student dropout*

Project is deployed to the GCP.
In the deployed project there is a HTML with form, where you can manually enter feature values and get a prediction.

### [Students dropout prediction](https://dropout-predict-2avfrxfgrq-uc.a.run.app/)
(it make take some little time to wake up first time)

Also, prediction via API is possible


## Project files to see:

**dataset/dataset.csv** - dataset

**notebook.ipynb** - Jupiter notebook of preparation, exploration of the data, training different models, and comparing them

**train.py** - script for training the model, using selected approach and hyperparameters found in the notebook, and
exporting the model to file

**model/model.bin** - model and DictVectoriser stored by pickle

**predict.py** - script for running flask server, with API JSON prediction, and prediction throug HTML interface

**Dockerfile** - a docker file for building the image.

For building image and deployment I have used:

**docker build -t dropout_predict .**

then I log in to GPC from local terminal, created a GCP image repository, enabled GCP specific API for working with
images, added a tag to my image, pushed it there, and run this container via Cloud Run service.


**predict_test.py** - prediction test using API JSON
(API using JSON can be reached with [prediction API](https://dropout-predict-2avfrxfgrq-uc.a.run.app/predict))



