# 문자열 배열을 받아 애너그램 단위로 그룹핑하라.
import collections
from typing import List


def solution(words: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in words:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())
