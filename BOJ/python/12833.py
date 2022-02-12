# 문제
# 세 수 A, B, C를 입력 받은 다음, ( ( ( ( A XOR B ) XOR B ) XOR B ) … ) XOR B 형태로 연산을 C회 했을 때의 결과값을 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 A, B, C가 주어진다. (0 < A, B, C ≤ 109)
#
# 출력
# 첫째 줄에 계산된 결과를 출력한다.
a, b, c=map(int, input().split())
for _ in range(c%2):
    a^=b
print(a)
