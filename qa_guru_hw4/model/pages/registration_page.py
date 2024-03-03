from selene import browser, have

from qa_guru_hw4 import recource
from qa_guru_hw4.data.users import User


class RegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[name=gender]')
        self.phone_number = browser.element('#userNumber')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.date_of_birth_year = browser.element('.react-datepicker__year-select')
        self.date_of_birth_month = browser.element('.react-datepicker__month-select')
        self.date_of_birth_day = browser
        self.subjects = browser.element('#subjectsInput')
        self.hobbies = browser.all('.custom-checkbox')
        self.upload_file = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.state = browser.element('#react-select-3-input')
        self.city = browser.element('#react-select-4-input')
        self.submit = browser.element('#submit')

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        return self

    def register(self, user: User):
        self.first_name.type(user.first_name)
        self.last_name.type(user.last_name)
        self.email.type(user.email)
        self.gender.element_by(have.value(user.gender)).element('..').click()
        self.phone_number.type(user.phone_number)
        self.date_of_birth.click()
        self.date_of_birth_year.type(user.date_of_birth_year)
        self.date_of_birth_month.type(user.date_of_birth_month)
        self.date_of_birth_day.element(
            f'.react-datepicker__day--0{user.date_of_birth_day}:not(.react-datepicker__day--outside-month)'
        ).click()
        self.subjects.type(user.subjects).press_enter()
        self.hobbies.element_by(have.exact_text(user.hobbies)).click()
        self.upload_file.send_keys(recource.path(user.upload_file))
        self.address.type(user.address)
        self.state.type(user.state).press_enter()
        self.city.type(user.city).press_enter()
        self.submit.press_enter()
        return self

    def should_register_user_with(self, user: User):
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            str(user.phone_number),
            f'{user.date_of_birth_day} {user.date_of_birth_month},{user.date_of_birth_year}',
            user.subjects,
            user.hobbies,
            user.upload_file,
            user.address,
            f'{user.state} {user.city}'))
        return self
