import math


def is_prime_number(number):
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return 0
    return 1


def solution(n):
    answer = 0
    for num in range(2, n+1):
        answer += is_prime_number(num)
    return answer


print(solution(10))  # 4
print(solution(5))   # 3
