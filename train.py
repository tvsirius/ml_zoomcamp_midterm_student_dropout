"""
In this file there is a script for training the final RandomForest model and exporting it

For more detail look to notebook.ipynb

"""
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer

from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score

import pickle

SEED=42

dataset='dataset/dataset.csv'
model_bin='model/model.bin'

# INITIAL READING AND PREPARATION

data=pd.read_csv(dataset)

data.columns = data.columns.str.lower().str.replace(' ', '_')

string_columns = list(data.dtypes[data.dtypes == 'object'].index)

for col in string_columns:
    data[col] = data[col].str.lower().str.replace(' ', '_')

data['dropout']=(data.target=='dropout').astype(int)


data=data.drop(columns='target')

data.rename(columns = {'nacionality':'nationality', 'age_at_enrollment':'age'}, inplace = True)
data.rename(columns={'daytime/evening_attendance':'daytime_or_evening_attendance',"mother's_qualification":"mother_qualification", "father's_qualification":"father_qualification",
       "mother's_occupation":"mother_occupation", "father's_occupation":"father_occupation"}, inplace=True )


# CATEGORICAL FILL IN


marital_status_values={
1:'Single',
2:'Married',
3:'Widower',
4:'Divorced',
5:'Facto union',
6:'Legally separated',}

data.marital_status=data.marital_status.map(marital_status_values)

nationality_values={1:'Portuguese',
2:'German',
3:'Spanish',
4:'Italian',
5:'Dutch',
6:'English',
7:'Lithuanian',
8:'Angolan',
9:'Cape Verdean',
10:'Guinean',
11:'Mozambican',
12:'Santomean',
13:'Turkish',
14:'Brazilian',
15:'Romanian',
16:'Moldova (Republic of)',
17:'Mexican',
18:'Ukrainian',
19:'Russian',
20:'Cuban',
21:'Colombian',
}
data.nationality=data.nationality.map(nationality_values)

application_mode_values={1:'1st phase-general contingent',
2:'Ordinance No. 612/93',
3:'1st phase-special contingent (Azores Island)',
4:'Holders of other higher courses',
5:'Ordinance No. 854-B/99',
6:'International student (bachelor)',
7:'1st phase-special contingent (Madeira Island)',
8:'2nd phase-general contingent',
9:'3rd phase-general contingent',
10:'Ordinance No. 533-A/99, item b2) (Different Plan)',
11:'Ordinance No. 533-A/99, item b3 (Other Institution)',
12:'Over 23 years old',
13:'Transfer',
14:'Change in course',
15:'Technological specialization diploma holders',
16:'Change in institution/course',
17:'Short cycle diploma holders',
18:'Change in institution/course (International)',
}

data.application_mode=data.application_mode.map(application_mode_values)

course_values=	{1:'Biofuel Production Technologies',
2:'Animation and Multimedia Design',
3:'Social Service (evening attendance)',
4:'Agronomy',
5:'Communication Design',
6:'Veterinary Nursing',
7:'Informatics Engineering',
8:'Equiniculture',
9:'Management',
10:'Social Service',
11:'Tourism',
12:'Nursing',
13:'Oral Hygiene',
14:'Advertising and Marketing Management',
15:'Journalism and Communication',
16:'Basic Education',
17:'Management (evening attendance)',
           }

data.course=data.course.map(course_values)


previous_qualification_values=	{1:'Secondary education',
2:'Higher education-bachelor’s degree',
3:'Higher education-degree',
4:'Higher education-master’s degree',
5:'Higher education-doctorate',
6:'Frequency of higher education',
7:'12th year of schooling-not completed',
8:'11th year of schooling-not completed',
9:'Other-11th year of schooling',
10:'10th year of schooling',
11:'10th year of schooling-not completed',
12:'Basic education 3rd cycle (9th/10th/11th year) or equivalent',
13:'Basic education 2nd cycle (6th/7th/8th year) or equivalent',
14:'Technological specialization course',
15:'Higher education-degree (1st cycle)',
16:'Professional higher technical course',
17:'Higher education-master’s degree (2nd cycle)',
}

data.previous_qualification=data.previous_qualification.map(previous_qualification_values)

parents_qualification_values={1:"Secondary Education-12th Year of Schooling or Equivalent",
2:"Higher Education-bachelor’s degree",
3:"Higher Education-degree",
4:"Higher Education-master’s degree",
5:"Higher Education-doctorate",
6:"Frequency of Higher Education",
7:"12th Year of Schooling:-not completed",
8:"11th Year of Schooling:-not completed",
9:"7th Year (Old)",
10:"Other-11th Year of Schooling",
11:"2nd year complementary high school course",
12:"10th Year of Schooling",
13:"General commerce course",
14:"Basic Education 3rd Cycle (9th/10th/11th Year) or Equivalent",
15:"Complementary High School Course",
16:"Technical-professional course",
17:"Complementary High School Course:-not concluded",
18:"7th year of schooling",
19:"2nd cycle of the general high school course",
20:"9th Year of Schooling-not completed",
21:"8th year of schooling",
22:"General Course of Administration and Commerce",
23:"Supplementary Accounting and Administration",
24:"Unknown",
25:"Cannot read or write",
26:"Can read without having a 4th year of schooling",
27:"Basic education 1st cycle (4th/5th year) or equivalent",
28:"Basic Education 2nd Cycle (6th/7th/8th Year) or equivalent",
29:"Technological specialization course",
30:"Higher education-degree (1st cycle)",
31:"Specialized higher studies course",
32:"Professional higher technical course",
33:"Higher Education-master’s degree (2nd cycle)",
34:"Higher Education-doctorate (3rd cycle)",
}

