import csv, pathlib, os,random,datetime,math
from faker import Faker
from uuid6 import uuid7

import parents
import address
"""
script that writes data to a csv file for insertion
into a district-education database

"""

path = pathlib.Path.cwd()  #parent directory


def gen_female_stu(sch_id,lvl)-> list:

    
    fake = Faker("en_US")

    id = uuid7()
    first_name = fake.first_name_female()
    last_name = fake.last_name()
    school_id = sch_id
    # determine birth date 
    if lvl == 1:
        birth_date = fake.date_between(start_date='-5y',end_date='4y')
    elif lvl == 2:
        birth_date = fake.date_between(start_date='-6y',end_date='5y')
    elif lvl == 3:
        birth_date = fake.date_between(start_date='-7y',end_date='6y')
    elif lvl == 4:
        birth_date = fake.date_between(start_date='-8y',end_date='-7y')
    elif lvl == 5:
        birth_date = fake.date_between(start_date='-9y',end_date='-8y')
    elif lvl == 6:
        birth_date = fake.date_between(start_date='-10y',end_date='-9y')
    elif lvl == 7:
        birth_date = fake.date_between(start_date='-11',end_date='10')
    elif lvl == 8:
        birth_date = fake.date_between(start_date='-12y',end_date='-11y')
    elif lvl == 9:
        birth_date = fake.date_between(start_date='-13y',end_date='12y')
    elif lvl == 10:
        birth_date = fake.date_between(start_date='-14y',end_date='13y')
    else:
        birth_date = fake.date_between(start_date='-16y',end_date='14y')
        
    
    admission_date = fake.date_between(start_date='-1y',end_date='-0y')
    student_level_id = lvl
    date_created = datetime.date.today()

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

def gen_male_stu(sch_id,lvl):

    
    fake = Faker("en_US")

    id = uuid7()
    first_name = fake.first_name_male()
    last_name =fake.last_name()
    school_id =sch_id
    # determine birth date 
    if lvl == 1:
        birth_date = fake.date_between(start_date='-5y',end_date='4y')
    elif lvl == 2:
        birth_date = fake.date_between(start_date='-6y',end_date='5y')
    elif lvl == 3:
        birth_date = fake.date_between(start_date='-7y',end_date='6y')
    elif lvl == 4:
        birth_date = fake.date_between(start_date='-8y',end_date='-7y')
    elif lvl == 5:
        birth_date = fake.date_between(start_date='-9y',end_date='-8y')
    elif lvl == 6:
        birth_date = fake.date_between(start_date='-10y',end_date='-9y')
    elif lvl == 7:
        birth_date = fake.date_between(start_date='-11',end_date='10')
    elif lvl == 8:
        birth_date = fake.date_between(start_date='-12y',end_date='-11y')
    elif lvl == 9:
        birth_date = fake.date_between(start_date='-13y',end_date='12y')
    elif lvl == 10:
        birth_date = fake.date_between(start_date='-14y',end_date='13y')
    else:
        birth_date = fake.date_between(start_date='-16y',end_date='14y')

    admission_date = fake.date_between(start_date='-1',end_date='0y')
    student_level_id = lvl
    date_created = datetime.date.today()

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
    
def write_student(students:list):

    with open(os.path.join(path,'data/seeds/student.csv'),'w') as file:
        file_writer = csv.DictWriter(file,['id','first_name','last_name','other_name','school_id',
                                        'birth_date','admission_date','student_level_id','date_created'])
        file_writer.writeheader()

        for student in students:
            file_writer.writerow({'id':student[0],'first_name':student[1],'last_name':student[2],
                                'other_name':student[3],'school_id':student[4],
                                'birth_date':student[5],'admission_date':student[6],
                                'student_level_id':student[7],'date_created':student[8]})


# read schools file
with open(os.path.join(path,'data/seeds/school.csv'),'r') as file:
    file_reader = csv.DictReader(file,delimiter=',')
    school_attr = [{'id' :int(i['id']),'school_lvl':int(i['school_level'])}for i in file_reader]    #store school id's in a list

for school in school_attr:
    #kindergarten
    if school['school_lvl'] == 1:           
        population = random.randint(101,220) # get population of the school
        cls_1 = math.floor(population/2)   - random.randint(1,10)
        for _ in range(cls_1):
            gend_dec = random.randint(1,2) # pick a gender
            if gend_dec == 1:
                student = gen_female_stu(school['id'],1)
                #decide if parents live together or not
                dec = random.randint(1,4)
                if dec > 3:
                    mother = parents.mother(address.create_address(),student[0])
                    father = parents.father(address.create_address(),student[0])
                else:
                    adrs = address.create_address()
                    mother = parents.mother(adrs,student[0])
                    father =parents.father(adrs,student[0])
              
            else:
                student = gen_male_stu(school['id'],1)
                #decide if parents live together or not
                dec = random.randint(1,4)
                if dec > 3:
                    mother = parents.mother(address.create_address(),student[0])
                    father = parents.father(address.create_address(),student[0])
                else:
                    adrs = address.create_address()
                    mother = parents.mother(adrs,student[0])
                    father =parents.father(adrs,student[0])
               
        for _ in range(population - cls_1):
            gend_dec = random.randint(1,2) # pick a gender
            if gend_dec == 1:
                student = gen_female_stu(school['id'],2)
                #decide if parents live together or not
                dec = random.randint(1,4)
                if dec > 3:
                    mother = parents.mother(address.create_address(),student[0])
                    father = parents.father(address.create_address(),student[0])
                else:
                    adrs = address.create_address()
                    mother = parents.mother(adrs,student[0])
                    father =parents.father(adrs,student[0])
            else:
                student = gen_male_stu(school['id'],2)
                #decide if parents live together or not
                dec = random.randint(1,4)
                if dec > 3:
                    mother = parents.mother(address.create_address(),student[0])
                    father = parents.father(address.create_address(),student[0])
                else:
                    adrs = address.create_address()
                    mother = parents.mother(adrs,student[0])
                    father =parents.father(adrs,student[0])
              





