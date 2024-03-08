from qa_guru_hw4.model.pages.registration_page import RegistrationPage


def test_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page \
        .fill_first_name('Serafima') \
        .fill_last_name('Lykova') \
        .fill_email('Lykova@mail.ru') \
        .fill_gender('Female') \
        .fill_phone_number('1234567890') \
        .fill_date_of_birth('1990', 'December', '05') \
        .fill_subjects('Maths', 'English') \
        .fill_hobbies('Sports') \
        .upload_file('testpic.jpg') \
        .fill_address('Address') \
        .fill_state('NCR') \
        .fill_city('Delhi') \
        .press_submit()
    registration_page.should_register_user_with('Serafima Lykova',
                                                'Lykova@mail.ru',
                                                'Female',
                                                '1234567890',
                                                '05 December,1990',
                                                'Maths, English',
                                                'Sports',
                                                'testpic.jpg',
                                                'Address',
                                                'NCR Delhi')
