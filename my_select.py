from connect_db import session
from models import Teacher, Group, Subject, Student, Grade
from sqlalchemy import func, desc

def select_1():
    result = session.query(Student.first_name, Student.last_name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade)\
        .join(Student)\
        .group_by(Student.id)\
        .order_by(desc('avg_grade'))\
        .limit(5).all()
    return result


def select_2(subject_id):
    result = session.query(Student.first_name, Student.last_name, func.avg(Grade.grade).label('avg_grade'))\
        .select_from(Student)\
        .join(Grade)\
        .filter(Grade.subject_id == subject_id)\
        .group_by(Student.id)\
        .order_by(desc('avg_grade'))\
        .limit(1).one()
    return result

def select_3(subject_id):
    result = session.query(Student.group_id, func.avg(Grade.grade).label('avg_grade'))\
        .select_from(Grade)\
        .join(Student)\
        .join(Subject)\
        .filter(Subject.id == subject_id)\
        .group_by(Student.group_id)\
        .order_by(Student.group_id).all()
    return result

def select_4():
    result = session.query(func.avg(Grade.grade).label('avg_grade'))\
        .select_from(Grade).one()
    return result

def select_5(teacher_id):
    result = session.query(Subject.name.label('courses'))\
        .select_from(Subject)\
        .join(Teacher)\
        .filter(Teacher.id == teacher_id).all()
    return result

def select_6(group_id):
    result = session.query('*')\
        .select_from(Student)\
        .filter_by(group_id=group_id).all()
    return result

def select_7(subject_id, group_id):
    result = session.query(Student.first_name, Student.last_name, Grade.grade)\
        .select_from(Student)\
        .join(Grade)\
        .filter(Grade.subject_id == subject_id, Student.group_id == group_id).all()
    return result

def select_8(teacher_id):
    result = session.query(func.avg(Grade.grade).label('avg_grade'))\
        .select_from(Grade)\
        .join(Subject)\
        .filter(Subject.teacher_id == teacher_id).one()
    return result

def select_9(student_id):
    result = session.query(Subject.name)\
        .select_from(Subject)\
        .join(Grade)\
        .filter(Grade.student_id == student_id)\
        .group_by(Subject.name).all()
    return result

def select_10(student_id, teacher_id):
    result = session.query(Subject.name)\
        .select_from(Subject)\
        .join(Grade)\
        .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id)\
        .group_by(Subject.name).all()
    return result

if __name__ == '__main__':
    ...