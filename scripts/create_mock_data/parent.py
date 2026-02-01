import csv, pathlib, os,random
from uuid6 import uuid7
from faker import Faker
from employee import generate_email



"""
script that writes data to a csv file for insertion
into a district-education database

"""

path = pathlib.Path.cwd()  #parent directory



def mother(adr:str,stu_id:str)->list:
    """
    Docstring for mother
    
    :return: list containing parent(mother) details
    :rtype: list[Any]
    """
    fake = Faker("en_US")

    id = uuid7()
    title = random.randint(1,22)
    first_name = fake.first_name_female()
    last_name = fake.last_name()
    phone =   '{"' + fake.basic_phone_number() + '","' + fake.basic_phone_number() + '"}' 
    relatioship = 'Mother'
    educational_level = random.randint(1,5)
    occupation = random.randint(1,20)
    address_id = adr
    life_status = random.randint(1,30)
    alive_stutus = 'Alive' if life_status < 29 else 'Deceased'
    studen_id = stu_id
    date_created = fake.date_between()

    # get a middle name or not
    dec = random.randint(1,2)     
    if dec == 1:
        other_name = fake.first_name()
        email = generate_email([first_name,other_name,last_name])
        return [id,title,first_name,last_name,other_name,email,phone,relatioship,educational_level,
                occupation,address_id,alive_stutus,studen_id,date_created]
    else:
        other_name = 'N/A'
        email = generate_email([first_name,last_name])
        return [id,title,first_name,last_name,other_name,email,phone,relatioship,educational_level,
                occupation,address_id,alive_stutus,studen_id,date_created]
    

def father(adr:str,stu_id:str)->list:
    """
    Docstring for mother
    
    :return: list containing parent(mother) details
    :rtype: list[Any]
    """
    fake = Faker("en_US")

    id = uuid7()
    title = random.randint(1,22)
    first_name = fake.first_name_male()
    last_name = fake.last_name()
    phone =   '{"' + fake.basic_phone_number() + '","' + fake.basic_phone_number() + '"}' 
    relatioship = 'Father'
    educational_level = random.randint(1,5)
    occupation = random.randint(1,20)
    address_id = adr
    life_status = random.randint(1,30)
    alive_stutus = 'Alive' if life_status < 29 else 'Deceased'
    studen_id = stu_id
    date_created = fake.date_between()

    # get a middle name or not
    dec = random.randint(1,2)     
    if dec == 1:
        other_name = fake.first_name()
        email = generate_email([first_name,other_name,last_name])
        return [id,title,first_name,last_name,other_name,email,phone,relatioship,educational_level,
                occupation,address_id,alive_stutus,studen_id,date_created]
    else:
        other_name = 'N/A'
        email = generate_email([first_name,last_name])
        return [id,title,first_name,last_name,other_name,email,phone,relatioship,educational_level,
                occupation,address_id,alive_stutus,studen_id,date_created]

def header_writer():
    path = os.path.join(pathlib.Path.cwd(),'data/seeds/parents.csv')
   
    if pathlib.Path(path).exists() == False:
        with open(path,'w') as file:
            file_writer = csv.DictWriter(file,['id','title','first_name','last_name','other_name','email','phone',
                                        'relationship','educational_level','occupation','address_id',
                                        'alive_status','student_id','date_created'])
            file_writer.writeheader()
        
def write_parent(parents:list):

    header_writer()
    with open(os.path.join(path,'data/seeds/parents.csv'),'a') as file:
        file_writer = csv.writer(file)
        for parent in parents:
            file_writer.writerow([parent[0],parent[1],parent[2],parent[3],parent[4],parent[5],parent[6],parent[7],parent[8],parent[9],parent[10],parent[11],parent[12],parent[13]])
def get_parents():

    with open(os.path.join(pathlib.Path.cwd(),'data/seeds/parents.csv'),'r') as file:
        parents = [i for i in csv.DictReader(file,delimiter=',')]
        return parents
    