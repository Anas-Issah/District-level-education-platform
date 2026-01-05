
BEGIN;
--=======================================
--CREATE UUID-OSSP EXTENSION
--=======================================

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";


--=======================================
--GENDER CUSTOM TYPE
--=======================================
CREATE TYPE gender_type AS ENUM ('Male','Female');

--=======================================
--STATUS CUSTOM TYPE
--=======================================
CREATE TYPE alive_status_type AS ENUM ('Alive', 'Deceased');

--=======================================
--NAME PREFIX CUSTOM TYPE
--=======================================
CREATE TYPE name_prefix AS ENUM ('Mr.', 'Ms.', 'Mrs.', 'Miss','Dr.', 'Prof.', 'Engr.',
                                 'Arch.', 'Rev.', 'Fr.', 'Sr.', 'Br.', 'Rabbi', 'Imam',
                                 'Pastor','Gen.', 'Col.', 'Maj.', 'Capt.', 'Lt.', 'Sgt.',
                                  'Cpl.', 'Pvt.','Sir' , 'Dame', 'Lord', 'Lady', 'Hon.', 
                                  'Excellency');

--=======================================
--GUARDIAN STUDENT RELATIONSHIP CUSTOM TYPE
--=======================================

CREATE TYPE guardian_student_relationship_type AS ENUM(
    'Mother', 'Father', 'Stepparent','Grandparent', 
    'Aunt', 'Uncle', 'Cousin','Sibling','Legal Guardian', 
    'Foster Parent', 'Host Parent', 'Social Worker',
    'Family Friend','Other'
);


COMMENT ON TABLE employee IS 'Employee details like name, address, station, etc';


--=======================================
--ADDRESS
--=======================================

CREATE TABLE IF NOT EXISTS address(
    id BIGINT GENERATED ALWAYS  AS IDENTITY PRIMARY KEY,
    gh_post_gps VARCHAR(20) NOT NULL,
    area_id INT FOREIGN KEY NOT NULL,
);

COMMENT ON TABLE address IS 'Details of employee''s address';


--=======================================
--AREA
--=======================================

CREATE TABLE IF NOT EXIST area(
    id SMALLINT GENERATED ALWAYS  AS IDENTITY PRIMARY KEY,
    area_name VARCHAR(80) NOT NULL,
    CONSTRAINT uq_area_name UNIQUE (area_name)
);

COMMENT ON TABLE area IS 'Geographical areas with the district';


--=======================================
--EMPLOYEE TYPE
--=======================================

CREATE TABLE IF NOT EXISTS employee_type(
    id SMALLINT GENERATED ALWAYS  AS IDENTITY PRIMARY KEY;
    type VARCHAR(50) NOT NULL,
    CONSTRAINT uq_title UNIQUE (title)
);

COMMENT ON TABLE employee_type IS 'Employee''s job title';


--=======================================
--STATION
--=======================================

CREATE TABLE IF NOT EXITST  station(
    id SMALLINT GENERATED ALWAYS  AS IDENTITY PRIMARY KEY,
    station_name VARCHAR(70) NOT NULL,
    CONSTRAINT uq_station_name UNIQUE (station_name)
);

COMMENT ON TABLE station IS 'An employee''s work satatioin';


--=======================================
--CIRCUIT
--=======================================

CREATE TABLE IF NOT EXISTS circuit(
    id SMALLINT GENERATED ALWAYS  AS IDENTITY PRIMARY KEY,
    circuit_name VARCHAR(50) NOT NULL,
    CONSTRAINT uq_circuit_name UNIQUE (circuit_name)
);

COMMENT ON TABLE circuit IS 'Circuits within the district';


--=======================================
--RELIGION
--=======================================

CREATE TABLE IF NOT EXISTS religion(
    id SMALLINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    religion_name VARCHAR(50)
);

COMMENT ON TABLE religion IS 'Main religions in the country'


--=======================================
--RANK
--=======================================

