def solution(bin1, bin2):
    answer = ''
    bin_to_decimal1 = int(bin1, 2)
    bin_to_decimal2 = int(bin2, 2)
    answer = bin_to_decimal1 + bin_to_decimal2
    return format(answer, 'b')


print(solution("10", "11"))     # 101
print(solution("1001", "1111"))  # 11000
