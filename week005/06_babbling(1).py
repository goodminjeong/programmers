def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]    
    for b in babbling:
        for w in word:
            if w in b:
                b = b.replace(w, "1", 1)
                try:
                    int(b)
                    answer += 1
                except ValueError:
                    pass            
    return answer

print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))
