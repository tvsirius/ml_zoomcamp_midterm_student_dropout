# ml_zoomcamp_midterm_student_dropout
ML project for students dropout prediction

This project is based on the Dropout Analysis for School Education dataset
[Dataset info](https://www.kaggle.com/code/jeevabharathis/student-dropout-analysis-for-school-education)
[Details here](https://www.mdpi.com/2306-5729/7/11/146)

Main purpose is to predict the chance of student dropout


Project is deployed to the GCP and you can test it here:
[Students dropout prediction](https://dropout-predict-2avfrxfgrq-uc.a.run.app/)


Project files to see:

dataset/dataset.csv - dataset

notebook.ipynb - Jupiter notebook of preparation, exploration of the data, training different models, and choosing the best
train.py - script for training the model, using selected approach and hyper-parameters found in the notebook, and exporting the model to file

model/model.bin - model and DictVectoriser stored by pickle

predict.py - script for running flask server, with API JSON prediction, and prediction throug HTML interface
predict_test.py - prediction test using API JSON
(API using JSON can be reached with [prediction API](https://dropout-predict-2avfrxfgrq-uc.a.run.app/predict))

