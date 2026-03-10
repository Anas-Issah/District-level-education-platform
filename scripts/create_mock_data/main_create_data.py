import os, pathlib, csv,random
import student, guardian, parent, address,school_attributes,scores,employee

path = pathlib.Path.cwd()  #parent directory


#CIRCUITS
circuits = ['A','B','C','D','E','F']


# SCHOOLS
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

# school_attributes.write_circuits(circuits=circuits) # write circuits
# circuits_ids = school_attributes.get_circuit_ids()   #read circuits_ids

# print(len(junior_high_schools) + len(kindergarten_schools) + len(primary_schools) + len(basic_schools))   


# #write schools to file
# circuit_num_kg = school_attributes.dist_schls(circuits_ids,len(kindergarten_schools))
# circuit_num_primary = school_attributes.dist_schls(circuits_ids,len(primary_schools))
# circuit_num_jhs = school_attributes.dist_schls(circuits_ids,len(junior_high_schools))
# circuit_num_basic = school_attributes.dist_schls(circuits_ids,len(basic_schools))


# for circuit in circuits_ids:
#     school_attributes.header_writer()
#     num_schls = circuit_num_kg[circuit]
#     kg_schls = []
#     for n in range(num_schls):
#         kg_schls.append(kindergarten_schools.pop(0))        
#     school_attributes.write_kg_schools(kg_schls,int(circuit))

#     num_schls = circuit_num_primary[circuit]
#     pri_schls = []
#     for n in range(num_schls):
#         pri_schls.append(primary_schools.pop(0))
#     school_attributes.write_basic_schools(pri_schls,int(circuit))   
  
#     num_schls = circuit_num_jhs[circuit]
#     jhs_schls = []
#     for n in range(num_schls):
#         jhs_schls.append(junior_high_schools.pop(0))
#     school_attributes.write_jhs_schools(jhs_schls,int(circuit))  

#     num_schls = circuit_num_basic[circuit]
#     basic_schls = []
#     for n in range(num_schls):
#         basic_schls.append(basic_schools.pop(0))
#     school_attributes.write_basic_schools(basic_schls,int(circuit))

# school_attr = school_attributes.get_schl_id_lvl()   #get schol level ids

# #create school population 
# for school  in school_attr:
#     #kg students
#     if school['school_lvl'] == 1:
#         student.create_kg_students(school)
#     #lower and upper primary
#     elif school['school_lvl'] == 2:
#         for l in range(3,9):
#             student.create_school_students(school,l)
#     #junior high
#     elif school['school_lvl'] == 3:
#         for l in range(9,12):
#             student.create_school_students(school,l)
#     #lower primary to junior high
#     else:
#         for l in range(3,12):
#             student.create_school_students(school,l)
 
#write a guardian for each student
# guardian.write_stu_guardian_rela()
# students = student.get_students()
# parents = parent.get_parents()

# #separate male and female relationship
# male = ['Uncle']
# female = ['Aunt']
# parent_guardian = ['Mother','Father']

# relationships = guardian.get_stu_guardian_rela()
# female_guardian_id = [rela['id'] for rela in relationships if rela['relationship'] not in (male + parent_guardian)]
# parent_guardian_id = [rela['id'] for rela in relationships if rela['relationship'] in parent_guardian]
# male_guardian_id = [rela['id'] for rela in relationships if rela['relationship'] not in (female + parent_guardian)]



# stu_guardians = []

# for student in students:
#     guard_dec = random.randint(1,5)   # decide if guardian is the parent or not
#     gender_dec = random.randint(1,2)     #decide gender
#     print(f'Creating a guardian for {student['first_name']} {student['last_name']}')
#     if guard_dec > 4:               #guardian is not a parent
#         if gender_dec ==1:
#             address.write_single_addres()
#             num_addres = len(address.get_address())
#             stu_guardian = guardian.create_guardian_female(int(random.choice(female_guardian_id)),num_addres,student['id'])
#             stu_guardians.append(stu_guardian)
#         else:
#             address.write_single_addres()
#             num_addres = len(address.get_address())
#             stu_guardian = guardian.create_guardian_male(int(random.choice(male_guardian_id)),num_addres,student['id'])
#             stu_guardians.append(stu_guardian)


#     else:
#         if gender_dec == 1:
#             for stu_parent in parents:
#                 if stu_parent['student_id'] == student['id'] and stu_parent['relationship'] == 'Mother':
#                     stu_guardian = guardian.create_parent_guardian(stu_parent)
#                     stu_guardians.append(stu_guardian)
#                     break
#         else:
#             for stu_parent in parents:
#                 if stu_parent['student_id'] == student['id'] and stu_parent['relationship'] == 'Father':
#                     stu_guardian = guardian.create_parent_guardian(stu_parent)
#                     stu_guardians.append(stu_guardian)
#                     break

# guardian.write_guardian(stu_guardians) #write guardians to file
# scores.create_scores()  # create students scores file

#create teachers
teachers = []
for k_school in kindergarten_schools:
    schl_attr = school_attributes.get_schl_id_lvl()
    for attr in schl_attr:
        if attr['school_name'] == k_school:
            schl_id = attr['id']
    for _ in range(2):
        for _ in range(2):
            teachers.append(employee.gen_female_emp(schl_id))
    employee.write_employee(teachers)
    teachers.clear()

for p_school in primary_schools:
    for attr in schl_attr:
        if attr['school_name'] == p_school:
            schl_id = attr["id"]
    for _ in range(6):
        gender = random.randint(1,2)
        if gender == 1:
            teachers.append(employee.gen_female_emp(schl_id))
        else:
            teachers.append(employee.gen_male_emp(schl_id))
    employee.write_employee(teachers)
    teachers.clear()

for b_school in basic_schools:
    for attr in schl_attr:
        if attr['school_name'] == p_school:
            schl_id = attr["id"]
    for _ in range(15):
        gender = random.randint(1,2)
        if gender == 1:
            teachers.append(employee.gen_female_emp(schl_id))
        else:
            teachers.append(employee.gen_male_emp(schl_id))
    employee.write_employee(teachers)
    teachers.clear()

for jhs_school in junior_high_schools:
    for attr in schl_attr:
        if attr['school_name'] == p_school:
            schl_id = attr["id"]
    for _ in range(9):
        gender = random.randint(1,2)
        if gender == 1:
            teachers.append(employee.gen_female_emp(schl_id))
        else:
            teachers.append(employee.gen_male_emp(schl_id))
    employee.write_employee(teachers)
    teachers.clear()