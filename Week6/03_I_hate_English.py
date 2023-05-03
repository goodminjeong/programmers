def solution(numbers):
    en_to_num = {
        "zero":"0",
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9",

    }
    answer, en_num = "", ""
    for num in numbers:
        en_num += num
        if en_num in en_to_num:
            answer += en_num.replace(en_num, en_to_num[en_num])
            en_num = ""
    return int(answer)

print(solution("onetwothreefourfivesixseveneightnine")) # 123456789
print(solution("onefourzerosixseven"))                  # 14067