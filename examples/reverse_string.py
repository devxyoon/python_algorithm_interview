# 문자열을 뒤집는 함수를 작성하라.
# 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.
from typing import List


def solution(s: List[str]) -> None:
    s.reverse()                      # reverse()는 리스트에만 제공되는 함수며, 리스트를 뒤집을 수 있다.