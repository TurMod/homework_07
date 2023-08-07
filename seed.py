import faker

from connect_db import session
from models import Teacher, Group, Student, Subject, Grade
from sqlalchemy import func
from random import randint, choice


fake_data = faker.Faker()

subjects = (
  'Algebra',
  'Geometry',
  'Physics',
  'Chemistry',
  'Biology',
  'Computer Science',
  'English',
  'Literature',
  'Geography',
  'History',
  'Art',
  'Music',
  'Physical Education'
)

def create_teachers(n):
    for _ in range(n):
        first_name, last_name = fake_data.first_name(), fake_data.last_name()
        teacher = Teacher(first_name=first_name, last_name=last_name)
        session.add(teacher)
    session.commit()

def create_groups(n):
    for _ in range(n):
        group_name = fake_data.company()
        group = Group(name=group_name)
        session.add(group)
    session.commit()

def create_subjects(n, subjects_list=subjects):
    count_id = session.query(func.count(Teacher.id)).select_from(Teacher).one()[0]
    for _ in range(n):
        subject_name = choice(subjects_list)
        subject = Subject(name=subject_name, teacher_id=randint(1, count_id))
        session.add(subject)
    session.commit()

def create_students(n):
    count_id = session.query(func.count(Group.id)).select_from(Group).one()[0]
    for _ in range(n):
        first_name, last_name = fake_data.first_name(), fake_data.last_name()
        student = Student(first_name=first_name, last_name=last_name, group_id=randint(1, count_id))
        session.add(student)
    session.commit()

def create_grades(n):
    count_students = session.query(func.count(Student.id)).select_from(Student).one()[0]
    count_subjects = session.query(func.count(Subject.id)).select_from(Subject).one()[0]
    for student_id in range(1, count_students + 1):
        for subject_id in range(1, count_subjects + 1):
            for _ in range(n):
                grade_ = Grade(grade=randint(1, 12), subject_id=subject_id, student_id=student_id)
                session.add(grade_)
    session.commit()

if __name__ == '__main__':
    create_teachers(5)
    create_subjects(5)
    create_groups(3)
    create_students(30)
    create_grades(2)