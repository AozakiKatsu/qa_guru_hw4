from qa_guru_hw4.data import users
from qa_guru_hw4.model.pages.application import app


def test_with_app_manager():
    student = users.student
    (
        app
        .left_panel
        .open_simple_registration_form()
        .simple_register(student)
        .should_simple_register_with(student)
    )
