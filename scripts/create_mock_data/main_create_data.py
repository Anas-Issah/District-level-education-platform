import os, pathlib, csv,random
import student, guardian, parent, address,school_attributes

path = pathlib.Path.cwd()  #parent directory

# SCHOOL

kindergarten_schools = [
    # Kindergartens
    "Little Stars Kindergarten","Happy Kids Kindergarten","Sunshine Kindergarten",
    "Bright Beginnings Kindergarten","Rainbow Kids KG","Tiny Steps Kindergarten",
    "Future Stars Kindergarten","Smart Kids KG","Play & Learn Kindergarten",
    "Rising Tots Kindergarten","Golden Apple Kindergarten","Caring Hearts Kindergarten",
    "Young Minds Kindergarten","Early Bloom Kindergarten"]

primary_schools= [
    "Greenfield Primary School","Oakridge Primary School","Unity Primary School",
    "Golden Crest Primary School","Riverside Primary School","Hilltop Primary School",
    "Bright Future Primary School","Heritage Primary School","Maple Leaf Primary School",
    "Crown Heights Primary School","Liberty Primary School","Wisdom Tree Primary School",
    "Progress Primary School","Harmony Primary School"
]

basic_schools = [
    "Beacon Hill Basic School","Vision Point Basic School","Noble Path Basic School",
    "True Light Basic School","Starbridge Basic School","Millennium Basic School",
    "Sunrise Basic School","Pioneer Basic School","Royal Scholars Basic School",
    "Knowledge Gate Basic School","Westview Basic School","Eastwood Basic School",
    "Northstar Basic School","Southgate Basic School",
]

junior_high_schools = [
    # Junior High School
    "Victory Junior High School","Excel Junior High School","Future Leaders Junior High",
    "Summit Peak Junior High School","Apex Junior High School","Elite Scholars Junior High",
    "Legacy Junior High School","Inspire Minds Junior High","Global Reach Junior High School",
    "Horizon View Junior High","Galaxy Junior High School","Phoenix Rise Junior High",
    "Alpha Prime Junior High","Omega Scholars Junior High"
]

#write schools to file
for sch in kindergarten_schools:
    school_attributes.write_kg_schools(sch)
for sch in primary_schools:
    school_attributes.write_primary_schools(sch)
for sch in junior_high_schools:
    school_attributes.write_jhs_schools(sch)
for sch in basic_schools:
    school_attributes.write_basic_schools(sch)
    
school_attr = school_attributes.get_schl_id_lvl()

#create school population 
for school  in school_attr:
    #kg students
    if school['school_lvl'] == 1:
        student.create_kg_students(school)
    #lower and upper primary
    elif school['school_lvl'] == 2:
        for l in range(3,9):
            student.create_school_students(school,l)
    #junior high
    elif school['school_lvl'] == 3:
        for l in range(9,12):
            student.create_school_students(school,l)
    #lower primary to junior high
    else:
        for l in range(3,12):
            student.create_school_students(school,l)
 
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



