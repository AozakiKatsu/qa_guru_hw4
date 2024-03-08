import os

from selene import browser, be, have


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)
        return self

    def fill_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()
        return self

    def fill_phone_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_subjects(self, value1, value2):
        browser.element('#subjectsInput').type(value1).press_enter()
        browser.element('#subjectsInput').type(value2).press_enter()
        return self

    def fill_hobbies(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()
        return self

    def upload_file(self, value):
        browser.element('#uploadPicture').send_keys(os.path.abspath(value))
        return self

    def fill_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)
        return self

    def fill_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()
        return self

    def fill_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()
        return self

    def press_submit(self):
        browser.element('#submit').press_enter()
        return self

    def should_register_user_with(self, *value):
        browser.element('.table').all('td').even.should(have.exact_texts(value))
        return self
