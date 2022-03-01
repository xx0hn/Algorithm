# 문제
# 길이가 $N$인 수열 $A_1 \ A_2 \ \cdots \ A_N$이 주어진다. $1\le i \le N$인 정수 $i$마다 $i < j \le N$이고 $A_i \ne A_j$인 정수 $j$중 최솟값을 출력하라. 만약 이러한 $j$가 없다면 $-1$을 출력하라.
#
# 입력
# 첫째 줄에 수열 $A$의 크기 $N$이 주어진다. 둘째 줄에는 $A_1 \ A_2 \ \cdots \ A_N$이 공백으로 구분되어 주어진다. $(1 \le N \le 10^6$, $-10^9 \le A_i \le 10^9 )$ 
#
# 입력으로 주어지는 모든 수는 정수이다.
#
# 출력
# 각 $i$마다 조건을 만족하는 최솟값 $j$를 출력하라. 만약 이러한 $j$가 없다면 $-1$을 출력하라.
import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int, input().split()))
answer=[]
p1, p2=0, 1
while p1<=p2:
    if p1==n-1:
        break
    if arr[p1]!=arr[p2]:
        answer+=[p2+1]*(p2-p1)
        p1=p2
        p2+=1
    elif p2==n-1 and arr[p1]==arr[p2]:
        answer+=[-1]*(p2-p1)
        break
    elif arr[p1]==arr[p2]:
        p2+=1
answer.append(-1)
print(*answer)
