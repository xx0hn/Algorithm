# 문제
# 백준이는 국방의 의무를 수행하기 위해 떠났다. 혹독한 훈련을 무사히 마치고 나서, 정말 잘 생겼고 코딩도 잘하는 백준은 그 특기를 살려 적군의 진영을 수학적으로 분석하는 일을 맡게 되었다.
#
# 2차원 평면 위의 N곳에 적군의 진영이 설치되어 있다. 각 적군의 진영들은 진영마다 하나의 통신탑을 설치해, i번째 적군의 통신탑은 설치 위치로부터 Ri 이내 거리에 포함되는 모든 지역을 자신의 통신영역 Ai로 가지게 된다. 만약 임의의 통신영역 Ai와 Aj가 닿거나 겹치는 부분이 있다면 진영 i와 진영 j는 직접적으로 통신이 가능하다. 물론 직접적으로 통신이 가능하지 않더라도, 임의의 지역 i와 j가 중간에 몇 개의 직접통신을 거쳐서 최종적으로 통신이 가능하다면 i와 j는 상호간에 통신이 가능한 것으로 본다.
#
# 적들은 영리해서, 상호간에 통신이 가능한 부대끼리는 결집력있는 한 그룹처럼 행동한다. 백준은 이러한 그룹의 개수를 알아내 아군의 전략지침에 도움을 주고자 한다. 군대에 가서도 코딩하는 불쌍한 백준을 위해 적군의 통신망 분석을 도와주자!
#
# 입력
# 입력 파일의 첫 번째 줄에 테스트 케이스의 수를 의미하는 자연수 T가 주어진다. 그 다음에는 T개의 테스트 케이스가 주어진다.
#
# 각각의 테스트 케이스에 대해서 적군 진영의 숫자 N (1 ≤ N ≤ 3,000)이 주어진다. 이어서 N줄에 걸쳐 적군 진영의 좌표 x, y (0 ≤ x, y ≤ 5,000), 그리고 해당 진영의 R (0 ≤ R ≤ 5,000)이 주어진다. 주어지는 수는 모두 정수이다.
#
# 출력
# 각 테스트 케이스에 대해서 한 줄에 걸쳐 적군 진영의 그룹 개수를 출력한다.
import sys
input = sys.stdin.readline
def distance(a, b):
    return (a[0]-b[0])**2+(a[1]-b[1])**2

def dfs(cur):
    for j in range(n):
        if distance(location[cur], location[j])>(location[cur][2]+location[j][2])**2 or cur==j or visited[j]:
            continue
        visited[j]=True
        dfs(j)
t=int(input())
for _ in range(t):
    n=int(input())
    answer=0
    location=[]
    visited=[False for _ in range(n)]
    for _ in range(n):
        location.append(list(map(int, input().split())))
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer+=1
    print(answer)
