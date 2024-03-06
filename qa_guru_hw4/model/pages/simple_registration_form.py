from selene import browser, have
from qa_guru_hw4.data.users import User


class SimpleRegistration:

    def open(self):
        browser.open('https://demoqa.com/text-box')
        return self

    def simple_register(self, user: User):
        browser.element('[id=userName]').type(f'{user.first_name} {user.last_name}')
        browser.element('[id=userEmail]').type(user.email)
        browser.element('[id=currentAddress]').type(user.address)
        browser.element('#submit').click()
        return self

    def should_simple_register_with(self, user: User):
        browser.element('#name').should(have.text(f'{user.first_name} {user.last_name}'))
        browser.element('#email').should(have.text(user.email))
        browser.element('#output').should(have.text(user.address))
        return self

