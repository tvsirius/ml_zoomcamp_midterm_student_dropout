#!/usr/bin/env python
# coding: utf-8

import requests

#url = 'http://localhost:9696/predict'
url = 'https://dropout-predict-2avfrxfgrq-uc.a.run.app/predict'

from sample_studs import *

for i,stud,stud_real in [(1,stud1,stud1_dropout),
                       (2,stud2,stud2_dropout),
                       (3,stud3,stud3_dropout),
                       (4,stud4,stud4_dropout),
                       (5,stud5,stud5_dropout),
                       (6,stud6,stud6_dropout),
                       ]:
    response = requests.post(url, json=stud).json()

    print(f'for {i} test student response is {response["dropout_probability"]}, and real target is {stud_real}')
