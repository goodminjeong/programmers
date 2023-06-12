def solution(strings, n):
    answer = []

    # 정렬 기준이 되는 배열 생성
    sort_string = []
    for string in strings:
        sort_string.append(string[n])
    sort_string.sort()

    # stirngs를 사전순으로 먼저 정렬함
    strings.sort()

    for sort in sort_string:  # 기준이 되는 알파벳과
        for string in strings:  # 사전순으로 정렬된 strings를 돌리면서
            if sort == string[n]:  # 기준 알파벳과 string의 n번째 알파벳이 일치하면
                answer.append(string)  # answer에 string을 붙이고
                strings.remove(string)  # 그 string은 strings에서 뺀다(안 빼면 중복 발생)
                break  # answer에 string 붙었으니까 strings 더 돌릴 필요없음

    return answer


print(solution(["sun", "bed", "car"], 1))  # ['car', 'bed', 'sun']
print(solution(["abce", "abcd", "cdx"], 2))  # ['abcd', 'abce', 'cdx']
