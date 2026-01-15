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



#write a guardian for each student
guardian.write_stu_guardian_rela()
relationships = guardian.get_stu_guardian_rela()
students = student.get_students()
parents = parent.get_parents()

for student in students:
    guard_dec = random.randint(1,5)   # decide if guardian is the parent or not
    if guard_dec > 4:
        gender_dec = random.randint(1,2)
        if gender_dec ==1:
            num_addres = len(address.get_address())
            addrs = address.create_address()
            
            # stu_guardian = guardian.create_guardian_female()
