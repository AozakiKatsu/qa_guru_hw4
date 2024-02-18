import os
from selene import browser, have, be, by


def test_form():
    browser.open('https://demoqa.com/automation-practice-form')
    # заполнение формы
    browser.element('#firstName').should(be.blank).type("Serafima")
    browser.element('#lastName').should(be.blank).type("Lykova")
    browser.element('#userEmail').should(be.blank).type("Lykova@mail.ru")
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').should(be.blank).type("1234567890")
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().element(by.text('1990')).click()
    browser.element('.react-datepicker__month-select').click().element(by.text('December')).click()
    browser.element('.react-datepicker__day--005').click()
    browser.element('#subjectsInput').type("Math").press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('testpic.jpg'))
    browser.element('#currentAddress').should(be.blank).type('Address')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').press_enter()

    # проверка заполненности формы
    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))

    # проверка на соответствие данных
    browser.element('.table > tbody > tr:nth-child(1)').should(have.text('Serafima Lykova'))
    browser.element('.table > tbody > tr:nth-child(2)').should(have.text('Lykova@mail.ru'))
    browser.element('.table > tbody > tr:nth-child(3)').should(have.text('Female'))
    browser.element('.table > tbody > tr:nth-child(4)').should(have.text('1234567890'))
    browser.element('.table > tbody > tr:nth-child(5)').should(have.text('05 December,1990'))
    browser.element('.table > tbody > tr:nth-child(6)').should(have.text('Maths'))
    browser.element('.table > tbody > tr:nth-child(7)').should(have.text('Sports'))
    browser.element('.table > tbody > tr:nth-child(8)').should(have.text('testpic.jpg'))
    browser.element('.table > tbody > tr:nth-child(9)').should(have.text('Address'))
    browser.element('.table > tbody > tr:nth-child(10)').should(have.text('NCR Delhi'))
