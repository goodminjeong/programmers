"""
없는 숫자 더하기

<문제 설명>
- 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다. 
- numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.

<제한 조건>
- 1 ≤ numbers의 길이 ≤ 9
- 0 ≤ numbers의 모든 원소 ≤ 9
- numbers의 모든 원소는 서로 다릅니다.
"""
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from func_speed import func_speed


@func_speed
def solution(numbers):
    num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in numbers:
        if num in num_list:
            num_list.remove(num)
    answer = sum(num_list)
    return answer


solution([1, 2, 3, 4, 6, 7, 8, 0])
solution([5, 8, 4, 0, 6, 7, 9])
