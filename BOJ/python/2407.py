# 문제
# nCm을 출력한다.
#
# 입력
# n과 m이 주어진다. (5 ≤ n ≤ 100, 5 ≤ m ≤ 100, m ≤ n)
#
# 출력
# nCm을 출력한다.
n, m=map(int, input().split())
top=1
bottom=1
for i in range(m):
    top*=(n-i)
    bottom*=(m-i)
print(top//bottom)
