import csv, pathlib,os
from random import randint
from student import get_students
import academic_attributes


def create_scores():
    students = get_students()
    kg_subjets = academic_attributes.kg_subjects
    lower_primary_subjects = academic_attributes.lower_primary_subjects
    upper_primary_subjects = academic_attributes.upper_primary_subjects
    jhs_subjects = academic_attributes.jhs_subjects
    subjects = academic_attributes.all_subjects()
    academic_attributes.write_subjects(subjects.values(),'subject')
    ids_subjects = academic_attributes.get_subject_id(subjects)



    scores = []
    academic_year1 = 2025
    academic_year2 = 2026
    n = 0



    for student in students:
        if int(student['student_level_id']) == 1:
            for t in range(1,4):
                for sub in kg_subjets:
                    n +=1                     
                    stu_score = [n,student['id'],academic_attributes.get_academic_year_id('2024/2025'),
                                t,t,ids_subjects[sub],randint(30,100)]
                    scores.append(stu_score)
                   
                
                    

         
            
        elif int(student['student_level_id']) == 2:
            for i in range(2): # academic years
                k = 1
                for t in range(1,4):      
                    for sub in kg_subjets:
                        academic_year = str(academic_year1 - k) + '/' + str(academic_year2 - k)
                        stu_score = [n,student['id'],academic_attributes.get_academic_year_id(academic_year),
                                    t,t,ids_subjects[sub],randint(30,100)]
                        n += 1
                        scores.append(stu_score)
                k -= 1

        elif int(student['student_level_id']) == 3:
            for i in range(1): # academic years
                for t in range(1,4):      
                    for sub in lower_primary_subjects:
                        stu_score = [n,student['id'],academic_attributes.get_academic_year_id('2024/2025'),
                                    t,t,ids_subjects[sub],randint(30,100)]
                        n += 1
                        scores.append(stu_score)

        elif int(student['student_level_id']) == 4:
            for i in range(2): # academic years
                k = 1
                for t in range(1,4):      
                    for sub in lower_primary_subjects:
                        academic_year = str(academic_year1 - k) + '/' + str(academic_year2 - k)
                        stu_score = [n,student['id'],academic_attributes.get_academic_year_id(academic_year),
                                    t,t,ids_subjects[sub],randint(30,100)]
                        n += 1
                        scores.append(stu_score)
                k -= 1

        elif int(student['student_level_id']) == 5:
            for i in range(3): # academic years
                k = 2
                for t in range(1,4):      
                    for sub in lower_primary_subjects:
                        academic_year = str(academic_year1 - k) + '/' + str(academic_year2 - k)
                        stu_score = [n,student['id'],academic_attributes.get_academic_year_id(academic_year),
                                    t,t,ids_subjects[sub],randint(30,100)]
                        n += 1
                        scores.append(stu_score)
                k -= 1

        elif int(student['student_level_id']) == 6:
            for i in range(4): # academic years
                k = 3
                for t in range(1,4): 
                    if k > 0:    
                        for sub in lower_primary_subjects:
                            academic_year = str(academic_year1 - k) + '/' + str(academic_year2 - k)
                            stu_score = [n,student['id'],academic_attributes.get_academic_year_id(academic_year),
                                        t,t,ids_subjects[sub],randint(30,100)]
                            n += 1
                            scores.append(stu_score)
                    else:
                        for sub in upper_primary_subjects:
                            academic_year = str(academic_year1 - k) + '/' + str(academic_year2 - k)
                            stu_score = [n,student['id'],academic_attributes.get_academic_year_id(academic_year),
                                        t,t,ids_subjects[sub],randint(30,100)]
                            n += 1
                            scores.append(stu_score)



                k -= 1

        elif int(student['student_level_id']) == 7:
            for i in range(5): # academic years
                k = 4
                for t in range(1,4):      
                    if k > 1:    
                        for sub in upper_primary_subjects:
                            academic_year = str(academic_year1 - k) + '/' + str(academic_year2 - k)
                            stu_score = [n,student['id'],academic_attributes.get_academic_year_id(academic_year),
                                        t,t,ids_subjects[sub],randint(30,100)]
                            n += 1
                            scores.append(stu_score)

                    else:
                        for sub in upper_primary_subjects:
                            academic_year = str(academic_year1 - k) + '/' + str(academic_year2 - k)
                            stu_score = [n,student['id'],academic_attributes.get_academic_year_id(academic_year),
                                        t,t,ids_subjects[sub],randint(30,100)]
                            n += 1
                            scores.append(stu_score)

                k -= 1

        elif int(student['student_level_id']) == 8:
            for i in range(6): # academic years
                k = 5
                for t in range(1,4):      
                    if k > 2:    
                        for sub in upper_primary_subjects:
                            academic_year = str(academic_year1 - k) + '/' + str(academic_year2 - k)
                            stu_score = [n,student['id'],academic_attributes.get_academic_year_id(academic_year),
                                        t,t,ids_subjects[sub],randint(30,100)]
                            n += 1
                            scores.append(stu_score)

                    else:
                        for sub in upper_primary_subjects:
                            academic_year = str(academic_year1 - k) + '/' + str(academic_year2 - k)
                            stu_score = [n,student['id'],academic_attributes.get_academic_year_id(academic_year),
                                        t,t,ids_subjects[sub],randint(30,100)]
                            n += 1
                            scores.append(stu_score)

                            
                k -= 1
        #start here  
        elif int(student['student_level_id']) == 9:
            for i in range(1): # academic years
                for t in range(1,4):      
                    for sub in jhs_subjects:
                        academic_year = str(academic_year1) + '/' + str(academic_year2)
                        stu_score = [n,student['id'],academic_attributes.get_academic_year_id(academic_year),
                                    t,t,ids_subjects[sub],randint(30,100)]
                        n += 1
                        scores.append(stu_score)
                

        elif int(student['student_level_id']) == 10:
            for i in range(2): # academic years
                k = 2
                for t in range(1,4):      
                    for sub in jhs_subjects:
                        academic_year = str(academic_year1 - k) + '/' + str(academic_year2 - k)
                        stu_score = [n,student['id'],academic_attributes.get_academic_year_id(academic_year),
                                    t,t,ids_subjects[sub],randint(30,100)]
                        n += 1
                        scores.append(stu_score)
                k -= 1

        else:
            for i in range(2): # for academic years
                k = 2
                for t in range(1,4):      
                    for sub in jhs_subjects:
                        academic_year = str(academic_year1 - k) + '/' + str(academic_year2 - k)
                        stu_score = [n,student['id'],academic_attributes.get_academic_year_id(academic_year),
                                    t,t,ids_subjects[sub],randint(30,100)]
                        n += 1
                        scores.append(stu_score)
                        

                k -= 1
            for i in range(1):
                for t in range(4,7):      
                    for sub in jhs_subjects:
                        academic_year = str(academic_year1 - k) + '/' + str(academic_year2 - k)
                        stu_score = [n,student['id'],academic_attributes.get_academic_year_id(academic_year),
                                    t -3,t,ids_subjects[sub],randint(30,100)]
                        n += 1
                        scores.append(stu_score)
                        

                
        if len(scores) >= 1000:
            write_scores(scores)
            scores.clear()
    
def header_writer():
    path = os.path.join(pathlib.Path.cwd(),'data/seeds/score.csv')
    if pathlib.Path(path).exists() == False:
        with open(os.path.join(pathlib.Path.cwd(),'data/seeds/score.csv'),'w') as file:
            file_writer = csv.DictWriter(file,['id','student_id','academic_year_id','academic_term_id','exam_id','subject_id','mark'])
            file_writer.writeheader()


def write_scores(stud_scores:list):
    
    header_writer()
    with open(os.path.join(pathlib.Path.cwd(),'data/seeds/score.csv'),'a') as file:
        file_writer = csv.writer(file)
        for s in stud_scores:
            file_writer.writerow(s)


