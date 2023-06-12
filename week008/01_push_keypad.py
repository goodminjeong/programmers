def solution(numbers, hand):
    answer = ''
    keypad = {1:(0,0), 2:(1,0), 3:(2,0),
              4:(0,1), 5:(1,1), 6:(2,1),
              7:(0,2), 8:(1,2), 9:(2,2),
                       0:(1,3)}
    left, right = (0,3), (2,3)
        
    for number in numbers:
        # 왼쪽 키패드
        if number in [1,4,7]:
            answer += "L"
            left = keypad[number]
            
        # 오른쪽 키패드
        elif number in [3,6,9]:
            answer += "R"
            right = keypad[number]
            
        # 가운데 키패드
        else:
            # 현재 손가락 위치와 키패드 간의 거리 계산
            left_distance = abs(keypad[number][0]-left[0]) + abs(keypad[number][1]-left[1])
            right_distance = abs(keypad[number][0]-right[0]) + abs(keypad[number][1]-right[1])
            
            # 왼쪽이 더 가까울 때
            if left_distance < right_distance:
                answer += "L"
                left = keypad[number]
                
            # 오른쪽이 더 가까울 때
            elif left_distance > right_distance:
                answer += "R"
                right = keypad[number]
                
            # 거리가 똑같을 때
            else:
                if hand == "left":
                    answer += "L"
                    left = keypad[number]
                else:
                    answer += "R"
                    right = keypad[number]                    
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")) # LRLLLRLLRRL
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))  # LRLLRRLLLRR
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))    # LLRLLRLLRL
