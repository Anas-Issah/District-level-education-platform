import os, pathlib, csv,random
import student, guardian, parent, address



path = pathlib.Path.cwd()  #parent directory
 
# read schools file
with open(os.path.join(path,'data/seeds/school.csv'),'r') as file:
    file_reader = csv.DictReader(file,delimiter=',')
    school_attr = [{'id' :int(i['id']),'school_lvl':int(i['school_level_id'])}for i in file_reader]    #store school id's in a list
 
for school  in school_attr:
    if school['school_lvl'] == 1:
        student.create_kg_students(school)
# 
 
 
#write a guardian for each student
guardian.write_stu_guardian_rela()
students = student.get_students()
parents = parent.get_parents()

#separate male and female relationship
male = ['Uncle']
female = ['Aunt']
parent_guardian = ['Mother','Father']

relationships = guardian.get_stu_guardian_rela()
female_guardian_id = [rela['id'] for rela in relationships if rela['relationship'] not in male + parent_guardian]
parent_guardian_id = [rela['id'] for rela in relationships if rela['relationship'] in parent_guardian]
male_guardian_id = [rela['id'] for rela in relationships if rela['relationship'] not in (female + parent_guardian)]

for rela in relationships:
    if rela['relationship'] not in (male and parent_guardian):
        female_guardian_id.append(rela['id'])
    if rela['relationship'] not in (female and parent_guardian):
        male_guardian_id.append(rela['id'])

stu_guardians = []

for student in students:
    guard_dec = random.randint(1,5)   # decide if guardian is the parent or not
    gender_dec = random.randint(1,2)     #decide gender
    if guard_dec > 4:               #guardian is not a parent
        if gender_dec ==1:
            address.write_single_addres()
            num_addres = len(address.get_address())
            addrs = address.create_address()
            stu_guardian = guardian.create_guardian_female(int(random.choice(female_guardian_id)),num_addres,student['id'])
            stu_guardians.append(stu_guardian)
        else:
            address.write_single_addres()
            num_addres = len(address.get_address())
            addrs = address.create_address()
            stu_guardian = guardian.create_guardian_male(int(random.choice(male_guardian_id)),num_addres,student['id'])
            stu_guardians.append(stu_guardian)


    else:
        for stu_parent in parents:
            if stu_parent['student_id'] == student['id'] and stu_parent['relationship'] == 'Mother':
                stu_guardian = guardian.create_parent_guardian(stu_parent)
                stu_guardians.append(stu_guardian)
                break

guardian.write_guardian(stu_guardians) #write guardians to file


