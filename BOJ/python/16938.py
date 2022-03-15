# 문제
# 알고리즘 캠프를 열려면 많은 준비가 필요하다. 그 중 가장 중요한 것은 문제이다. 오늘은 백준이를 도와 알고리즘 캠프에 사용할 문제를 고르려고 한다.
#
# 백준이는 문제를 N개 가지고 있고, 모든 문제의 난이도를 정수로 수치화했다. i번째 문제의 난이도는 Ai이다.
#
# 캠프에 사용할 문제는 두 문제 이상이어야 한다. 문제가 너무 어려우면 학생들이 멘붕에 빠지고, 문제가 너무 쉬우면 학생들이 실망에 빠지게 된다. 따라서, 문제 난이도의 합은 L보다 크거나 같고, R보다 작거나 같아야 한다. 또, 다양한 문제를 경험해보기 위해 가장 어려운 문제와 가장 쉬운 문제의 난이도 차이는 X보다 크거나 같아야 한다.
#
# 캠프에 사용할 문제를 고르는 방법의 수를 구해보자.
#
# 입력
# 첫째 줄에 N, L, R, X가 주어진다.
#
# 둘째 줄에는 문제의 난이도 A1, A2, ..., AN이 주어진다.
#
# 출력
# 캠프에 사용할 문제를 고르는 방법의 수를 출력한다.
#
# 제한
# 1 ≤ N ≤ 15
# 1 ≤ L ≤ R ≤ 109
# 1 ≤ X ≤ 106
# 1 ≤ Ai ≤ 106
import itertools
n, l, r, x=map(int, input().split())
a=list(map(int, input().split()))
answer=0
case=[]
for i in range(2, n+1):
    case+=list(itertools.combinations(a, i))
for i in range(len(case)):
    if l<=sum(case[i])<=r and max(case[i])-min(case[i])>=x:
        answer+=1
print(answer)
