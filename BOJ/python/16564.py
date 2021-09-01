#  히오스 프로게이머

#  준석이는 Heroes of the Storm 프로게이머 지망생이다.

#  이 게임에는 총 N개의 캐릭터가 있다. 그리고 현재 각 캐릭터의 레벨은 Xi이다. 성권이는 앞으로 게임이 끝날 때까지, 레벨을 최대 총합 K만큼 올릴 수 있다.

#  팀 목표레벨 T =min(Xi) (1 ≤ i ≤ N)라고 정의하면, 게임이 끝날 때까지 성권이가 달성할 수 있는 최대 팀 목표레벨 T는 무엇인가?

#  예를 들어, N = 3, X1= 10, X2= 20, X3= 15이고 K = 10일 때, X1을 7만큼 올리고 X3을 2만큼 올리면 최소 레벨 Xi는 17이 된다. 따라서 팀 목표레벨 T는 17이다.

#  이 경우처럼 레벨을 총합 K보다 적게 올릴 수도 있다.

#  #######입력#######

#  첫째 줄에는 캐릭터의 개수 N, 올릴 수 있는 레벨 총합 K가 주어진다. (1 ≤ N ≤1,000,000, 1 ≤ K ≤ 1,000,000,000)

#  다음 N개의 줄에는 현재 각 캐릭터의 레벨이 X1, X2, X3, ... , Xn 으로 주어진다. (1 ≤ Xi ≤ 1,000,000,000)

#  #######출력#######

#  가능한 최대 팀 목표레벨 T를 출력한다.

#  제한시간: 1초
import sys

n, k=map(int, sys.stdin.readline().split())
x = []
result=0
x=sorted([int(sys.stdin.readline())for _ in range(n)])

front=x[0]
back=x[0]+k
while front<=back:
    mid=(front+back)//2
    cnt=0
    for i in range(n):
        if mid>x[i]:
            cnt=cnt+mid-x[i]
        else:
            break
    if cnt>k:
        back=mid-1
    else:
        result=mid
        front=mid+1

print(result)
