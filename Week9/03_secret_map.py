import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from func_speed import func_speed


# 내 맘대로 풀이
@func_speed
def solution1(n, arr1, arr2):
    answer = []
    binary_arr1 = list(map(lambda x: str(bin(x))[2:].zfill(n), arr1))
    binary_arr2 = list(map(lambda x: str(bin(x))[2:].zfill(n), arr2))

    for i in range(n):
        cipher = ""
        for j in range(n):
            if binary_arr1[i][j] == "0" and binary_arr2[i][j] == "0":
                cipher += " "
            else:
                cipher += "#"
        answer.append(cipher)
    return answer


# 비트연산 사용한 풀이
@func_speed
def solution2(n, arr1, arr2):
    answer = []
    binary_arr = list(map(lambda x, y: format(x | y, "b").rjust(n), arr1, arr2))

    for binary in binary_arr:
        binary = binary.replace("0", " ")
        binary = binary.replace("1", "#")
        answer.append(binary)

    return answer


print(solution1(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution2(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
# ['#####', '# # #', '### #', '#  ##', '#####']
# ['#####', '# # #', '### #', '#  ##', '#####']
print(solution1(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
print(solution2(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
# ['######', '###  #', '##  ##', ' #### ', ' #####', '### # ']
# ['######', '###  #', '##  ##', ' #### ', ' #####', '### # ']
