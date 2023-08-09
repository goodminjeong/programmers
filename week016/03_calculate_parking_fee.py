"""
주차 요금 계산

<문제 설명>
- 주차장의 요금표와 차량이 들어오고(입차) 나간(출차) 기록이 주어졌을 때, 차량별로 주차 요금을 계산하려고 합니다.
- 주차 요금을 나타내는 정수 배열 fees, 자동차의 입/출차 내역을 나타내는 문자열 배열 records가 매개변수로 주어집니다.
- 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return 하도록 solution 함수를 완성해주세요.

<제한사항>
- fees의 길이 = 4
    - fees[0] = 기본 시간(분)
    - 1 ≤ fees[0] ≤ 1,439
    - fees[1] = 기본 요금(원)
    - 0 ≤ fees[1] ≤ 100,000
    - fees[2] = 단위 시간(분)
    - 1 ≤ fees[2] ≤ 1,439
    - fees[3] = 단위 요금(원)
    - 1 ≤ fees[3] ≤ 10,000
- 1 ≤ records의 길이 ≤ 1,000
    - records의 각 원소는 "시각 차량번호 내역" 형식의 문자열입니다.
    - 시각, 차량번호, 내역은 하나의 공백으로 구분되어 있습니다.
    - 시각은 차량이 입차되거나 출차된 시각을 나타내며, HH:MM 형식의 길이 5인 문자열입니다.
        - HH:MM은 00:00부터 23:59까지 주어집니다.
        - 잘못된 시각("25:22", "09:65" 등)은 입력으로 주어지지 않습니다.
    - 차량번호는 자동차를 구분하기 위한, `0'~'9'로 구성된 길이 4인 문자열입니다.
    - 내역은 길이 2 또는 3인 문자열로, IN 또는 OUT입니다. IN은 입차를, OUT은 출차를 의미합니다.
    - records의 원소들은 시각을 기준으로 오름차순으로 정렬되어 주어집니다.
    - records는 하루 동안의 입/출차된 기록만 담고 있으며, 입차된 차량이 다음날 출차되는 경우는 입력으로 주어지지 않습니다.
    - 같은 시각에, 같은 차량번호의 내역이 2번 이상 나타내지 않습니다.
    - 마지막 시각(23:59)에 입차되는 경우는 입력으로 주어지지 않습니다.
    - 아래의 예를 포함하여, 잘못된 입력은 주어지지 않습니다.
        - 주차장에 없는 차량이 출차되는 경우
        - 주차장에 이미 있는 차량(차량번호가 같은 차량)이 다시 입차되는 경우
"""
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from func_speed import func_speed


@func_speed
def solution(fees, records):
    # 주차장에 들어온 차량 리스트 만들기
    cars = []
    for car_number in records:
        cars.append(car_number.split(" ")[1])
        cars = list(set(cars))  # 중복 제거
    cars.sort()  # 차량번호순으로 정렬

    # 각 차량별 누적 주차 시간을 담을 딕셔너리 만들기
    parking_times = dict.fromkeys(cars, 0)

    # 내역에 따른 각 차량별 누적 주차 시간 계산하기
    parking = []
    for record in records:
        time, number, status = record.split(" ")
        time = int(time.split(":")[0]) * 60 + int(time.split(":")[1])
        if status == "IN":
            parking.append(number)
            parking_times[number] += -time
        else:
            parking.remove(number)
            parking_times[number] += time

    # 주차장 OUT이 없는 차량 누적 주차시간 계산하기
    if len(parking) != 0:
        for n in parking:
            parking_times[n] += 1439

    # 각 차량별 요금 계산하기
    answer = []
    for car in cars:
        if parking_times[car] > fees[0]:
            answer.append(
                fees[1] + (-((fees[0] - parking_times[car]) // fees[2])) * fees[3]
            )
        else:
            answer.append(fees[1])
    return answer


solution(
    [180, 5000, 10, 600],
    [
        "05:34 5961 IN",
        "06:00 0000 IN",
        "06:34 0000 OUT",
        "07:59 5961 OUT",
        "07:59 0148 IN",
        "18:59 0000 IN",
        "19:09 0148 OUT",
        "22:59 5961 IN",
        "23:00 5961 OUT",
    ],
)
solution(
    [120, 0, 60, 591],
    [
        "16:00 3961 IN",
        "16:00 0202 IN",
        "18:00 3961 OUT",
        "18:00 0202 OUT",
        "23:58 3961 IN",
    ],
)
solution([1, 461, 1, 10], ["00:00 1234 IN"])
