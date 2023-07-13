"""
예산

<문제 설명>
- S사에서는 각 부서에 필요한 물품을 지원해 주기 위해 부서별로 물품을 구매하는데 필요한 금액을 조사했습니다.
- 그러나, 전체 예산이 정해져 있기 때문에 모든 부서의 물품을 구매해 줄 수는 없습니다.
- 그래서 최대한 많은 부서의 물품을 구매해 줄 수 있도록 하려고 합니다.
- 물품을 구매해 줄 때는 각 부서가 신청한 금액만큼을 모두 지원해 줘야 합니다.
- 예를 들어 1,000원을 신청한 부서에는 정확히 1,000원을 지원해야 하며, 1,000원보다 적은 금액을 지원해 줄 수는 없습니다.
- 부서별로 신청한 금액이 들어있는 배열 d와 예산 budget이 매개변수로 주어질 때, 최대 몇 개의 부서에 물품을 지원할 수 있는지 return 하도록 solution 함수를 완성해주세요.

<제한사항>
- d는 부서별로 신청한 금액이 들어있는 배열이며, 길이(전체 부서의 개수)는 1 이상 100 이하입니다.
- d의 각 원소는 부서별로 신청한 금액을 나타내며, 부서별 신청 금액은 1 이상 100,000 이하의 자연수입니다.
- budget은 예산을 나타내며, 1 이상 10,000,000 이하의 자연수입니다.
"""
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from func_speed import func_speed


# 첫 번째 풀이
@func_speed
def solution1(d, budget):
    total, answer = 0, 0
    d.sort()
    for apply in d:
        total += apply
        answer += 1
        if total > budget:
            answer -= 1
            break
        elif (total == budget) or (total < budget and len(d) == 1):
            break
    return answer


# 두 번째 풀이
@func_speed
def solution2(d, budget):
    total, answer = 0, 0
    d.sort()
    for apply in d:
        total += apply
        if total > budget:
            break
        answer += 1
    return answer


solution1([1, 3, 2, 5, 4], 9)
solution1([2, 2, 3, 3], 10)
solution1([100], 101)
solution1([100], 99)

solution2([1, 3, 2, 5, 4], 9)
solution2([2, 2, 3, 3], 10)
solution2([100], 101)
solution2([100], 99)
