from faker import Faker
import random
from .models import School, Professor, Course, Rating, Profile
from django.contrib.auth.models import User

def generateUser(n):
    fake=Faker()
    for i in range(n):
        User.objects.create(username=fake.name(), email=fake.email(), password=fake.password())

def generateRating(n):
    for i in range(n):
        course = Course.objects.order_by('?').first()
        author = Profile.objects.order_by('?').first()
        rate = random.randint(1, 5)
        attendance = random.randint(1, 2) % 2 == 0
        grade = random.choice(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D', 'F', 'N'])
        semester = random.choice(['Fall', 'Spring', 'Summer']) + ' ' + str(random.randint(2010, 2022))
        Rating.objects.create(course=course, author=author, rate=rate, attendance=attendance, grade=grade, semester=semester)

def generateProfessor(n):
    departments = ['CPSC', 'MATH', 'ENGL', 'CHIN', 'PHYS', 'SCIE', 'BIOL', 'CHEM']
    fake = Faker()
    for i in range(n):
        index = random.randint(0, len(departments) - 1)
        school = School.objects.first()
        department = departments[index]
        Professor.objects.create(name=fake.name(), school=school, department=department)


def generateCourse(n):
    courseIds = {
        'CPSC' : ['1030', '1040', '1045', '1050', '1150', '1160', '1181', '2150' ,'2190'],
        'MATH':  ['1120', '1150', '1162', '1170', '1171', '2171', '2362' ,'2371'],
        'ENGL':  ['1123', '1125', '1135', '2225'],
        'CHIN': ['1125', '1250', '2223', '3311'],
        'PHYS' : ['1114', '1118', '1125', '2323'],
        'SCIE':  ['1113', '1114'],
        'BIOL': ['1115', '1185', '1215', '2192', '2380'],
        'CHEM': ['1114', '1120', '1220', '2100', '3216'],
    }
    for i in range(n):
        school = School.objects.first()
        professor = Professor.objects.order_by('?').first()
        subject = professor.department
        courseList = courseIds[subject]
        index = random.randint(0, len(courseList)-1)
        course_number = courseList[index]
        Course.objects.create(school=school, subject=subject, course_number=course_number, professor=professor)
    