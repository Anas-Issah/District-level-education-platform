import csv, pathlib, os,random
from uuid6 import uuid7
from faker import Faker
from employee import generate_email



"""
script that writes data to a csv file for insertion
into a district-education database

"""




def create_guardian_female(rela:int,address_id:int,student_id):

    fake = Faker("en_US")

    id = uuid7()
    title = random.randint(1,22)
    first_name = fake.first_name_female()
    last_name = fake.last_name()
    phone = '"' + '{' + f"{fake.basic_phone_number()}" +','+   f"{fake.basic_phone_number()}" + '}' + '"' 
    gender = "Female"
    educational_level = random.randint(1,5)
    occupation = random.randint(1,20)
    address_id = address_id
    student_id = student_id
    date_created = fake.date_between()

     # get a middle name or not
    dec = random.randint(1,2)     
    if dec == 1:
        other_name = fake.first_name_female()
        email = generate_email([first_name,other_name,last_name])
        return [id,title,first_name,last_name,other_name,email,phone,gender,
                educational_level,occupation,address_id,student_id,
                rela,date_created]
    else:
        other_name = 'N/A'
        email = generate_email([first_name,last_name])
        return [id,title,first_name,last_name,other_name,email,phone,gender,
                educational_level,occupation,address_id,student_id,
                rela,date_created]

def create_guardian_male(rela:int,address_id:int,student_id):

    fake = Faker("en_US")

    id = uuid7()
    title = random.randint(1,22)
    first_name = fake.first_name_male()
    last_name = fake. last_name()
    phone = '"' + '{' + f"{fake.basic_phone_number()}" +','+   f"{fake.basic_phone_number()}" + '}' + '"' 
    gender = "Male"
    educational_level = random.randint(1,5)
    occupation = random.randint(1,20)
    address_id = address_id
    student_id = student_id
    date_created = fake.date_between()

     # get a middle name or not
    dec = random.randint(1,2)     
    if dec == 1:
        other_name = fake.first_name_male()
        email = generate_email([first_name,other_name,last_name])
        return [id,title,first_name,last_name,other_name,email,phone,gender,
                educational_level,occupation,address_id,student_id,
                rela,date_created]
    else:
        other_name = 'N/A'
        email = generate_email([first_name,last_name])
        return [id,title,first_name,last_name,other_name,email,phone,gender,
                educational_level,occupation,address_id,student_id,
                rela,date_created]

def create_parent_guardian(parent:dict)-> list:

    fake = Faker('en_Us')
    id = parent['id']
    title = parent['title']
    first_name = parent['first_name']
    last_name = parent['last_name']
    other_name = parent['other_name']
    email = parent['email']
    phone = parent['phone']
    gender = 'Female' if parent['relationship'] == 'Mother' else 'Male'
    educational_level = parent['educational_level']
    occupation = parent['occupation']
    address_id = parent['address_id']
    student_id = parent['student_id']
    guardian_stu_rela = 1 if parent['relationship'] == 'Mother' else 2
    date_created = fake.date_between()

    return [id,title,first_name,last_name,other_name,email,phone,gender,
                educational_level,occupation,address_id,student_id,
                guardian_stu_rela,date_created]
    
def write_stu_guardian_rela():
    relationships = [
    'Mother', 'Father', 'Stepparent','Grandparent', 
     'Aunt','Uncle', 'Cousin','Sibling','Legal Guardian', 
    'Foster Parent', 'Host Parent', 'Social Worker',
    'Family Friend','Other'
    ]

    path = pathlib.Path.cwd()  #parent directory


    with open(os.path.join(path,'data/seeds/stu_guardian_rela.csv'),'a') as file:
        file_writer = csv.DictWriter(file,['id','relationship'])
        file_writer.writeheader()

        num = 1
        for rela in relationships:
            file_writer.writerow({'id':num,'relationship':rela})
            num += 1

def get_stu_guardian_rela():

    path = pathlib.Path.cwd()  #parent directory


    with open(os.path.join(path,'data/seeds/stu_guardian_rela.csv'),'r') as file:
        relationships = [i for i in csv.DictReader(file,delimiter=',')]
        return relationships
    
def header_writer():
    path = os.path.join(pathlib.Path.cwd(),'data/seeds/students.csv')
   
    if pathlib.Path(path).exists() == False:
        with open(path,'w') as file:
            file_writer = csv.DictWriter(file,['id','first_name','last_name','other_name','email','phone',
                                           'gender','educational_level','occupation','address_id',
                                           'student_id','guardian_stu_rela_id','date_created'])
            file_writer.writeheader()

def write_guardian(guardians:list):

    header_writer()
    path = pathlib.Path.cwd()  #parent directory

    with open(os.path.join(path,'data/seeds/guardian.csv'),'a') as file:
        file_writer = csv.writer(file)
    
        for guardian in guardians:
            file_writer.writerow([guardian[0],guardian[1],guardian[2],guardian[3],guardian[4],
                                  guardian[5],guardian[6],guardian[7],guardian[8],guardian[9],
                                  guardian[10],guardian[11],guardian[12]])


