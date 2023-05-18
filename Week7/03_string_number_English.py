def solution(s):
    answer, n = "", ""
    num_en = {"zero": 0,
              "one": 1,
              "two": 2,
              "three": 3,
              "four": 4,
              "five": 5,
              "six": 6,
              "seven": 7,
              "eight": 8,
              "nine": 9}
    for ss in s:
        try:
            int(ss)
            answer += ss
        except ValueError:
            n += ss
            if n in num_en.keys():
                answer += str(num_en[n])
                n = ""
    return int(answer)


print(solution("one4seveneight"))   # 1478
print(solution("23four5six7"))      # 234567
print(solution("2three45sixseven"))  # 234567
print(solution("123"))              # 123
