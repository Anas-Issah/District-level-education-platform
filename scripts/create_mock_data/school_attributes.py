import csv, pathlib, os

"""
script that writes data to a csv file for insertion
into a district-education database

"""


def write_school_lvls():
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


def write_circuits():
    path = pathlib.Path.cwd()  #parent directory
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

def get_circuit_ids():
    path = pathlib.Path.cwd()  #parent directory
    with open(os.path.join(path,'data/seeds/circuit.csv'),'r') as file:
        file_reader = csv.DictReader(file,delimiter=',')
        return [id['id'] for id in file_reader]
        

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
             
def write_kg_schools(kg_schools,c_id):
    path = pathlib.Path.cwd()  #parent directory

    num = 1          
    with open(os.path.join(path,'data/seeds/schools.csv'),'a') as file:
        file_writer = csv.DictWriter(file,['id','name','school_code','school_level_id'])
        file_writer.writeheader()
        for sch in kg_schools:
            file_writer.writerow({'id':num,'name':sch['school'],'school_code':generate_school_code(num),
            'school_level_id':1,'circuit_id':c_id})
            num += 1

def write_primary_schools(primary_schools,c_id):
    path = pathlib.Path.cwd()  #parent directory

    num = 1          
    with open(os.path.join(path,'data/seeds/schools.csv'),'a') as file:
        file_writer = csv.DictWriter(file,['id','name','school_code','school_level_id'])
        file_writer.writeheader()
        for sch in primary_schools:
            file_writer.writerow({'id':num,'name':sch['school'],'school_code':generate_school_code(num),
            'school_level_id':2,'circuit_id':c_id})
            num += 1

def write_jhs_schools(jhs_schools,c_id):
    path = pathlib.Path.cwd()  #parent directory

    num = 1          
    with open(os.path.join(path,'data/seeds/schools.csv'),'a') as file:
        file_writer = csv.DictWriter(file,['id','name','school_code','school_level_id'])
        file_writer.writeheader()
        for sch in jhs_schools:
            file_writer.writerow({'id':num,'name':sch['school'],'school_code':generate_school_code(num),
            'school_level_id':3,'circuit_id':c_id})
            num += 1

def write_basic_schools(basic_schools,c_id):
    path = pathlib.Path.cwd()  #parent directory

    num = 1          
    with open(os.path.join(path,'data/seeds/schools.csv'),'a') as file:
        file_writer = csv.DictWriter(file,['id','name','school_code','school_level_id'])
        file_writer.writeheader()
        for sch in basic_schools:
            file_writer.writerow({'id':num,'name':sch['school'],'school_code':generate_school_code(num),
            'school_level_id':4,'circuit_id':c_id})
            num += 1

def get_schl_id_lvl():

    path = pathlib.Path.cwd()  #parent directory
    # read schools file
    with open(os.path.join(path,'data/seeds/school.csv'),'r') as file:
        file_reader = csv.DictReader(file,delimiter=',')
        return [{'id' :int(i['id']),'school_lvl':int(i['school_level_id'])}for i in file_reader]    #store school id and lvl in a list
