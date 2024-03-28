import pytest


@pytest.mark.run(order=2)
def test_send_mail_1(set_up):
    print("Метод 1")
    pass


@pytest.mark.run(order=1)
def test_send_mail_2(set_up):
    print("Метод 2")
    pass


@pytest.mark.run(order=6)
def test_send_mail_3(set_up):
    print("Метод 3")
    pass


@pytest.mark.run(order=5)
def test_send_mail_4(set_up):
    print("Метод 4")
    pass


@pytest.mark.run(order=4)
def test_send_mail_5(set_up):
    print("Метод 5")
    pass


@pytest.mark.run(order=3)
def test_send_mail_6(set_up):
    print("Метод 6")
    pass
