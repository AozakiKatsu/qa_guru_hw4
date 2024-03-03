from qa_guru_hw4.data import users
from qa_guru_hw4.model.pages.registration_page import RegistrationPage


def test():
    registration_page = RegistrationPage()
    student = users.student

    registration_page.open() \
        .register(student) \
        .should_register_user_with(student)
