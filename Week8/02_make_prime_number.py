from itertools import combinations


def is_prime_number(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        if is_prime_number(sum(i)):
            answer += 1
    return answer


print(solution([1, 2, 3, 4]))       # 1
print(solution([1, 2, 7, 6, 4]))    # 4
