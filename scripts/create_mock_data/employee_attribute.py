import csv, os, pathlib

"""
script that writes data to a csv file for insertion
into a district-education database

"""

path = pathlib.Path.cwd()   #parent path directory

#EMPLOYEE TYPE
employee_type = [
    'Teaching','Non-Teaching'
]

num = 1

with open(os.path.join(path,'data/seeds/employee_type.csv'),'w') as file:
    file_writer = csv.DictWriter(file,['id','type'])
    file_writer.writeheader()
    for em_type in employee_type:
        file_writer.writerow({'id':num,'type':em_type})
        num += 1

#RANK

ranks = [
    'Director General', 'Deputy Director General', 'Director I','Director II',
    'Deputy Director','Assisstant Director','Principal Superintendent',
    'Senior Superintendent I','Senior Superintendent II','Superintedent I',
    'Superintendent II','Pupil Teacher','Chief Accountant','Chief Accountant II',
    'Deputy Chief Accountant','Deputy Chief Accountant II','Principal Accountant (Chartered)',
    'Principal Accountant (Unit Head)','Principal Accountant (Basic Grade)','Senior Accountant',
    'Accountant','Accountant Assistant','Chief Admin Officer','Chief Admin Officer II',
    'Deputy Chief Admin Officer','Deputy Chief Admin Officer II','Principal Admin Officer (Chartered)',
    'Principal Admin Officer (Unit Head)','Principal Admin Officer (Basic Grade)',
    'Senior Admin Officer','Administrative Officer','Assistant Admin Officer','Senior Clerk',
    'Clerk Grade I','Clerk Grade II',
    "Chief Internal Auditor","Chief Internal Auditor II","Deputy Chief Auditor",
    "Deputy Chief Auditor II","Principal Internal Auditor (Chartered)",
    "Principal Internal Auditor (Unit Head)","Principal Internal Auditor (Basic Grade)",
    "Senior Internal Auditor","Internal Auditor","Assistant Internal Auditor",
    "Internal Audit Assistant Grade I","Internal Audit Assistant Grade II",
    "Internal Audit Assistant Grade III","Chief Domestic Bursar",
    "Deputy Chief Domestic Bursar","Principal Domestic Bursar","Senior Domestic Bursar",
    "Domestic Bursar","Assistant Domestic Bursar","Senior Matron","Matron",
    "Chief Cook","Cook","Assistant Cook","Head Steward","Steward","Head Laundry Man",
    "Laundry Man","Head Pantry Hand","Pantry Hand","Senior House Mother",
    "House Mother","Chief Librarian","Deputy Chief Librarian","Principal Librarian",
    "Senior Librarian","Librarian","Assistant Librarian","Senior Library Assistant",
    "Library Assistant","Junior Library Assistant","Chief Laboratory Technician",
    "Deputy Chief Lab Technician","Principal Lab Technician","Senior Lab Technician",
    "Laboratory Technician","Assistant Lab Technician","Senior Lab Assistant",
    "Laboratory Assistant Grade I","Laboratory Assistant Grade II"
]

num = 1
with open(os.path.join(path,'data/seeds/employees_ranks.csv'),'w') as file:
    file_writer = csv.DictWriter(file,['id','rank_name'])
    file_writer.writeheader()
    for rank  in ranks:
        file_writer.writerow({'id':num,'rank_name':rank})
        num += 1
    
    
#EDUCATIONAL LEVEL

educational_level = [
    'Phd','Masters','Degree','Diploma','Senior High School','Junior High School'
]

num = 1 

with open(os.path.join(path,'data/seeds/educational_level.csv'),'w') as file:
    file_writer = csv.DictWriter(file,['id','level'])
    file_writer.writeheader()
    for level in educational_level:
        file_writer.writerow({'id':num,'level':level})
        num += 1

#SPECIALITY

specialities =[
    'English Language','Mathematics','Integrated Science','Social Studies','Computing',
    'Career Technology','Creative Arts','Asante Twi','French','Religious And Moral Ed.',
    'Early Grade Education','Primary Education',

]

num = 1 

with open(os.path.join(path,'data/seeds/speciality.csv'),'w') as file:
    file_writer = csv.DictWriter(file,['id','speciality_name'])
    file_writer.writeheader()
    for speciality in specialities:
        file_writer.writerow({'id':num,'speciality_name':speciality})
        num += 1

#RELIGION

religions = [
    'Christianity','Islam','Traditional','Other'
]

num = 1 

with open(os.path.join(path,'data/seeds/religion.csv'),'w') as file:
    file_writer = csv.DictWriter(file,['id','religion_name'])
    file_writer.writeheader()
    for religion in religions:
        file_writer.writerow({'id':num,'religion_name':religion})
        num += 1

#STATION

stations = [

]


