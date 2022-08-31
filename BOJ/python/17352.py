# 문제
# 선린월드에는 N개의 섬이 있다. 섬에는 1, 2, ..., N의 번호가 하나씩 붙어 있다. 그 섬들을 N - 1개의 다리가 잇고 있으며, 어떤 두 섬 사이든 다리로 왕복할 수 있다.
#
# 어제까지는 그랬다.
#
# "왜 다리가 N - 1개밖에 없냐, 통행하기 불편하다"며 선린월드에 불만을 갖던 욱제가 다리 하나를 무너뜨렸다! 안 그래도 불편한 통행이 더 불편해졌다. 서로 왕복할 수 없는 섬들이 생겼기 때문이다. 일단 급한 대로 정부는 선린월드의 건축가를 고용해, 서로 다른 두 섬을 다리로 이어서 다시 어떤 두 섬 사이든 왕복할 수 있게 하라는 지시를 내렸다.
#
# 그런데 그 건축가가 당신이다! 안 그래도 천하제일 코딩대회에 참가하느라 바쁜데...
#
# 입력
# 첫 줄에 정수 N이 주어진다. (2 ≤ N ≤ 300,000)
#
# 그 다음 N - 2개의 줄에는 욱제가 무너뜨리지 않은 다리들이 잇는 두 섬의 번호가 주어진다.
#
# 출력
# 다리로 이을 두 섬의 번호를 출력한다. 여러 가지 방법이 있을 경우 그 중 아무거나 한 방법만 출력한다.
def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
n = int(input())
parent = [i for i in range(n+1)]
for _ in range(n-2):
    a, b = map(int, input().split())
    union(a, b)
for i in range(1, n+1):
    for j in range(1, n+1):
        if find(i) != find(j):
            print(i, j)
            quit()