data.mother_qualification=data.mother_qualification.map(parents_qualification_values)
data.father_qualification=data.father_qualification.map(parents_qualification_values)

gender_values={1:'male',
0:'female',
}
data.gender=data.gender.map(gender_values)


daytime_or_evening_attendance_attendance_values={1:'daytime',
0:'evening',
}

data.daytime_or_evening_attendance=data.daytime_or_evening_attendance.map(daytime_or_evening_attendance_attendance_values)


parents_occupation_values={
1:"Student",
2:"Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers",
3:"Specialists in Intellectual and Scientific Activities",
4:"Intermediate Level Technicians and Professions",
5:"Administrative staff",
6:"Personal Services, Security and Safety Workers, and Sellers",
7:"Farmers and Skilled Workers in Agriculture, Fisheries, and Forestry",
8:"Skilled Workers in Industry, Construction, and Craftsmen",
9:"Installation and Machine Operators and Assembly Workers",
10:"Unskilled Workers",
11:"Armed Forces Professions",
12:"Other Situation",
13:"(blank)",
14:"Armed Forces Officers",
15:"Armed Forces Sergeants",
16:"Other Armed Forces personnel",
17:"Directors of administrative and commercial services",
18:"Hotel, catering, trade, and other services directors",
19:"Specialists in the physical sciences, mathematics, engineering, and related techniques",
20:"Health professionals",
21:"Teachers",
22:"Specialists in finance, accounting, administrative organization, and public and commercial relations",
23:"Intermediate level science and engineering technicians and professions",
24:"Technicians and professionals of intermediate level of health",
25:"Intermediate level technicians from legal, social, sports, cultural, and similar services",
26:"Information and communication technology technicians",
27:"Office workers, secretaries in general, and data processing operators",
28:"Data, accounting, statistical, financial services, and registry-related operators",
29:"Other administrative support staff",
30:"Personal service workers",
31:"Sellers",
32:"Personal care workers and the like",
33:"Protection and security services personnel",
34:"Market-oriented farmers and skilled agricultural and animal production workers",
35:"Farmers, livestock keepers, fishermen, hunters and gatherers, and subsistence",
36:"Skilled construction workers and the like, except electricians",
37:"Skilled workers in metallurgy, metalworking, and similar",
38:"Skilled workers in electricity and electronics",
39:"Workers in food processing, woodworking, and clothing and other industries and crafts",
40:"Fixed plant and machine operators",
41:"Assembly workers",
42:"Vehicle drivers and mobile equipment operators",
43:"Unskilled workers in agriculture, animal production, and fisheries and forestry",
44:"Unskilled workers in extractive industry, construction, manufacturing, and transport",
45:"Meal preparation assistants",
46:"Street vendors (except food) and street service providers",
}

data.mother_occupation=data.mother_occupation.map(parents_occupation_values)
data.father_occupation=data.father_occupation.map(parents_occupation_values)


# YES/NO attr 1:'yes    0:'no
# Displaced
# Educational special needs
# Debtor
# Tuition fees up to date
# Scholarship holder
# International

yes_no_categorical_columns=['displaced',  'educational_special_needs', 'debtor', 'tuition_fees_up_to_date',
       'scholarship_holder', 'international']

yes_no_values={
1:'yes', 0:'no'}

for column in yes_no_categorical_columns:
    data[column]=data[column].map(yes_no_values)


data_all=data.drop(columns=['nationality','international','educational_special_needs','unemployment_rate'],
                   inplace=False)


# SPLIT THE DATASET


df_train_full, df_test = train_test_split(data_all, test_size=0.2, random_state=SEED)
y_train_full=df_train_full.dropout.values
# df_train, df_val = train_test_split(df_train_full, test_size=0.25, random_state=SEED)
# y_train = df_train.dropout.values
# y_val = df_val.dropout.values
y_test = df_test.dropout.values

del df_train_full['dropout']
del df_test['dropout']

print(len(data_all))
print(len(df_train_full))
print(len(df_test))

assert len(data_all)==len(df_train_full)+len(df_test)

dict_train_full = df_train_full.to_dict(orient='records')
dict_test = df_test.to_dict(orient='records')

dv = DictVectorizer(sparse=True)
X_train_full = dv.fit_transform(dict_train_full)
X_test = dv.transform(dict_test)


# MODEL TRAINING


n_estimators=180
max_depth=15
min_samples_leaf=3


model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, min_samples_leaf=min_samples_leaf, random_state=SEED)

model.fit(X_train_full, y_train_full)


# METRICS

y_pred_rf = model.predict_proba(X_test)[:, 1]


print(f'Random Forest model trained, accuracy={accuracy_score(y_test, y_pred_rf>=0.5)}, auc={roc_auc_score(y_test, y_pred_rf)}')

# SAVING TO .bin


print(f'Writing to {model_bin} file')

with open(model_bin, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print((dv, model))
print('Writng done...')
