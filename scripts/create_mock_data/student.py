import csv, pathlib, os,sys,random
from faker import Faker
from uuid6 import uuid7
"""
script that writes data to a csv file for insertion
into a district-education database

"""

path = pathlib.Path.cwd()  #parent directory


def gen_female_stu()-> list:

    
    fake = Faker("en_US")

    id = uuid7()
    first_name = fake.first_name_female()
    last_name = fake.last_name()
    school_id = ''
    birth_date = fake.date_between_dates()
    admission_date = ''
    student_level_id = ''
    date_created = ''

    # get a middle name or not
    dec = random.randint(1,2)     
    if dec == 1:
        other_name = fake.first_name()
        return[
            id,first_name,last_name,other_name,school_id,birth_date,admission_date,
            student_level_id,date_created
        ]
    else:
        other_name = 'N/A'
        return[
            id,first_name,last_name,other_name,school_id,birth_date,admission_date,
            student_level_id,date_created
        ]

def gen_male_stu():

    
    fake = Faker("en_US")

    id = uuid7()
    first_name = fake.first_name_male()
    last_name =fake.last_name()
    school_id = ''
    birth_date = fake.date_between_dates()
    admission_date = ''
    student_level_id = ''
    date_created = ''

    # get a middle name or not
    dec = random.randint(1,2)     
    if dec == 1:
        other_name = fake.first_name()
        return[
            id,first_name,last_name,other_name,school_id,birth_date,admission_date,
            student_level_id,date_created
        ]
    else:
        other_name = 'N/A' 
        return[
            id,first_name,last_name,other_name,school_id,birth_date,admission_date,
            student_level_id,date_created
        ]


# create students
students = []

dec = [1,2]

for x in range(10):    
    students.append(gen_female_stu())

for x in range(10):    
    students.append(gen_male_stu())
          
#write students to file   
with open(os.path.join(path,'data/seeds/student.csv'),'w') as file:
    file_writer = csv.DictWriter(file,['id','first_name','last_name','other_name','school_id',
                                       'birth_date','admission_date','student_level_id','date_created'])
    file_writer.writeheader()

    for student in students:
        file_writer.writerow({'id':student[0],'first_name':student[1],'last_name':student[2],
                              'other_name':student[3],'school_id':student[4],
                            'birth_date':student[5],'admission_date':student[6],
                            'student_level_id':student[7],'date_created':student[8]})



