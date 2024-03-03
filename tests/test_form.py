from qa_guru_hw4.model.pages.registration_page import RegistrationPage


def test_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page \
        .fill_firstname('Serafima') \
        .fill_lastname('Lykova') \
        .fill_email('Lykova@mail.ru') \
        .fill_gender('Female') \
        .fill_number('1234567890') \
        .fill_date_of_birth('1990', 'December', '05') \
        .fill_subjects('Maths', 'English') \
        .fill_hobbies('Sports') \
        .upload_file('testpic.jpg') \
        .fill_address('Address') \
        .fill_state('NCR') \
        .fill_city('Delhi') \
        .press_submit() \
        .should_register_user_with('Serafima Lykova',
                                   'Lykova@mail.ru',
                                   'Female',
                                   '1234567890',
                                   '05 December,1990',
                                   'Maths, English',
                                   'Sports',
                                   'testpic.jpg',
                                   'Address',
                                   'NCR Delhi')
