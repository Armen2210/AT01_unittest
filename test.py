import pytest
# from main import isPalindrome
# from main import sort_list
# from main import check
from main import init_db, add_user, get_user



# def tets_check():
#     assert check(6) == True
#
# def tets_check2():
#     assert check(3) == False
#
# @pytest.mark.parametrize('number, expected', [
#     (2, True),
#     (5, False),
#     (0, True),
#     (56, True),
#     (-3, False)
# ])
#
# def test_check_with_params(number, expected):
#     assert check(number) == expected

# def test_isPalindrome():
#     assert isPalindrome('madam') == True
#     assert isPalindrome('hello') == False

# @pytest.mark.parametrize("test_input,expected", [
#     ('level', True),
#     ('python', False),
#     ('racecar', True),
#     ('', True),
# ])
#
# def test_isPalindrome(test_input, expected):
#     assert isPalindrome(test_input) == expected

# def test_sorted1():
#     assert sort_list([5, 6, 1, 3, 4, 2]) == ([1, 2, 3, 4, 5, 6])
#
# def test_sorted2():
#     assert sort_list([2, -1, -2, 0, 1, 3]) == ([-2, -1, 0, 1, 2, 3])

# Создадим фикстуру. Для этого нужно использовать специальный декоратор, указывающий на то,
# что прописанная здесь функция будет являться фикстурой, подготавливая тестовую среду и предоставляя ресурсы для этой среды;
# Вызовем функцию conn, которая создаст базу данных: init_db, а также возвращаем подключение, чтобы с ним можно было работать;
# Чтобы остальные функции тоже могли работать с подключением conn, используем yield.
# Напоминаем, что yield, как и return, возвращает значения, и в этом случае yield будет возвращать объект conn тестам,
# которые будут использовать нашу фикстуру.
# yield позволяет функции временно приостановить свое выполнение, пока тесты используют ресурс, который мы им передали;
# Закроем подключение.

@pytest.fixture
def db_conn():
    conn = init_db()
    yield conn
    conn.close()

def test_add_or_get_user(db_conn):
    add_user(db_conn, "Piter", 35) # добавили пользователя
    user = get_user(db_conn, "Piter") # проверили наличие пользователя, поместив его в переменную user
    assert user == (1, "Piter", 35) # проводим сравнение: что в переменной user с тем, что в правой части: ==....

