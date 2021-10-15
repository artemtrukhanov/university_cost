# ONLINE

salary_for_teacher = 300 # зарплата преподавателя в час
salary_for_methodist = 27000 # зарплата методиста в месяц
salary_for_sysadmin = 40000 # зарплата сисадмина в месяц
salary_for_accountant = 30000 # зарплата бухгалтера в месяц
taxes = 0.13 # подоходный налог
internet = 1000 # интернет в месяц
c1 = 15000

students = 22 # студентов в группе

# OFFLINE

square_for_teacher = 4 # кв. м. на преподавателя
square_for_student = 2 # кв. м. на студента
rent_per_meter = 300
utilities = 100
salary_for_security = 30000 # зарплата охраннику в месяц
salary_for_janitor = 15000 # зарплата уборщице в месяц
salary_for_cloakroomer = 13000 # зарплата градиробщице в месяц

# Оборудование

chair = 1200
desk = 3000
board = 12000
projector = 25000
pc = 30000
equipment = (pc + chair + desk)*22 + board + projector

# Преподаватели по семестрам [лекторы, практики, лабы]
teachers = [[3, 4, 1],
             [3, 3, 3],
             [3, 2, 4],
             [3, 2, 4],
             [3, 2, 4],
             [4, 3, 2],
             [4, 3, 2],
             [3, 4, 3]]

# Количество часов [лекции, практики, лабы]
hours = [
        [104, 112, 16],
        [104, 124, 48],
        [104, 96, 64],
        [104, 61, 80],
        [112, 24, 64],
        [96, 24, 48],
        [88, 64, 24],
        [90, 18, 12]
]

all_teachers = []
all_hours = []
teachers_hours = []

for i in range(0, 7):
    all_teachers.append(sum(teachers[i]))

for i in range(0, 7):
    all_hours.append(sum(hours[i]))

# Зарплата работников
teachers_salary = sum(all_teachers) * sum(all_hours) * salary_for_teacher
teachers_salary += teachers_salary * taxes
methodist_salary = salary_for_methodist * 2 * 12 *4
methodist_salary += methodist_salary * taxes
sysadmin_salary = salary_for_sysadmin * 12 * 4
sysadmin_salary += sysadmin_salary * taxes
accountant_salary = salary_for_accountant * 2 * 12 * 4
accountant_salary += accountant_salary * taxes

security_salary = salary_for_security * 4 * 12 * 4
security_salary += security_salary * taxes
janitor_security = salary_for_janitor * 2 * 12 * 4
janitor_security += janitor_security * taxes
cloakroomer_salary = salary_for_cloakroomer * 2 * 12 * 4
cloakroomer_salary += cloakroomer_salary * taxes

uni_needs = (c1 + internet) * 12 * 4

square_for_teacher = square_for_teacher * sum(all_teachers) * rent_per_meter
square_for_student = students * square_for_student * rent_per_meter
utilities = utilities * (square_for_student + square_for_teacher)

rent_full = 4 * (square_for_teacher + square_for_student + utilities)

online = (teachers_salary + methodist_salary + sysadmin_salary + accountant_salary + uni_needs) // (students*4*8)
offline = (teachers_salary + methodist_salary + sysadmin_salary + accountant_salary + security_salary + janitor_security + cloakroomer_salary + rent_full + equipment + uni_needs) // (students*4*8)
print('Стоимость онлайн обучения: ', online)
print('Стоимость офлайн обучения: ', offline)
