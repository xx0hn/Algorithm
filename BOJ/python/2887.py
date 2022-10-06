# 문제
# 때는 2040년, 이민혁은 우주에 자신만의 왕국을 만들었다. 왕국은 N개의 행성으로 이루어져 있다. 민혁이는 이 행성을 효율적으로 지배하기 위해서 행성을 연결하는 터널을 만들려고 한다.
#
# 행성은 3차원 좌표위의 한 점으로 생각하면 된다. 두 행성 A(xA, yA, zA)와 B(xB, yB, zB)를 터널로 연결할 때 드는 비용은 min(|xA-xB|, |yA-yB|, |zA-zB|)이다.
#
# 민혁이는 터널을 총 N-1개 건설해서 모든 행성이 서로 연결되게 하려고 한다. 이때, 모든 행성을 터널로 연결하는데 필요한 최소 비용을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 행성의 개수 N이 주어진다. (1 ≤ N ≤ 100,000) 다음 N개 줄에는 각 행성의 x, y, z좌표가 주어진다. 좌표는 -109보다 크거나 같고, 109보다 작거나 같은 정수이다. 한 위치에 행성이 두 개 이상 있는 경우는 없다.
#
# 출력
# 첫째 줄에 모든 행성을 터널로 연결하는데 필요한 최소 비용을 출력한다.
def find(a):
    if a != parents[a]:
        parents[a] = find(parents[a])
    return parents[a]
def union(a, b):
    a = find(a)
    b = find(b)
    parents[b] = a
n = int(input())
zs, ys, xs = [], [], []
for i in range(n):
    z, y, x = map(int, input().split())
    zs.append((z, i))
    ys.append((y, i))
    xs.append((x, i))
zs.sort()
ys.sort()
xs.sort()
tmp = []
parents = [i for i in range(n+1)]
for idx in zs, ys, xs:
    for i in range(1, n):
        cost1, a = idx[i-1]
        cost2, b = idx[i]
        tmp.append((a, b, abs(cost1-cost2)))
tmp.sort(key=lambda x:x[2], reverse=True)
answer = 0
cnt = n-1
while cnt:
    a, b, cost = tmp.pop()
    if find(a) == find(b):
        continue
    union(a, b)
    cnt -= 1
    answer += cost
print(answer)
