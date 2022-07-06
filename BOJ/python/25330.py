# 문제
# 올 여름 출시된 RPG 게임 "SHOW ME THE DUNGEON"은 주인공 시루가 몬스터에게 침략당한 마을을 구하는 내용의 게임이다. 배경이 되는 나라는 $0, 1, 2, \cdots, N$번의 번호가 붙어있는 $N+1$개의 마을로 이루어져 있다. $0$번 마을과 $1, 2, \cdots, N$번 마을을 오갈 수 있는 도로가 존재하고 이 밖의 도로는 존재하지 않는다. 즉, $N$개의 도로가 존재한다.
#
# 게임이 시작하면 시루는 $0$번 마을에 위치하게 되며, $0$번 마을을 제외한 $1, 2, \cdots, N$번 마을에는 몬스터가 각각 한 마리씩 있다. 시루는 마을을 방문할 때 도로를 통해 이동하며, 어떤 마을에서 다른 마을로 이동하기 위해서는 $0$번 마을을 거쳐야만 한다. 시루는 몇 개의 마을을 선택해 적당한 순서로 방문해 몬스터와 싸울 것이다.
#
#  $i$번째 마을에 있는 몬스터의 공격력은 $A_i$이고 해당 마을에 $P_i$명의 주민이 있다. 시루는 어떤 마을을 방문하면 몬스터와 싸운 다음 마을에 있는 주민을 해방시킨다. 시루의 초기 체력은 $K$이고, 마을 $i$를 방문하기 전에 마을 $t_1, t_2, \cdots, t_k$를 방문했다면, 마을 $i$에서 몬스터와 싸울 때 $A_{t_1} + A_{t_2} + \cdots + A_{t_k} + A_i$만큼의 체력을 소모한다. 시루의 체력이 $0$보다 작아지는 경우, 주민을 해방시키지 못하고 게임이 종료된다.
#
# 모든 마을의 주민을 해방시키는 것은 불가능할 수 있기 때문에, 시루는 체력을 최대 $K$만큼만 소모하면서 최대한 많은 주민을 해방시키려고 한다. 시루가 해방시킬 수 있는 주민들의 최대 수를 구해보자.
#
# 입력
# 첫째 줄에 몬스터의 수 $N$과 시루의 초기 체력 $K$가 공백으로 구분되어 주어진다.
#
# 둘째 줄에 각 마을에 있는 몬스터의 공격력 $A_1, A_2, \cdots, A_N$이 공백으로 구분되어 주어진다.
#
# 셋째 줄에 각 마을에 있는 주민의 수 $P_1, P_2, \cdots, P_N$이 공백으로 구분되어 주어진다.
#
# 입력으로 주어지는 모든 값은 정수이다.
#
# 출력
# 시루가 해방시킬 수 있는 주민들의 최대 수를 출력한다. 만약 주민을 해방시킬 수 없다면 0을 출력한다.
#
# 제한
#  $1 \leq N \leq 20$ 
#  $1 \leq K \leq 100\,000$ 
#  $1 \leq A_i \leq 100\,000$ 
#  $1 \leq P_i \leq 100\,000$ 
n, k = map(int, input().split())
a = list(map(int, input().split()))
p = list(map(int, input().split()))
answer = 0
def save_citizen(cur, damage, citizen, path):
    global answer
    if damage <= k:
        answer = max(answer, citizen)
    if damage > k:
        return
    for i in range(n):
        if cur == i or i in set(path):
            continue
        new_damage = damage + sum([a[d] for d in path]) + a[i]
        save_citizen(i, new_damage, citizen+p[i], path+[i])
save_citizen(-1, 0, 0, [])
print(answer)
