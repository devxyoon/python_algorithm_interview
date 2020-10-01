from examples import most_common_word


def test_solution():
    assert most_common_word.solution("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]) \
           == "ball"
