import csv, pathlib, os

"""
script that writes data to a csv file for insertion
into a district-education database

"""

path = pathlib.Path.cwd()  #parent directory
"""
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

subjects = [
    'English Language','Mathematics','Integrated Science','Social Studies','Computing',
            'Career Technology','Creative Arts','Asante Twi','French','Religious And Moral Ed.']

num = 1
with open(os.path.join(path,'data/seeds/subject.csv'),'w') as file:
    file_writer = csv.DictWriter(file,['id','subject_name'])
    file_writer.writeheader()
    for subject in subjects:
        file_writer.writerow({'id':num,'subject_name':subject})
        num += 1
"""

#MOTIVATTION LOOKUP

lables = [
            'High','Moderate','Low'
]

score_value =[
            5,3,1
] 

num = 1
with open(os.path.join(path,'data/seeds/motivation_lookup.csv'),'w') as file:
    file_writer = csv.DictWriter(file,['id','label','score_value'])
    file_writer.writeheader()
    for lable,value in zip(lables,score_value):
        file_writer.writerow({'id':num,'label':lable,'score_value':value})
        num += 1

#CONDUCT
lables = [
    'Constructive','Passive','Disruptive'
]

num = 1

with open(os.path.join(path,'data/seeds/conduct_lookup.csv'),'w') as file:
    file_writer = csv.DictWriter(file,['id','label','score_value'])
    file_writer.writeheader()
    for lable,value in zip(lables,score_value):
        file_writer.writerow({'id':num,'label':lable,'score_value':value})
        num += 1

