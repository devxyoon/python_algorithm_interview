from examples import valid_palindrome


def test_solution():
    assert valid_palindrome.solution('A man, a plan, a canal: Panama') is True
    assert valid_palindrome.solution('race a car') is False
