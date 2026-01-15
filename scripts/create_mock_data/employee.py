import csv, pathlib, os,sys,random
from uuid6 import uuid7
from faker import Faker
from employee_attribute import ranks, specialities, religions, educational_level



"""
script that writes data to a csv file for insertion
into a district-education database

"""

path = pathlib.Path.cwd()  #parent di


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
    
 
def generate_email(name:list)->str:
    """
    Docstring for generate_email
    
    :param name: a list containing the names of a person
    :type name: list
    :return: an example email using the names of the person
    :rtype: str
    """
    email = ''
    for n in name:
        email +=  n
    return email + '@example.com'


def gen_female_emp()->list:
    """
    Docstring for gen_female_emp
    
    :return: list containing employee details
    :rtype: list[Any]
    """
    fake = Faker("en_US")

    id = uuid7()
    title = random.randint(1,22)
    first_name = fake.first_name_female()
    last_name = fake.last_name()
    staff_id = generate_staff_id(500)
    phone = '"' + '{' + f"{fake.basic_phone_number()}" +','+   f"{fake.basic_phone_number()}" + '}' + '"' 
    birth_date = fake.date_between(start_date='-55y',end_date='-25y')
    emp_gender = 'Female'
    edu_level = random.randint(1,len(educational_level)-1)
    rank = random.randint(3,12)
    address_id = 'null'
    employee_type = 1
    station_id = ''
    first_appointment_date = fake.date_between(start_date='-20y',end_date='-2y')
    date_posted = fake.date_between()
    speciality_id = random.randint(1,len(specialities))
    religion_id = random.randint(1,3)
    last_promotion_date = fake.date_between()
    license_num = 'QT/' + staff_id + '/' + str(first_appointment_date.year)

    # get a middle name or not
    dec = random.randint(1,2)     
    if dec == 1:
        other_name = fake.first_name()
        email = generate_email([first_name,other_name,last_name])
        return [id,title,first_name,last_name,other_name,staff_id,license_num,email,phone,birth_date,emp_gender,
            edu_level,rank,address_id,employee_type,station_id,first_appointment_date,date_posted,speciality_id,religion_id,
            last_promotion_date]
    else:
        other_name = 'N/A'
        email = generate_email([first_name,last_name])
        return [id,title,first_name,last_name,other_name,staff_id,license_num,email,phone,birth_date,emp_gender,
            edu_level,rank,address_id,employee_type,station_id,first_appointment_date,date_posted,speciality_id,religion_id,
            last_promotion_date]
    
def gen_male_emp()->list:
    """
    Docstring for gen_male_emp
    
    :return: list containing employee details
    :rtype: list[Any]
    """
    fake = Faker("en_US")

    id = uuid7()
    title = random.randint(8,29)
    first_name = fake.first_name_male()
    last_name = fake.last_name()
    staff_id = generate_staff_id(500)
    phone = '"' + '{' + f"{fake.basic_phone_number()}" +','+   f"{fake.basic_phone_number()}" + '}' + '"' 
    birth_date = fake.date_between(start_date='-55y',end_date='-25y')
    emp_gender = 'Male'
    edu_level = random.randint(1,len(educational_level)-1)
    rank = random.randint(3,12)
    address_id = 'null'
    employee_type = 1
    station_id = ''
    first_appointment_date = fake.date_between(start_date='-20y',end_date='-2y')
    date_posted = fake.date_between()
    speciality_id = random.randint(1,len(specialities))
    religion_id = random.randint(1,3)
    last_promotion_date = (fake.date_between())
    license_num = 'QT/' + staff_id + '/' + str(first_appointment_date.year)
    date_created = date_posted

    # get a middle name or not
    dec = random.randint(1,2)     
    if dec == 1:
        other_name = fake.first_name()
        email = generate_email([first_name,other_name,last_name])
        return [id,title,first_name,last_name,other_name,staff_id,license_num,email,phone,birth_date,emp_gender,
            edu_level,rank,address_id,employee_type,station_id,first_appointment_date,date_posted,speciality_id,religion_id,
            last_promotion_date,date_created]
    else:
        other_name = 'N/A'
        email = generate_email([first_name,last_name])
        return [id,title,first_name,last_name,other_name,staff_id,license_num,email,phone,birth_date,emp_gender,
            edu_level,rank,address_id,employee_type,station_id,first_appointment_date,date_posted,speciality_id,religion_id,
            last_promotion_date,date_created]
   

def write_employee(employees:list):

    with open(os.path.join(path,'data/seeds/employess.csv'),'w') as file:
        file_writer = csv.DictWriter(file,['id','first_name','last_name','other_name','staff_id','license_num',
                                        'email','phone','birth_date','gender','education_level','rank_id',
                                        'address_id','employee_type','station_id','first_appointment_date',
                                        'date_posted','speciality','last_promotion_date','date_created'])
        file_writer.writeheader()

        for employee in employees:
            file_writer.writerow({'id':employee[0],'first_name':employee[1],'last_name':employee[2],
                                'other_name':employee[3],'staff_id':employee[4],'license_num':employee[5],
                                'email':employee[6],'phone':employee[7],'birth_date':employee[8],
                                'gender':employee[9],'education_level':employee[10],'rank_id':employee[11],
                                'gender':employee[12],'education_level':employee[13],'rank_id':employee[14],
                                'address_id':employee[15],'employee_type':employee[16],'station_id':employee[17],
                                'first_appointment_date':employee[18],'date_posted':employee[19],
                                'speciality':employee[20],'last_promotion_date':employee[21],'date_created':employee[22]})


# CREATE AND WRITE EMPLOYEES


