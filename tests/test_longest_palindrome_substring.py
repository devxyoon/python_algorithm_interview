from examples import longest_palindrome_substring


def test_solution():
    assert longest_palindrome_substring.solution("babad") == "bab" or "aba"
    assert longest_palindrome_substring.solution("cbbd") == "bb"