CREATE TABLE IF NOT EXIST employee_rank(
    id SMALLINT GENERATED ALWAYS  AS IDENTITY PRIMARY KEY,
    rank_name VARCHAR(50) NOT NULL,
    CONSTRAINT uq_rank_name UNIQUE(rank_name)
);

COMMENT ON TABLE rank IS 'Ranks within Ghana Education Service';




--=======================================
-- EDUCATION LEVEL
--=======================================

CREATE TABLE IF NOT EXIST education_level(
    id SMALLINT GENERATED ALWAYS  AS IDENTITY PRIMARY KEY,
    level VARCHAR(30) NOT NULL,
    CONSTRAINT uq_level UNIQUE (level)
);

COMMENT ON TABLE education_level IS 'Education level of employees';


--=======================================
--SPECIALITY
--=======================================

CREATE IF NOT EXISTS speciality(
    id SMALLINT GENERATED ALWAYS  AS IDENTITY PRIMARY KEY,
    speciality_name VARCHAR(50) NOT NULL,
    CONSTRAINT uq_speciality UNIQUE (speciality_name)
);

COMMENT ON TABLE speciality IS 'Teacher level or subject speciality';


--=======================================
--EMPLOYEE
--=======================================

CREATE TABLE IF NOT EXISTS employee(
    id UUID PRIMARY KEY DEFAULT uuid_generate_v7(),
    prefix name_prefix NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50)  NOT NULL,
    other_name VARCHAR(70) NULL,
    staff_id VARCHAR(20)  NOT NULL INDEX,
    liscence_number VARCHAR(20) INDEX,
    email VARCHAR(50) NULL,
    phone1 VARCHAR(14)[]  NOT NULL,
    birth_date DATE NOT NULL,
    gender gender_type NOT NULL,
    education_level_id INT NOT NULL,
    rank_id INT NOT NULL,
    address_id INT  NOT NULL,
    employee_type_id INT  NOT NULL,
    station_id INT NOT NULL,
    first_appointment_date DATE NOT NULL,
    date_posted DATE NOT NULL,
    speciality_id INT,
    religion_id INT NOT NULL
    last_promotion_date DATE ,
    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_employee_education_level FOREIGN KEY(education_level_id) REFERENCES education_level(id),
    CONSTRAINT fk_employee_rank FOREIGN KEY(rank_id) REFERENCES employee_rank(id),
    CONSTRAINT fk_address_id FOREIGN KEY(address_id) REFERENCES address(id),
    CONSTRAINT fk_employee_type_id FOREIGN KEY(employee_type_id) REFERENCES employee_type(id),
    CONSTRAINT fk_station_id FOREIGN KEY(station_id) REFERENCES station(id),
    CONSTRAINT fk_specialiity_id FOREIGN KEY (speciality_id) REFERENCES speciality(id),
    CONSTRAINT fk_religion_id FOREIGN KEY (speciality_id) REFERENCES religion(id),
    CONSTRAINT uq_staff_id UNIQUE (staff_id),
    CONSTRAINT uq_liscence_number UNIQUE (liscence_number),
    CONSTRAINT uq_phone1 UNIQUE (phone1)


);


--=======================================
--EMPLOYEE HISTORY
--=======================================

