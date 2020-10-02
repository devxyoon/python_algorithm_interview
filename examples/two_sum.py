# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.


from typing import List


def solution(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]
