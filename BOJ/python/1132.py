# 문제
# N개의 수가 주어진다. 이 숫자는 모두 자연수이고, 알파벳 A부터 J가 자리수를 대신해서 쓰여 있다. 이 알파벳은 모두 한 자리를 의미한다. 그리고, 각 자리수는 정확하게 알파벳 하나이다. 0으로 시작하는 수는 없다. 이때, 가능한 수의 합 중 최댓값을 구해보자.
#
# 입력
# 첫째 줄에 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 각 수가 주어진다. 수의 길이는 최대 12이다. 적어도 한 알파벳은 수의 가장 처음에 주어지지 않는다.
#
# 출력
# 첫째 줄에 합의 최댓값을 출력한다.
n = int(input())
match = [[0, False] for _ in range(10)]  # A B C ..
answer = 0
for _ in range(n):
    word = str(input())
    m = 1
    match[ord(word[0])-65][1] = True
    for c in range(len(word)-1, -1, -1):
        match[ord(word[c])-65][0] += m
        m *= 10
match.sort(reverse=True)
if match[9][1]:
    for i in range(8, -1, -1):
        if not match[i][1]:
            del match[i]
            break
for i in range(9):
    answer += match[i][0] * (9-i)
print(answer)
