"""
부족한 금액 계산하기

<문제 설명>
- 새로 생긴 놀이기구는 인기가 매우 많아 줄이 끊이질 않습니다.
- 이 놀이기구의 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다.
- 즉, 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.
- 놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
- 단, 금액이 부족하지 않으면 0을 return 하세요.

<제한사항>
- 놀이기구의 이용료 price : 1 ≤ price ≤ 2,500, price는 자연수
- 처음 가지고 있던 금액 money : 1 ≤ money ≤ 1,000,000,000, money는 자연수
- 놀이기구의 이용 횟수 count : 1 ≤ count ≤ 2,500, count는 자연수
"""
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from func_speed import func_speed


# 첫 번째 풀이
@func_speed
def solution1(price, money, count):
    spend_list = [price * count]
    for i in range(1, count):
        spend_list.append(price * i)
    spend = sum(spend_list)
    spend -= money
    return spend if spend > 0 else 0


# 두 번째 풀이
@func_speed
def solution2(price, money, count):
    spend = price * count
    spend_list = []
    while spend >= price:
        spend_list.append(spend)
        spend -= price
    spend = sum(spend_list)
    spend -= money
    return spend if spend > 0 else 0


# 세 번째 풀이
@func_speed
def solution3(price, money, count):
    spend = price * count
    sum_spend = 0
    while spend >= price:
        sum_spend += spend
        spend -= price
    sum_spend -= money
    return sum_spend if sum_spend > 0 else 0


# 네 번째 풀이
@func_speed
def solution4(price, money, count):
    sum_spend = 0
    for i in range(1, count + 1):
        sum_spend += price * i
    sum_spend -= money
    return sum_spend if sum_spend > 0 else 0


# 다섯 번째 풀이
@func_speed
def solution5(price, money, count):
    sum_spend = sum(range(price, price * count + 1, price))
    sum_spend -= money
    return sum_spend if sum_spend > 0 else 0


solution1(3, 20, 4)
solution2(3, 20, 4)
solution3(3, 20, 4)
solution4(3, 20, 4)
solution5(3, 20, 4)
