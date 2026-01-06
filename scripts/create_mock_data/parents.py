import csv, pathlib, os,sys,random
from uuid6 import uuid7
from faker import Faker
from employee import genrate_email



"""
script that writes data to a csv file for insertion
into a district-education database

"""

path = pathlib.Path.cwd()  #parent directory



def mother()->list:
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
    phone = '"' + '{' + f"{fake.basic_phone_number()}" +','+   f"{fake.basic_phone_number()}" + '}' + '"' 
    relatioship = 'Mother'
    educational_level = random.randint(1,5)
    occupation = random.randint(1,20)
    address_id = 'null'
    alive_stutus = random.choice(['Alive','Deceased'])
    studen_id = ''
    date_created = fake.date_between()

    # get a middle name or not
    dec = random.randint(1,2)     
    if dec == 1:
        other_name = fake.first_name()
        email = genrate_email([first_name,other_name,last_name])
        return [id,title,first_name,last_name,other_name,email,phone,relatioship,educational_level,
                occupation,address_id,alive_stutus,studen_id,date_created]
    else:
        other_name = 'N/A'
        email = genrate_email([first_name,last_name])
        return [id,title,first_name,last_name,other_name,email,phone,relatioship,educational_level,
                occupation,address_id,alive_stutus,studen_id,date_created]
    

def father()->list:
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
    phone = '"' + '{' + f"{fake.basic_phone_number()}" +','+   f"{fake.basic_phone_number()}" + '}' + '"' 
    relatioship = 'Father'
    educational_level = random.randint(1,5)
    occupation = random.randint(1,20)
    address_id = 'null'
    alive_stutus = random.choice(['Alive','Deceased'])
    studen_id = ''
    date_created = fake.date_between()

    # get a middle name or not
    dec = random.randint(1,2)     
    if dec == 1:
        other_name = fake.first_name()
        email = genrate_email([first_name,other_name,last_name])
        return [id,title,first_name,last_name,other_name,email,phone,relatioship,educational_level,
                occupation,address_id,alive_stutus,studen_id,date_created]
    else:
        other_name = 'N/A'
        email = genrate_email([first_name,last_name])
        return [id,title,first_name,last_name,other_name,email,phone,relatioship,educational_level,
                occupation,address_id,alive_stutus,studen_id,date_created]
   
# create employees
parents = []

choice = random.randint(1,2)
for x in range(500):
    parents.append(mother())
    parents.append(father)

# write employees to file
with open(os.path.join(path,'data/seeds/parents.csv'),'w') as file:
    file_writer = csv.DictWriter(file,['id','first_name','last_name','other_name','email','phone',
                                       'relationship','educational_level','occupation','address_id',
                                       'alive_status','student_id','date_created'])
    file_writer.writeheader()

    for parent in parents:
        file_writer.writerow({'id':parent[0],'first_name':parent[1],'last_name':parent[2],
                              'other_name':parent[3],'email':parent[4],'phone':parent[5],
                              'relationship':parent[6],
                              'educational_level':parent[7],'occupation':parent[8],
                              'address_id':parent[9],'alive_status':parent[10],'student_id':parent[11],
                              'date_created':parent[12]})