CREATE TABLE IF NOT EXISTS employee_history(
    id BIGINT GENERATED ALWAYS  AS IDENTITY PRIMARY KEY,
    id UUID PRIMARY KEY DEFAULT uuid_generate_v7(),
    prefix name_prefix NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50)  NOT NULL,
    other_name VARCHAR(70) NULL,
    staff_id VARCHAR(20)  NOT NULL INDEX,
    liscence_number VARCHAR(20) INDEX,
    email VARCHAR(50) NULL,
    phone VARCHAR(14)[]  NOT NULL,
    birth_date DATE NOT NULL,
    gender gender_type NOT NULL,
    education_level_id INT NOT NULL,
    rank_id INT NOT NULL,
    address_id INT  NOT NULL,
    employee_type_id INT  NOT NULL,
    station_id INT NOT NULL,
    first_appointment_date DATE NOT NULL,
    date_posted DATE NOT NULL,
    speciality_id INT,
    religion_id INT NOT NULL
    last_promotion_date DATE ,
    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_employee_education_level FOREIGN KEY(education_level_id) REFERENCES education_level(id),
    CONSTRAINT fk_employee_rank FOREIGN KEY(rank_id) REFERENCES employee_rank(id),
    CONSTRAINT fk_address_id FOREIGN KEY(address_id) REFERENCES address(id),
    CONSTRAINT fk_employee_type_id FOREIGN KEY(employee_type_id) REFERENCES employee_type(id),
    CONSTRAINT fk_station_id FOREIGN KEY(station_id) REFERENCES station(id),
    CONSTRAINT fk_specialiity_id FOREIGN KEY (speciality_id) REFERENCES speciality(id),
    CONSTRAINT fk_religion_id FOREIGN KEY (speciality_id) REFERENCES religion(id),
    CONSTRAINT uq_staff_id UNIQUE (staff_id),
    CONSTRAINT uq_liscence_number UNIQUE (liscence_number),
    CONSTRAINT uq_phone1 UNIQUE (phone1)


);

COMMENT ON TABLE employee_history IS 'Table to track changes in employee data';


--=======================================
--PAST EMPLOYEE
--=======================================

CREATE TABLE IF NOT EXISTS past_employee(
    id BIGINT GENERATED ALWAYS  AS IDENTITY PRIMARY KEY,
    id UUID PRIMARY KEY DEFAULT uuid_generate_v7(),
    prefix name_prefix NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50)  NOT NULL,
    other_name VARCHAR(70) NULL,
    staff_id VARCHAR(20)  NOT NULL INDEX,
    liscence_number VARCHAR(20) INDEX,
    email VARCHAR(50) NULL,
    phone VARCHAR(14)[],
    birth_date DATE NOT NULL,
    gender gender_type NOT NULL,
    education_level_id INT NOT NULL,
    rank_id INT NOT NULL,
    address_id INT  NOT NULL,
    employee_type_id INT  NOT NULL,
    station_id INT NOT NULL,
    first_appointment_date DATE NOT NULL,
    date_posted DATE NOT NULL,
    speciality_id INT,
    religion_id INT NOT NULL
    last_promotion_date DATE ,
    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_employee_education_level FOREIGN KEY(education_level_id) REFERENCES education_level(id),
    CONSTRAINT fk_employee_rank FOREIGN KEY(rank_id) REFERENCES employee_rank(id),
    CONSTRAINT fk_address_id FOREIGN KEY(address_id) REFERENCES address(id),
    CONSTRAINT fk_employee_type_id FOREIGN KEY(employee_type_id) REFERENCES employee_type(id),
    CONSTRAINT fk_station_id FOREIGN KEY(station_id) REFERENCES station(id),
    CONSTRAINT fk_specialiity_id FOREIGN KEY (speciality_id) REFERENCES speciality(id),
    CONSTRAINT fk_religion_id FOREIGN KEY (speciality_id) REFERENCES religion(id),
    CONSTRAINT uq_staff_id UNIQUE (staff_id),
    CONSTRAINT uq_liscence_number UNIQUE (liscence_number),
    CONSTRAINT uq_phone1 UNIQUE (phone1)
);

COMMENT ON TABLE past_employee IS 'stores data of past employess';


--=======================================
--SCHOOL LEVEL
--=======================================

CREATE TABLE IF NOT EXISTS school_level(
    id SMALLINT GENERATED ALWAYS  AS IDENTITY PRIMARY KEY,
    level_name VARCHAR(20) NOT NULL,
    CONSTRAINT uq_school_level_name UNIQUE (level_name) 
);

COMMENT ON TABLE school_level IS 'The educational levels of schools';


--=======================================
--SCHOOL
--=======================================

