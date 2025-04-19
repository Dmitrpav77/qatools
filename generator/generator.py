import random
from calendar import firstweekday

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')

def generated_person():
    yield Person(
        full_name=faker_ru.first_name_female() + ' ' + faker_ru.middle_name() + ' ' + faker_ru.last_name_female(),
        first_name=faker_ru.first_name_female(),
        last_name=faker_ru.last_name_female(),
        email=faker_ru.email(),
        salary=random.randint(10000, 500000),
        mobile=f'9{random.randint(10, 99)}{random.randint(1000000, 9999999)}',
        date_of_birth=str(faker_ru.date_of_birth()),
        age=random.randint(20, 50),
        department=faker_ru.job_female(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )

def generated_file(type_file):
    path = rf'O:\pet_project\example{random.randint(0, 999)}.{type_file}'
    file = open(path, 'w+')
    file.write('Hello World!')
    file.close()
    return file.name, path