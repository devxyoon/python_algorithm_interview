import re

# 주어진 문자열이 팰린드롬인지 확인하라.
# 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.


def solution(s: str) -> bool:
    s = re.sub('[^a-z0-9]', '', s.lower())      #re.sub() 함수는 문자열에서 매치된 텍스트를 다른 텍스트로 치환할 때 사용
    return s == s[::-1]                         #문자열슬라이싱
