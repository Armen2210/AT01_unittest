import pytest
from main import isPalindrome
# from main import check



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

@pytest.mark.parametrize("test_input,expected", [
    ('level', True),
    ('python', False),
    ('racecar', True),
    ('', True),
])

def test_isPalindrome(test_input, expected):
    assert isPalindrome(test_input) == expected
