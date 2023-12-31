"""
Flask server for prediction serving of the model

Have endpoints:
/predict - for API predictions in JSON
/ - return main.html (HTML with form and script)
/predict_form - POST request predict processing with returing str with prediction to the script in HTML

"""
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer

from flask import Flask, request, jsonify, render_template

import pickle

DROPOUT_THRESHOLD = 0.5

model_bin = 'model/model.bin'


# LOADING MODEL

print(f'Reading from {model_bin} file')

with open(model_bin, 'rb') as f_in:
    dv, model = pickle.load(f_in)

print((dv, model))
print('Reading done...')




def predict_single(student, dv, model):
    """
    Helper function for making predictions

    :param student: dict with all student data (must contain features)
    :param dv: DictVectorizer
    :param model: RandomForestClassifier
    :return: prediction of dropout using given params
    """
    X = dv.transform([student])
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred[0]



app = Flask('dropout')


@app.route('/predict', methods=['POST'])
def predict():
    """
    Flask routine for processing JSON request on the /predict endpoint
    request -> json with student data

    :return: -> json with model prediction
    """
    student = request.get_json()


    # PREDICTION
    prediction = predict_single(student, dv, model)
    dropout = prediction >= DROPOUT_THRESHOLD

    result = {
        'dropout_probability': float(prediction),
        'dropout': bool(dropout),
    }

    print('--------\nPredict by API /predict ')
    print('\n--student---', student, '\n---prediction---\n',
          f'Dropout probability: {prediction:.3f}\n    Is dropout: {dropout}\n---------------\n')

    return jsonify(result)


@app.route('/', methods=['GET'])
def main_get():
    """
    Flask routine for entering via browser, to get base page with form and script

    :return: main.html
    """
    return render_template('main.html')


@app.route('/predict_form', methods=['POST'])
def predict_form():
    """
    Flask routine for processing request from main.html script

    :return: str with model predition to display in browser
    """

    student = {}

    # filling the student dict with features from request

    categorical_features = [
        'marital_status', 'application_mode', 'course',
        'daytime_or_evening_attendance', 'previous_qualification',
        'mother_qualification', 'father_qualification', 'mother_occupation',
        'father_occupation', 'displaced', 'debtor',
        'tuition_fees_up_to_date', 'gender', 'scholarship_holder'
    ]
    for feature in categorical_features:
        student[feature] = request.form.get(feature)
        # Check so feature MUST BE in request
        if student[feature] is None:
            raise KeyError(f'{feature} not in request!!!')

    # Extract numerical features
    numerical_features = [
        'application_order', 'age',
        'curricular_units_1st_sem_(credited)',
        'curricular_units_1st_sem_(enrolled)',
        'curricular_units_1st_sem_(evaluations)',
        'curricular_units_1st_sem_(approved)',
        'curricular_units_1st_sem_(grade)',
        'curricular_units_1st_sem_(without_evaluations)',
        'curricular_units_2nd_sem_(credited)',
        'curricular_units_2nd_sem_(enrolled)',
        'curricular_units_2nd_sem_(evaluations)',
        'curricular_units_2nd_sem_(approved)',
        'curricular_units_2nd_sem_(grade)',
        'curricular_units_2nd_sem_(without_evaluations)',
        'inflation_rate',
        'gdp'
    ]
    numerical_features_float = ['curricular_units_1st_sem_(grade)', 'curricular_units_2nd_sem_(grade)',
                                'inflation_rate', 'gdp']

    for feature in numerical_features:
        student[feature] = request.form.get(feature)
        # Check so feature MUST BE in request

        if student[feature] is None:
            raise KeyError(f'{feature} not in request!!!')

        # int and float will be str in request, so i need to convert, and assing 0 if they are blank

        try:
            if feature in numerical_features_float:
                student[feature] = float(student[feature])
            else:
                student[feature] = int(student[feature])
        except:
            student[feature] = 0


    # PREDICTION
    prediction = predict_single(student, dv, model)
    dropout = prediction >= DROPOUT_THRESHOLD

    print('Predict by form /predict_form ')

    print('\n--student---', student, '\n---prediction---\n',
          f'Dropout probability: {prediction:.3f}\n    Is dropout: {dropout}\n---------------\n')

    return f'Dropout probability: {prediction:.3f}\n    Is dropout: {dropout}'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
