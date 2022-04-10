# 단순한 동전 챙기기
# ‘.’ (빈 공간), ‘S’ (시작점), ‘E' (도착점) 그리고 ‘1'에서 '9’ 사이의 숫자로 이루어진 N * N 격자 정보가 주어집니다. 숫자가 써져 있으면 해당 위치에 동전이 놓여져 있음을 뜻하고, 각 숫자는 해당 동전의 번호를 의미합니다. 동전은 해당 위치에 도달해야 얻을 수 있으며, 동전은 각 위치에 최대 하나씩만 놓여져 있기 때문에 같은 위치에서 2개 이상의 동전을 얻을 수는 없습니다. 이때, 시작점에서 출발하여 적절하게 이동하여 최소 3개의 동전을 수집하여 도착점으로 도달하려고 합니다. 동전을 수집할 시에는 꼭 번호가 증가하는 순서대로 수집해야만 합니다. 또, 해당 위치를 지나가더라도 동전을 수집하지 않아도 되며 같은 위치를 2번 이상 지나가는 것 역시 허용됩니다.

# 다음 그림을 예로 들어봅시다.



# 1 → 4-> 5 순서로 동전을 주워 도착점으로 가게 되는 경우 최소 12번의 이동을 통해 도착점에 도달하게 됩니다.



# 하지만 1 → 2 → 3 순서로 동전을 주워 도착점으로 가게 되는 경우 8번의 이동 만으로도 도착점에 도달할 수 있게 됩니다.



# N * N 크기의 격자 상태가 주어졌을 때 동전의 숫자가 증가하는 순서대로 최소 3개의 동전을 수집해 도착지에 도달하기 위해 필요한 최소 이동 횟수를 구하는 프로그램을 작성해보세요.

# 입력 형식
# 첫째 줄에는 격자의 크기를 나타내는 N이 주어집니다.

# 그 다음 줄 부터는 N개의 줄에 걸쳐 격자의 정보가 주어집니다. 각 줄마다 해당 행의 정보가 주어지며, 이 정보는 ‘.’ (빈 공간), ‘S’ (시작점), ‘E' (도착점) 그리고 ‘1'에서 '9’ 사이의 숫자로 이루어진 길이가 N인 문자열로 이루어져 있으며, 공백없이 주어집니다. 시작점과 도착점은 단 하나씩만 주어짐을 가정해도 좋으며, 같은 숫자를 지닌 동전은 주어지지 않습니다.

# 2 ≤ N ≤ 20
# 출력 형식
# 시작점에서 출발하여 동전의 숫자가 증가하는 순서대로 최소 3개의 동전을 수집해 도착지에 도달하기 위해 필요한 최소 이동 횟수를 출력합니다. 만약 불가능하다면 -1을 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 4
# ..3.
# 2..E
# .1..
# 5S.4
# 출력:

# 8
# 예제2
# 입력:

# 4
# ..3.
# ...E
# .1..
# .S..
# 출력:

# -1
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
import collections
import sys
n=int(input())
grid=[str(input()) for _ in range(n)]
coins=collections.defaultdict(list)
coins_lst=[]
s, e=[], []
for i in range(n):
    for j in range(n):
        if grid[i][j]=='S':
            s=[i, j]
        if grid[i][j]=='E':
            e=[i, j]
        if grid[i][j].isdigit():
            coins[grid[i][j]]=[i, j]
            coins_lst.append(grid[i][j])
coins_lst.sort()
def get_dist(y1, x1, y2, x2):
    return abs(y1-y2)+abs(x1-x2)
path=[]
answer=sys.maxsize
def get_path(cur, cnt):
    global answer
    if cur==len(coins_lst):
        if cnt==3:
            dist=get_dist(s[0], s[1], coins[path[0]][0], coins[path[0]][1])
            for i in range(2):
                dist+=get_dist(coins[path[i]][0], coins[path[i]][1], coins[path[i+1]][0], coins[path[i+1]][1])
            dist+=get_dist(coins[path[2]][0], coins[path[2]][1], e[0], e[1])
            answer=min(answer, dist)
        return
    path.append(coins_lst[cur])
    get_path(cur+1, cnt+1)
    path.pop()
    get_path(cur+1, cnt)
get_path(0, 0)
if answer==sys.maxsize:
    print(-1)
else:
    print(answer)
