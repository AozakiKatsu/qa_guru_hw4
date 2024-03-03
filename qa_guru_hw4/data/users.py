import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: int
    date_of_birth_year: int
    date_of_birth_month: str
    date_of_birth_day: str
    subjects: str
    hobbies: str
    upload_file: str
    address: str
    state: str
    city: str


student = User(first_name='Ivan',
               last_name='Ivanov',
               email='Ivanov@ivan.ru',
               gender='Male',
               phone_number=9991119999,
               date_of_birth_year=1990,
               date_of_birth_month='December',
               date_of_birth_day='05',
               subjects='Maths',
               hobbies='Sports',
               upload_file='testpic.jpg',
               address='Address',
               state='NCR',
               city='Delhi')
