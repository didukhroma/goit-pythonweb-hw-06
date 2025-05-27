import random
import datetime
from connect import session, engine
from models import Student, Teacher, Group, Grade, Subject


from faker import Faker


faker = Faker()

teachers: list[Teacher] = [
    Teacher(name=f"{faker.first_name()} {faker.last_name()}", email=faker.email())
    for _ in range(5)
]
session.add_all(teachers)
session.commit()

groups: list[Group] = [Group(name=faker.word()) for _ in range(3)]
session.add_all(groups)
session.commit()


subjects: list[Subject] = [
    Subject(name=faker.word(), teacher=random.choice(teachers)) for _ in range(8)
]
session.add_all(subjects)
session.commit()

students: list[Student] = [
    Student(
        name=f"{faker.first_name()} {faker.last_name()}",
        email=faker.email(),
        group=random.choice(groups),
    )
    for _ in range(50)
]
session.add_all(students)
session.commit()

grades: list[Grade] = []

for student in students:
    for subject in subjects:
        for _ in range(20):
            grades.append(
                Grade(
                    subject=random.choice(subjects),
                    student=student,
                    grade=random.randint(51, 100),
                    date_received=faker.past_date(),
                )
            )
session.add_all(grades)
session.commit()
