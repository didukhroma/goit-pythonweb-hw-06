from connect import session
from models import Student, Subject, Teacher, Grade, Group
from sqlalchemy import select, func, desc


def select_1():
    stmt = (
        select(Student.name, func.avg(Grade.grade).label("average_grade"))
        .join(Grade, Student.grades)
        .group_by(Student.id)
        .order_by(desc("average_grade"))
        .limit(5)
    )
    result = session.execute(stmt)
    for idx, row in enumerate(result):
        print(f"{idx + 1} Student: {row.name} - Average grade:{row.average_grade:.1f}")


def select_2(subject_id: int):
    stmt = (
        select(Student.name, func.avg(Grade.grade).label("average_grade"))
        .join(Grade, Student.grades)
        .where(Grade.subject_id == subject_id)
        .group_by(Student.id)
        .order_by(desc("average_grade"))
        .limit(1)
    )
    result = session.execute(stmt)
    for row in result:
        print(f"Student: {row.name} - Average grade:{row.average_grade:.1f}")


def select_3(subject_id: int):
    stmt = (
        select(
            Group.name,
            func.avg(Grade.grade).label("average_grade"),
        )
        .join(Student, Group.students)
        .join(Grade, Student.grades)
        .where(Grade.subject_id == subject_id)
        .group_by(Group.id)
        .order_by(desc("average_grade"))
    )
    result = session.execute(stmt)
    for row in result:
        print(f"Group: {row.name} - Average grade:{row.average_grade:.1f}")


def select_4():
    stmt = select(func.avg(Grade.grade).label("average_grade"))
    result = session.execute(stmt)
    for row in result:
        print(f"Average grade: {row.average_grade:.1f}")


def select_5(teacher_id):
    stmt = select(Subject.name).where(Subject.teacher_id == teacher_id)
    result = session.execute(stmt)
    for row in result:
        print(f"Subject: {row.name}")


def select_6(group_id):
    stmt = select(Student.name).where(Student.group_id == group_id)
    result = session.execute(stmt)
    for row in result:
        print(f"Student: {row.name}")


def select_7(group_id, subject_id):
    stmt = (
        select(Student.name, Grade.grade)
        .join(Group, Student.group_id == Group.id)
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .where(Student.group_id == group_id)
        .where(Subject.id == subject_id)
    )
    result = session.execute(stmt)
    for row in result:
        print(f"Student: {row.name} - Grade:{row.grade}")


def select_8(teacher_id):
    stmt = (
        select(Subject.name, func.avg(Grade.grade).label("average_grade"))
        .join(Grade, Subject.id == Grade.subject_id)
        .where(Subject.teacher_id == teacher_id)
        .group_by(Subject.name)
    )

    result = session.execute(stmt)
    for row in result:
        print(f"Subject: {row.name} - Average grade:{row.average_grade:.1f}")


def select_9(student_id):
    stmt = (
        select(Student.name, Subject.name.label("subject"))
        .distinct()
        .join(Grade, Grade.student_id == Student.id)
        .join(Subject, Grade.subject_id == Subject.id)
        .where(Student.id == student_id)
    )

    result = session.execute(stmt)
    for row in result:
        print(f"Student: {row.name} - Subject:{row.subject}")


def select_10(student_id, teacher_id):
    stmt = (
        select(
            Student.name, Teacher.name.label("teacher"), Subject.name.label("subject")
        )
        .distinct()
        .join(Grade, Grade.student_id == Student.id)
        .join(Subject, Grade.subject_id == Subject.id)
        .join(Teacher, Teacher.id == Subject.teacher_id)
        .where(Student.id == student_id)
        .where(Teacher.id == teacher_id)
    )

    result = session.execute(stmt)
    for row in result:
        print(f"Student: {row.name} - Teacher: {row.teacher} - Subject:{row.subject}")


# select_1()
# select_2(1)
# select_3(2)
# select_4()
# select_5(2)
# select_6(1)
# select_7(1, 2)
# select_8(2)
# select_9(2)
# select_10(2, 2)
