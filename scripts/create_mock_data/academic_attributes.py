import csv, pathlib, os

"""
script that writes data to a csv file for insertion
into a district-education database

"""

path = pathlib.Path.cwd()  #parent directory

#EXAMS TYPES

exam = ['First term', 'Second term','Term term',  
        'First mock','Second mock','Third mock'
        ]    
num = 1          
with open(os.path.join(path,'data/seeds/exam.csv'),'w') as file:
    file_writer = csv.DictWriter(file,['id','exam_name'])
    file_writer.writeheader()
    for ex in exam:
        file_writer.writerow({'id':num,'exam_name':ex})
        num += 1


#STUDENT LEVEL

student_levels = ['KG ONE','KG TWO','BASIC ONE','BASIC TWO','BASIC THREE',
                  'BASIC FOUR','BASIC FIVE','BASIC SIX','BASIC SEVEN',
                  'BASIC EIGTH','BASIC NINE']
num = 1
with open(os.path.join(path,'data/seeds/student_level.csv'),'w') as file:
    file_writer = csv.DictWriter(file,['id','level_name'])
    file_writer.writeheader()
    for level in student_levels:
        file_writer.writerow({'id':num,'level_name':level})
        num += 1

#SUBJECT
kg_subjects = [
                'Literacy','Numeracy','Owop','Creative Arts'
                
                ]

lower_primary_subjects = [
            'English Language','Mathematics','Integrated Science','History','Creative Arts',
            'Ghanaian Language','Religious And Moral Ed.']

upper_primary_subjects = [
                    'English Language','Mathematics','Integrated Science','History',
                    'Creative Arts','Ghanaian Language','Religious And Moral Ed.','Computing'
            ]           

jhs_subjects = [
            'English Language','Mathematics','Integrated Science','Creative Arts','Ghanaian Language','Religious And Moral Ed.',
            'Computing','Social Studies','Career Technology']

def all_subjects():
    subject_ids = {}

    kg_subjects.extend(lower_primary_subjects)
    kg_subjects.extend(upper_primary_subjects)
    kg_subjects.extend(jhs_subjects)

    n = 1
    for sub in kg_subjects:
        if sub not in subject_ids.values():
            subject_ids[n] = sub
            n += 1
    return subject_ids

def get_subject_id(subs_ids:dict)->dict:

    ids = {}
    for key, value in subs_ids.items():
        ids[value] = key
        
    return ids

def write_subjects(subjects,file_name):
    num = 1
    with open(os.path.join(path,'data/seeds', file_name +'.csv'),'w') as file:
        file_writer = csv.DictWriter(file,['id','subject_name'])
        file_writer.writeheader()
        for subject in subjects:
            file_writer.writerow({'id':num,'subject_name':subject})
            num += 1

def get_subjects(file_name):

    path = os.path.join(pathlib.Path.cwd(),'data/seeds',file_name + '.csv') 
    try:
        with open(path) as file:
            return  [i for i in csv.DictReader(file,delimiter=',')]
    except FileNotFoundError:
        return []

#MOTIVATTION LOOKUP

def write_motivation_lookup():
    lables = [
                'High','Moderate','Low'
    ]

    score_value =[
                5,3,1
    ] 

    num = 1
    with open(os.path.join(path,'data/seeds/motivation_lookup.csv'),'w') as file:
        file_writer = csv.DictWriter(file,['id','lable','score_value'])
        file_writer.writeheader()
        for lable,value in zip(lables,score_value):
            file_writer.writerow({'id':num,'lable':lable,'score_value':value})
            num += 1

#CONDUCT
def write_conduct():                
    lables = [
        'Constructive','Passive','Disruptive'
    ]
    score_value =[
                5,3,1
    ]       

    num = 1

    with open(os.path.join(path,'data/seeds/conduct_lookup.csv'),'w') as file:
        file_writer = csv.DictWriter(file,['id','lable','score_value'])
        file_writer.writeheader()
        for lable,value in zip(lables,score_value):
            file_writer.writerow({'id':num,'lable':lable,'score_value':value})
            num += 1

def write_academic_years():
    academic_year1 = 2025
    academic_year2 = 2026
    academic_years = {n+1:str(academic_year1 -(10 - n)) +'/'+ str(academic_year2 - (10 - n)) for n
                      in range(10)}
    with open(os.path.join(pathlib.Path.cwd(),'data/seeds/academic_years.csv'),'w') as file:
        file_writer = csv.DictWriter(file,['id','year'])
        file_writer.writeheader()
        for key in academic_years.keys():
            file_writer.writerow({'id':key,'year':academic_years[key]})

def get_academic_year():
    with open(os.path.join(pathlib.Path.cwd(),'data/seeds/academic_years.csv'),'r') as file:
        file_reader = csv.DictReader(file, delimiter=',')
        return [ i for i in file_reader]
    
def get_academic_year_id(year:str):

    academic_year = get_academic_year()
    for x in academic_year:
        if x['year'] == year:
            return list(x.values())[0]




# files = {'kg':kg_subjects,'lower_primary':lower_primary_subjects,
#          'upper_primary':upper_primary_subjects,'jhs':jhs_subjects}
# for key in files.keys():
#     if key == 'kg':
#         write_subjects(files[key],'kg_subjects')
#     elif key == 'lower_primary':
#         write_subjects(files[key],'lower_primary_subjects')
#     elif key == 'upper_primary':
#         write_subjects(files[key],'upper_primary_subjects')
#     else:
#         write_subjects(files[key],'jhs_subjects')