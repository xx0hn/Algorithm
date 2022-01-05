# 문제
# 정수 N과 K가 주어졌을 때, 다음 두 조건을 만족하는 문자열 S를 찾는 프로그램을 작성하시오.
#
# 문자열 S의 길이는 N이고, 'A', 'B'로 이루어져 있다.
# 문자열 S에는 0 ≤ i < j < N 이면서 s[i] == 'A' && s[j] == 'B'를 만족하는 (i, j) 쌍이 K개가 있다.
# 입력
# 첫째 줄에 N과 K가 주어진다. (2 ≤ N ≤ 50, 0 ≤ K ≤ N(N-1)/2)
#
# 출력
# 첫째 줄에 문제의 조건을 만족하는 문자열 S를 출력한다. 가능한 S가 여러 가지라면, 아무거나 출력한다. 만약, 그러한 S가 존재하지 않는 경우에는 -1을 출력한다.
n , k = map(int,input().split())
s = 'B'*n
s = list(s)
def check(word):
    cnt = 0
    for i in range(len(word)-1):
        if word[i] == 'A':
            for j in range(i+1,len(word)):
                if word[j] == 'B':
                    cnt += 1
    return cnt

for i in range(n):
    s[i] = 'A'
    if check(s) == k:
        break
    elif check(s) > k:
        s[i] = 'B'

answer = "".join(s)
if answer=='B'*n or answer=='A'*n:
    if k == 0:
        print(answer)
    else:
        print(-1)
else:
    print(answer)
