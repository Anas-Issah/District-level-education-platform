import csv, pathlib, os,sys,random
from uuid6 import uuid7
from faker import Faker
from employee_attribute import ranks, specialities, religions, educational_level



"""
script that writes data to a csv file for insertion
into a district-education database

"""

path = pathlib.Path.cwd()  #parent di
fake = Faker("en_US")

gender = ['Male','Female']



def generate_staff_id(num:int) -> str:
    """
    Docstring for generate_staff_id
    
    :param num: a counter
    :type num: int
    :return: a string representing mock staff id
    :rtype: str
    """ 
    prefix = '00'
    if num < 10:
        return prefix + '00' + str(num)
    elif num < 100:
        return prefix + '0' + str(num)
    else:
        return prefix + str(num)     
    
def generate_liscence_num()-> str:
    prefix = 'QT/0'

    return '' 
def genrate_email(name:list)->str:
    """
    Docstring for genrate_email
    
    :param name: a list containing the names of a person
    :type name: list
    :return: an example email using the names of the person
    :rtype: str
    """
    email = ''
    for n in name:
        email +=  n
    return email + '@example.com'

prefix = [
    'Mr.', 'Ms.', 'Mrs.', 'Miss','Dr.', 'Prof.', 'Engr.',
        'Arch.', 'Rev.', 'Fr.', 'Sr.', 'Br.', 'Rabbi', 'Imam',
         'Pastor','Gen.', 'Col.', 'Maj.', 'Capt.', 'Lt.', 'Sgt.',
        'Cpl.', 'Pvt.','Sir' , 'Dame', 'Lord', 'Lady', 'Hon.', 
        'Excellency'
        ]

def gen_female_emp()->list:
    """
    Docstring for gen_female_emp
    
    :return: list containing employee details
    :rtype: list[Any]
    """
    title = random.choice(prefix)
    first_name = fake.first_name_female()
    last_name = fake.last_name()
    middle_name = fake.first_name()
    staff_id = generate_staff_id(500)
    email = genrate_email([first_name,middle_name,last_name])
    phone = '"' + '{' + f"{fake.basic_phone_number()}" +','+   f"{fake.basic_phone_number()}" + '}' + '"' 
    birth_date = fake.date_between(start_date='-55y',end_date='-25y')
    emp_gender = 'Female'
    edu_level = random.randint(1,len(educational_level)-1)
    rank = 'null'
    address_id = 'null'
    employee_type = ''
    station_id = ''
    first_appointment_date = fake.date_between(start_date='-20y',end_date='-2y')
    date_posted = fake.date_between()
    speciality_id = ''
    religion_id = ''
    last_promotion_date = fake.date_between()
    license_num = 'QT/' + staff_id + '/' + str(first_appointment_date.year)

    return [title,first_name,last_name,middle_name,staff_id,license_num,email,phone,birth_date,emp_gender,
            edu_level,rank,address_id,employee_type,station_id,first_appointment_date,date_posted,speciality_id,religion_id,
            last_promotion_date]
    
