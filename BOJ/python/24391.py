# 문제
# 해강이는 앙중대학교에 다닌다. 해강이는 이번 학기에 강의코드 1번부터 N번까지 N개의 강의를 듣고 있다.
#
# 모든 강의는 강의코드와 동일한 번호의 건물에서 진행된다. 예를 들어, 강의코드가 1인 강의는 1번 건물에서 진행되고, 강의코드가 N-1인 강의는 N-1번 건물에서 진행된다.
#
# 해강이는 밖에 나오는 것을 싫어해서, 강의 시간표 순서대로 모든 강의를 들으면서 한 건물에서 밖으로 나와서 다른 건물로 이동하는 횟수를 최소화하고 싶다. 앙중대학교에는 다행히도 서로 연결되어 있는 건물들이 있어, 이 건물끼리는 밖으로 나오지 않고 이동할 수 있다.
#
# 해강이의 강의 시간표가 주어질 때, 밖에 나오는 것을 싫어하는 해강이를 위해 최소 몇 번만 밖에 나오면 되는지 구해보자. 맨 처음 강의를 들으러 이동하는 횟수는 세지 않는다.
#
# 입력
# 첫째 줄에 강의의 개수 N(1 ≤ N ≤ 105)과 연결되어 있는 건물의 쌍의 개수 M(0 ≤ M ≤ 105)이 공백으로 구분되어 주어진다.
#
# 두 번째 줄부터는 M줄에 걸쳐 i와 j(1 ≤ i, j ≤ N)가 주어진다. 이는 i번 건물과 j번 건물이 연결되어 있다는 의미이다. 건물이 자기 자신과 연결되거나, 이미 연결된 건물의 쌍이 다시 주어지는 경우는 없다.
#
# 마지막 줄에는 N개의 강의코드 Ai(1 ≤ Ai ≤ N)로 이루어진 강의 시간표가 공백으로 구분되어 주어진다.
#
# 출력
# 해강이가 밖에 나와야 하는 최소 횟수를 출력한다.
n, m = map(int, input().split())
parents = [i for i in range(n+1)]
def find(a):
    if a != parents[a]:
        parents[a] = find(parents[a])
    return parents[a]
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)
path = list(map(int, input().split()))
answer = 0
for i in range(n-1):
    if find(path[i]) != find(path[i+1]):
        answer += 1
print(answer)
