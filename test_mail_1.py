import pytest


@pytest.fixture()
def set_up():
    print("Вход в систему выполнен!")


def test_send_mail_1(set_up):
    print("письмо отправлено")
    pass


def test_send_mail_2(set_up):
    print("письмо отправлено")
    pass


def test_send_mail_3(set_up):
    print("письмо отправлено")
    pass

# test_send_mail()
# pytest -s -v