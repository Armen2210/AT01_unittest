from homework_AT02_pytest import count_vowels



def test_only_vowels():
    assert count_vowels("аеёиоуыэюя") == 10

def test_no_vowels():
    assert count_vowels("бвгджз") == 0

def test_mixed_string():
    assert count_vowels("ПрИвЕт Мир") == 3

