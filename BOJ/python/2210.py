# 문제
# 5×5 크기의 숫자판이 있다. 각각의 칸에는 숫자(digit, 0부터 9까지)가 적혀 있다. 이 숫자판의 임의의 위치에서 시작해서, 인접해 있는 네 방향으로 다섯 번 이동하면서, 각 칸에 적혀있는 숫자를 차례로 붙이면 6자리의 수가 된다. 이동을 할 때에는 한 번 거쳤던 칸을 다시 거쳐도 되며, 0으로 시작하는 000123과 같은 수로 만들 수 있다.
#
# 숫자판이 주어졌을 때, 만들 수 있는 서로 다른 여섯 자리의 수들의 개수를 구하는 프로그램을 작성하시오.
#
# 입력
# 다섯 개의 줄에 다섯 개의 정수로 숫자판이 주어진다.
#
# 출력
# 첫째 줄에 만들 수 있는 수들의 개수를 출력한다.
import sys
sys.setrecursionlimit(10**9)
def dfs(h, w, tmp):
    if len(tmp)==6:
        if tmp not in nums:
            nums.append(tmp)
        return
    dh = [0, 0, 1, -1]
    dw = [1, -1, 0, 0]
    for i in range(4):
        next_h=h+dh[i]
        next_w=w+dw[i]
        if next_h>=0 and next_w>=0 and next_h<5 and next_w<5:
            dfs(next_h, next_w, tmp+pad[next_h][next_w])
pad=[]
for _ in range(5):
    pad.append(list(map(str, input().split())))
nums=[]
for i in range(5):
    for j in range(5):
        dfs(i, j, pad[i][j])
print(len(nums))
