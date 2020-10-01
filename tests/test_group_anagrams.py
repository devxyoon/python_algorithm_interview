from examples import group_anagrams


def test_solution():
    assert group_anagrams.solution(["eat", "tea", "tan", "ate", "nat", "bat"]) \
           == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
