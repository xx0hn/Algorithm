# 문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
#
# 출력
# 첫째 줄부터 차례대로 별을 출력한다.
n=int(input())
for i in range(n):
    if i%2==0:
        print('* '*n)
    else:
        print(' *'*n)