CREATE TABLE IF NOT EXISTS school(
    id BIGINT GENERATED ALWAYS  AS IDENTITY PRIMARY KEY,
    name VARCHAR(70) NOT NULL,
    school_code VARCHAR(10) NOT NULL,
    school_level_id INT NOT NULL,
    CONSTRAINT fk_school_level_id FOREIGN KEY REFERENCES school_level(id),
    CONSTRAINT uq_school_code UNIQUE (school_code)
);

COMMENT ON TABLE school IS 'Schools in the district';


--=======================================
--STUDENT LEVEL
--=======================================

CREATE TABLE IF NOT EXIST student_level(
    id SMALLINT GENERATED ALWAYS  AS IDENTITY PRIMARY KEY,
    level_name VARCHAR,
    CONSTRAINT uq_student_level_name UNIQUE (level_name)
);

COMMENT ON TABLE student_level IS 'Student is level';


--=======================================
--STUDENT
--=======================================

CREATE TABLE IF NOT EXIST student(
    id UUID PRIMARY KEY DEFAULT uuid_generate_v7(),
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    other_name VARCHAR(70) NULL,
    school_id INT NOT NULL INDEX,
    birth_date DATE NOT NULL,
    addmission_date DATE NOT NULL INDEX,
    student_level_id INT NOT NULL INDEX,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_school_id FOREIGN KEY school(school_id)
    CONSTRAINT fk_student_level_id FOREIGN KEY student_level(id)
);

COMMENT ON TABLE student IS 'Students in the district';




--=======================================
--EXAM
--=======================================

CREATE TABLE IF NOT EXISTS exam(
    id SMALLINT GENERATED ALWAYS  AS IDENTITY PRIMARY KEY,
    exam_name VARCHAR,
    CONSTRAINT uq_exam_name UNIQUE (exam_name)
);

COMMENT ON TABLE exam IS 'Examination written in schools';


--=======================================
--SUBJECT
--=======================================

CREATE TABLE IF NOT EXISTS subject(
    id SMALLINT GENERATED ALWAYS  AS IDENTITY PRIMARY KEY,
    subject_name VARCHAR,
    CONSTRAINT uq_subject_name UNIQUE (subject_name)
);

COMMENT ON TABLE subject IS 'Subjects studied in schools';


--=======================================
--ACADEMIC YEAR
--=======================================

CREATE TABLE IF NOT EXISTS academic_year(
    id BIGINT GENERATED ALWAYS  AS IDENTITY PRIMARY KEY,
    academic_year VARCHAR(20) NOT NULL
):

COMMENT ON TABLE academic_year IS 'Academic year look-up table'

--=======================================
--ACADEMIC TERM
--=======================================

CREATE TABLE IF NOT EXISTS academic_term(
    id SMALLINT GENERATED ALWAYS  AS IDENTITY PRIMARY KEY,
    term VARCHAR(20) NOT NULL

);

COMMENT ON TABLE academic_term IS 'Academic term is an academic year'


--=======================================
--SCORE
--=======================================

CREATE TABLE IF NOT EXISTS score(
    id BIGINT GENERATED ALWAYS  AS IDENTITY PRIMARY KEY,
    student_id UUID NOT NULL,
    exam_id INT NOT NULL,
    subject_id INT NOT NULL INDEX,
    academic_year_id INT NOT NULL INDEX,
    academic_term_id INT NOT NULL INDEX,
    mark INT NOT NULL,
    CONSTRAINT fk_student_id FOREIGN KEY REFERENCES student(id),
    CONSTRAINT fk_exam_id FOREIGN KEY REFERENCES exam(id),
    CONSTRAINT fk_student_id FOREIGN KEY REFERENCES subject(id)
    CONSTRAINT fk_academic_year_id FOREIGN KEY REFERENCES academic_year(id)
    CONSTRAINT fk_acdemic_term_id FOREIGN KEY REFERENCES academic_term (id)

);

COMMENT ON TABLE score IS 'Examination scores of the student';


--=======================================
--STUDENT EVALUATION
--=======================================

