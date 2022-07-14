# 문제
# 오늘은 신승원의 생일이다.
#
# 박승원은 생일을 맞아 신승원에게 인천국제공항을 선물로 줬다.
#
# 공항에는 G개의 게이트가 있으며 각각은 1에서 G까지의 번호를 가지고 있다.
#
# 공항에는 P개의 비행기가 순서대로 도착할 예정이며, 당신은 i번째 비행기를 1번부터 gi (1 ≤ gi ≤ G) 번째 게이트중 하나에 영구적으로 도킹하려 한다. 비행기가 어느 게이트에도 도킹할 수 없다면 공항이 폐쇄되고, 이후 어떤 비행기도 도착할 수 없다.
#
# 신승원은 가장 많은 비행기를 공항에 도킹시켜서 박승원을 행복하게 하고 싶어한다. 승원이는 비행기를 최대 몇 대 도킹시킬 수 있는가?
#
# 입력
# 첫 번째 줄에는 게이트의 수 G (1 ≤ G ≤ 105)가 주어진다.
#
# 두 번째 줄에는 비행기의 수 P (1 ≤ P ≤ 105)가 주어진다.
#
# 이후 P개의 줄에 gi (1 ≤ gi ≤ G) 가 주어진다.
#
# 출력
# 승원이가 도킹시킬 수 있는 최대의 비행기 수를 출력한다.
g = int(input())
p = int(input())
airplane = [int(input()) for _ in range(p)]
parent = [i for i in range(g+1)]
answer = 0
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]
for i in range(p):
    tmp = find(airplane[i])
    if tmp == 0:
        break
    parent[tmp] = parent[tmp-1]
    answer += 1
print(answer)
