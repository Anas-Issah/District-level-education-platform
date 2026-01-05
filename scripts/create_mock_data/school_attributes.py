import csv, pathlib, os

"""
script that writes data to a csv file for insertion
into a district-education database

"""

path = pathlib.Path.cwd()  #parent directory

#SCHOOL LEVEL
school_lvls = [
    'Kindergarten','Primary','Junior High','Basic'
]
num = 1          
with open(os.path.join(path,'data/seeds/school_level.csv'),'w') as file:
    file_writer = csv.DictWriter(file,['id','level_name'])
    file_writer.writeheader()
    for sch_lvl in school_lvls:
        file_writer.writerow({'id':num,'level_name':sch_lvl})
        num += 1

#CIRCUIT

circuits  = [
    'A','B','C','D','ABESIM','ATRONIE'
]
num = 1          
with open(os.path.join(path,'data/seeds/circuit.csv'),'w') as file:
    file_writer = csv.DictWriter(file,['id','circuit_name'])
    file_writer.writeheader()
    for circuit in circuits:
        file_writer.writerow({'id':num,'circuit_name':circuit})
        num += 1


# SCHOOL

schools = [
    
]


def generate_school_code(num:int) -> str:
    """
    Docstring for generate_school_code
    
    :param num: a counter
    :type num: int
    :return: a string representing mock school code
    :rtype: str
    """ 
    prefix = '0A00'
    if num < 10:
        return prefix + '00' + str(num)
    elif num < 100:
        return prefix + '0' + str(num)
    else:
        return prefix + str(num)         

num = 1          
with open(os.path.join(path,'data/seeds/schools.csv'),'w') as file:
    file_writer = csv.DictWriter(file,['id','name','school_code','school_level_id'])
    file_writer.writeheader()
    for sch in schools:
        if sch['level'] == 'Kindergarten':
            id = 1
        elif sch['level'] == 'Primary':
            id = 2
        elif sch['level'] == 'Junior High':
            id = 3
        else:
            id = 4
        file_writer.writerow({'id':num,'name':sch['school'],'school_code':generate_school_code(num),'school_level_id':id})
        num += 1


