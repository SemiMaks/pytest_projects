# pytest directory #


**Do not** commit this to version control.

See [the docs](https://docs.pytest.org/en/stable/how-to/cache.html) for more information.

---
Фикстуры
https://docs.pytest.org/en/8.0.x/reference/reference.html#fixtures  
https://pytest-docs-ru.readthedocs.io/ru/latest/contents.html  
https://temofeev.ru/info/articles/vstroennye-fikstury-pytest/  

Потоки ввода/вывода ошибок:

* Capfd
/'''
def test_system_echo(capfd):
      os.system('echo "hello"')
      captured = capfd.readouterr()
      assert captured.out == "hello\n"
/'''

* Capfdbinary
'''
def test_system_echo(capfdbinary):
      os.system('echo "hello"')
      captured = capfdbinary.readouterr()
      assert captured.out == b"hello\n"
'''

* Capsys
'''
def test_output(capsys):
        print("hello")
        captured = capsys.readouterr()
        assert captured.out == "hello\n"
'''

* Capsysbinary
'''
 def test_output(capsysbinary):
        print("hello")
        captured = capsysbinary.readouterr()
        assert captured.out == b"hello\n"
'''

Логирование:
* Caplog
'''
# Задать уровень логирования
def test_foo(caplog):
    caplog.set_level(logging.INFO)
    for message in caplog.messages:
        assert "for debug level" not in message
# Пример проверки уровня логирования и текста в сообщении лога
def test_baz(caplog):
    func_under_test()
    for record in caplog.records:
        assert record.levelname != "CRITICAL"
    assert "wally" not in caplog.text
'''
* Recwarn
'''
import warnings

def test_check_warnings(recwarn):
    warnings.warn("hello", UserWarning)
    assert len(recwarn) == 1
    warn = recwarn.pop(UserWarning)
    assert issubclass(warn.category, UserWarning)
    assert str(warn.message) == "hello"
    assert warn.filename
'''