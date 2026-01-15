import csv, pathlib, os,random
from uuid6 import uuid7
from faker import Faker
from employee import generate_email



"""
script that writes data to a csv file for insertion
into a district-education database

"""


# id UUID PRIMARY KEY DEFAULT uuid_generate_v7(),
#     prefix_id INT NOT NULL,
#     first_name VARCHAR(50) NOT NULL,
#     last_name VARCHAR(50) NOT NULL,
#     other_name VARCHAR(70) NULL,
#     email VARCHAR9(70) NULL,
#     phone VARCHAR(14) [],
#     gender gender_type NOT NULL,
#     education_level_id INT NOT NULL,
#     occupation_id INT NOT NULL,
#     address_id INT NOT NULL,
#     student_id UUID NOT NULL INDEX,
#     guardian_student_relationship_id INT  NOT NULL,
#     date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     CONSTRAINT fk_address_id FOREIGN KEY REFERENCES address (id),
#     CONSTRAINT fk_student_id FOREIGN KEY REFERENCES student (id),
#     CONSTRAINT fk_pefix_id FOREIGN KEY (prefix_id) REFERENCES name_prefix_lookup(id)
#     CONSTRAINT fk_guardian_student_relationship_id FOREIGN KEY (guardian_student_relationship_id) REFERENCES guardian_student_relationship(id),
#     CONSTRAINT fk_occupation_id FOREIGN KEY (occupation_id) REFERENCES occupation (id),
#     CONSTRAINT fk_guardian_education_level FOREIGN KEY (education_level) REFERENCES education_level(id)

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
    guardian_stu_rela = rela
    date_created = fake.date_between()

     # get a middle name or not
    dec = random.randint(1,2)     
    if dec == 1:
        other_name = fake.first_name_female()
        email = generate_email([first_name,other_name,last_name])
        return [id,title,first_name,last_name,other_name,email,phone,gender,
                educational_level,occupation,address_id,student_id,
                guardian_stu_rela,date_created]
    else:
        other_name = 'N/A'
        email = generate_email([first_name,last_name])
        return [id,title,first_name,last_name,other_name,email,phone,gender,
                educational_level,occupation,address_id,student_id,
                guardian_stu_rela,date_created]

def create_guardian_male(rela:int,address_id:int,student_id):

    fake = Faker("en_US")

    id = uuid7()
    title = random.randint(1,22)
    first_name = fake.first_name_male()
    last_name = fake.last_name()
    phone = '"' + '{' + f"{fake.basic_phone_number()}" +','+   f"{fake.basic_phone_number()}" + '}' + '"' 
    gender = "Male"
    educational_level = random.randint(1,5)
    occupation = random.randint(1,20)
    address_id = address_id
    student_id = student_id
    guardian_stu_rela = rela
    date_created = fake.date_between()

     # get a middle name or not
    dec = random.randint(1,2)     
    if dec == 1:
        other_name = fake.first_name_male()
        email = generate_email([first_name,other_name,last_name])
        return [id,title,first_name,last_name,other_name,email,phone,gender,
                educational_level,occupation,address_id,student_id,
                guardian_stu_rela,date_created]
    else:
        other_name = 'N/A'
        email = generate_email([first_name,last_name])
        return [id,title,first_name,last_name,other_name,email,phone,gender,
                educational_level,occupation,address_id,student_id,
                guardian_stu_rela,date_created]

def write_stu_guardian_rela():
    relationships = [
        'Mother', 'Father', 'Stepparent','Grandparent', 
    'Aunt', 'Uncle', 'Cousin','Sibling','Legal Guardian', 
    'Foster Parent', 'Host Parent', 'Social Worker',
    'Family Friend','Other'
    ]

    path = pathlib.Path.cwd()  #parent directory


    with open(os.path.join(path,'data/seeds/stu_guardian_rela.csv'),'w') as file:
        file_writer = csv.DictWriter(file,['id','relationship'])
        file_writer.writeheader()

        num = 1
        for rela in relationships:
            file_writer.writerow({'id':num,'relationship':rela})
            n += 1

def get_stu_guardian_rela():

    path = pathlib.Path.cwd()  #parent directory


    with open(os.path.join(path,'data/seeds/stu_guardian_rela.csv'),'r') as file:
        relationships = [i for i in csv.DictReader(file,delimiter=',')]
        return relationships

def write_guardian(guardians:list):

    path = pathlib.Path.cwd()  #parent directory

    with open(os.path.join(path,'data/seeds/guardians.csv'),'w') as file:
        file_writer = csv.DictWriter(file,['id','first_name','last_name','other_name','email','phone',
                                           'gender','educational_level','occupation','address_id',
                                           'student_id','guardian_stu_rela','date_created'])
        file_writer.writeheader()
    
        for guardian in guardians:
            file_writer.writerow({'id':guardian[0],'first_name':guardian[1],'last_name':guardian[2],
                                  'other_name':guardian[3],'email':guardian[4],'phone':guardian[5],
                                  'gender':guardian[6],'educational_level':guardian[7],'occupation':guardian[8],
                                  'address_id':guardian[9],'student_id':guardian[10],'guardian_stud_id':guardian[11],
                                  'date_created':guardian[12]})


