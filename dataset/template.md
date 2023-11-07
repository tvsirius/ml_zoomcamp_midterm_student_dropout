## Explanation of the features and values of categorical 

FIELDS example:
{"marital_status": "Single",
         "application_mode": "Over 23 years old",
         "application_order": 1,
         "course": "Nursing",
         "daytime_or_evening_attendance": "daytime",
         "previous_qualification": "Secondary education",
         "mother_qualification": "General Course of Administration and Commerce",
         "father_qualification": "Basic Education 3rd Cycle (9th/10th/11th Year) or Equivalent",
         "mother_occupation": "Unskilled Workers",
         "father_occupation": "Installation and Machine Operators and Assembly Workers",
         "displaced": "yes",
         "debtor": "no",
         "tuition_fees_up_to_date": "yes",
         "gender": "female",
         "scholarship_holder": "no",
         "age": 27,
         "curricular_units_1st_sem_(credited)": 0,
         "curricular_units_1st_sem_(enrolled)": 7,
         "curricular_units_1st_sem_(evaluations)": 14,
         "curricular_units_1st_sem_(approved)": 0,
         "curricular_units_1st_sem_(grade)": 0.0,
         "curricular_units_1st_sem_(without_evaluations)": 0,
         "curricular_units_2nd_sem_(credited)": 0,
         "curricular_units_2nd_sem_(enrolled)": 7,
         "curricular_units_2nd_sem_(evaluations)": 14,
         "curricular_units_2nd_sem_(approved)": 0,
         "curricular_units_2nd_sem_(grade)": 0.0,
         "curricular_units_2nd_sem_(without_evaluations)": 0,
         "inflation_rate": 0.6,
         "gdp": 2.02}

numerical features is 
[
'application_order', #int
        'age', #int
       'curricular_units_1st_sem_(credited)',#int
       'curricular_units_1st_sem_(enrolled)',#int
       'curricular_units_1st_sem_(evaluations)',#int
       'curricular_units_1st_sem_(approved)',#int
       'curricular_units_1st_sem_(grade)',  #float
       'curricular_units_1st_sem_(without_evaluations)',#int
       'curricular_units_2nd_sem_(credited)',#int
       'curricular_units_2nd_sem_(enrolled)',#int
       'curricular_units_2nd_sem_(evaluations)',#int
       'curricular_units_2nd_sem_(approved)',#int
       'curricular_units_2nd_sem_(grade)',#float
       'curricular_units_2nd_sem_(without_evaluations)',#int
       'inflation_rate', #float
'gdp', #float
]


categorical features is ['marital_status', 'application_mode', 'course',
       'daytime_or_evening_attendance', 'previous_qualification',
       'mother_qualification', 'father_qualification', 'mother_occupation',
       'father_occupation', 'displaced', 'debtor',
       'tuition_fees_up_to_date', 'gender', 'scholarship_holder',
       ]


Categorical feature values:

marital_status_values={
1:'Single',
2:'Married',
3:'Widower',
4:'Divorced',
5:'Facto union',
6:'Legally separated',}

data.marital_status=data.marital_status.map(marital_status_values)

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

mother_qualification_values=
father_qualification_values={1:"Secondary Education-12th Year of Schooling or Equivalent",
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

gender_values={1:'male',
0:'female',
}
data.gender=data.gender.map(gender_values)


daytime_or_evening_attendance_attendance_values={1:'daytime',
0:'evening',
}

data.daytime_or_evening_attendance=data.daytime_or_evening_attendance.map(daytime_or_evening_attendance_attendance_values)


mother_occupation_values=
father_occupation_values=
{
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

other categorical values have this values {'yes','no'}

['displaced', 'debtor', 'tuition_fees_up_to_date','scholarship_holder']