CREATE TABLE IF NOT EXIST student_evaluation(
    id BIGINT GENERATED ALWAYS  AS IDENTITY PRIMARY KEY,
    student_id UUID NOT NULL,
    academic_year INT NOT NULL INDEX,
    acdemic_term INT NOT NULL INDEX,
    attendance IN NOT NULL,
    motivation_lookup_id INT NOT NULL,
    conduct_lookup_id INT NOT NULL,
    CONSTRAINT fk_student_id FOREIGN KEY REFERENCES student(id),
    CONSTRAINT fk_academic_year FOREIGN KEY REFERENCES academic_year(id),
    CONSTRAINT fk_academic_term FOREIGN KEY REFERENCES academic_term (id),
    CONSTRAINT fk_motivation_lookup_id FOREIGN KEY REFERENCES motivation_lookup (id),
    CONSTRAINT fk_conduct_lookup_id FOREIGN KEY REFERENCES conduct_lookup (id)
):

COMMENT ON TABLE student_evaluation IS 'Teacher evaluation of student';


--=======================================
--MOTIVATION LOOKUP
--=======================================

CREATE TABLE IF NOT EXISTS motivation_lookup(
    id SMALLINT GENERATED ALWAYS  AS IDENTITY PRIMARY KEY,
    lable VARCHAR(30) NOT NULL,
    score_value INT NOT NULL
);

COMMENT ON TABLE motivation_lookup IS 'Lookup table for student motivation level'


--=======================================
--MOTIVATION LOOKUP
--=======================================

CREATE TABLE IF NOT EXISTS conduct_lookup(
    id SMALLINT GENERATED ALWAYS  AS IDENTITY PRIMARY KEY,
    lable VARCHAR(30) NOT NULL,
    score_value INT NOT NULL
);

COMMENT ON TABLE conduct_lookup IS 'Lookup table for student conduct'


--=======================================
--TEACHER SUBJECT
--=======================================

CREATE TABLE IF NOT EXISTS teacher_subject(
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    employee_id UUID NOT NULL,
    subject_id INT NOT NULL INDEX,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_employee_id FOREIGN KEY REFERENCES employee(id),
    CONSTRAINT fk_subject_id FOREIGN KEY REFERENCES subject (id)
);

COMMENT ON TABLE teacher_subject IS 'Subject taught by a teacher';


--=======================================
--PARENT
--=======================================

CREATE TABLE IF NOT EXISTS parent(
    id UUID PRIMARY KEY DEFAULT uuid_generate_v7(),
    prefix name_prefix NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    other_name VARCHAR(70) NULL,
    email VARCHAR9(70) NULL,
    phone VARCHAR(14) [],
    gender gender_type NOT NULL,
    address_id INT NOT NULL,
    status alive_status_type NOT NULL,
    student_id UUID NOT NULL INDEX,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_address_id FOREIGN KEY REFERENCES address (id),
    CONSTRAINT fk_student_id FOREIGN KEY REFERENCES student (id)
);

COMMENT ON TABLE parent IS 'Parents of students';


--=======================================
--GUARDIAN
--=======================================

CREATE TABLE IF NOT EXISTS guardian(
    id UUID PRIMARY KEY DEFAULT uuid_generate_v7(),
    prefix name_prefix NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    other_name VARCHAR(70) NULL,
    email VARCHAR9(70) NULL,
    phone VARCHAR(14) [],
    gender gender_type NOT NULL,
    address_id INT NOT NULL,
    student_id UUID NOT NULL INDEX,
    relationship guardian_student_relationship_type NOT NULL,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_address_id FOREIGN KEY REFERENCES address (id),
    CONSTRAINT fk_student_id FOREIGN KEY REFERENCES student (id)
);

COMMENT ON TABLE guardian IS 'Guardian of a STUDENT';


--=======================================
--STUDENT HISTORY
--=======================================

CREATE TABLE IF NOT EXISTS student_history(
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id UUID PRIMARY KEY DEFAULT uuid_generate_v7(),
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    other_name VARCHAR(70) NULL,
    school_id INT NOT NULL,
    birth_date DATE NOT NULL,
    addmission_date DATE NOT NULL,
    student_level_id INT NOT NULL,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_school_id FOREIGN KEY school(school_id)
    CONSTRAINT fk_student_level_id FOREIGN KEY student_level(id)
);

COMMENT ON TABLE student_history IS 'Table to track changes in student data';


--=======================================
--PARENT HISTORY
--=======================================

CREATE TABLE IF NOT EXISTS parent_history(
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id UUID PRIMARY KEY,
    prefix name_prefix NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    other_name VARCHAR(70) NULL,
    email VARCHAR9(70) NULL,
    phone VARCHAR(14) [],
    gender gender_type NOT NULL,
    address_id INT NOT NULL,
    status alive_status_type NOT NULL,
    student_id UUID NOT NULL INDEX,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_address_id FOREIGN KEY REFERENCES address (id),
    CONSTRAINT fk_student_id FOREIGN KEY REFERENCES student (id)
):

COMMENT ON TABLE parent_history IS 'Table to track changes in parent''s data';


--=======================================
--GUARDIAN HISTORY
--=======================================

CREATE TABLE IF NOT EXIST guardian_history(
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id UUID PRIMARY KEY,
    prefix name_prefix NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    other_name VARCHAR(70) NULL,
    email VARCHAR9(70) NULL,
    phone VARCHAR(14) [],
    gender gender_type NOT NULL,
    address_id INT NOT NULL,
    student_id UUID NOT NULL,
    relationship guardian_student_relationship_type NOT NULL,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_address_id FOREIGN KEY REFERENCES address (id),
    CONSTRAINT fk_student_id FOREIGN KEY REFERENCES student (id)
):

COMMENT ON TABLE guardian_history IS 'Table to track changes in guardian data'


--=======================================
--TEACHER SUBJECT HISTORY
--=======================================

CREATE TABLE IF NOT EXISTS teacher_subject_history(
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    employee_id UUID NOT NULL,
    subject_id INT NOT NULL,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_employee_id FOREIGN KEY REFERENCES employee(id),
    CONSTRAINT fk_subject_id FOREIGN KEY REFERENCES subject (id)

);

COMMENT ON TABLE teacher_subject_history IS 'Table to track changes in subjects taught by a teacher'


--=======================================
--PAST STUDENT
--=======================================

CREATE TABLE IF NOT EXIST past_student(
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Student_id UUID,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    other_name VARCHAR(70) NULL,
    school_id INT NOT NULL INDEX,
    birth_date DATE NOT NULL,
    addmission_date DATE NOT NULL,
    student_level_id INT NOT NULL,
    past_student_reason_id INT,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_school_id FOREIGN KEY school(school_id),
    CONSTRAINT fk_student_level_id FOREIGN KEY student_level(id),
    CONSTRAINT fk_past_student_reason_id FOREIGN KEY past_student_reason (id)

);

COMMENT ON TABLE student IS 'Past tudents of the district';



--=======================================
--PAST STUDENT REASON
--=======================================

CREATE TABLE IF NOT EXISTS past_student_reason(
    id SMALLINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    religion_name VARCHAR(50)
);

COMMENT ON TABLE past_student_reason IS 'condition for becoming a past student'



--=======================================
--STUDENT TRANSFER
--=======================================

CREATE TABLE IF NOT EXISTS student_transfer(
    id SMALLINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id UUID PRIMARY KEY DEFAULT uuid_generate_v7(),
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    other_name VARCHAR(70) NULL,
    school_id INT NOT NULL,
    birth_date DATE NOT NULL,
    addmission_date DATE NOT NULL,
    student_level_id INT NOT NULL,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_school_id FOREIGN KEY school(school_id)
    CONSTRAINT fk_student_level_id FOREIGN KEY student_level(id)
);

COMMENT ON TABLE religion IS 'Internal district transfer list'


--=======================================
--TRIGGER FUNCTIONS
--=======================================



























































































