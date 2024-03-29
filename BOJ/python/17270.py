# 문제
# 연예인 김영광을 너무 닮아서 길거리에서 매번 사진이 찍히는 지헌이는 사람들에게 노출되는 것을 매우 꺼려한다. 하지만 친구인 성하와 약속을 하면 성하는 매번 늦기 때문에 길거리에 나온 지헌이는 매번 성하를 기다린다. 약속 장소에서 성하에게 전화를 하면 매번 “가는 중” 이라는 대답만 듣고 기다리는 동안 길거리에서 사람들에게 사진을 찍히는 지헌이는 스트레스를 심하게 받고 있다. 참지 못한 지헌이는 성하의 핸드폰을 해킹하여서 항상 어디 있는지 알 수 있게 되었다.
#
# 스트레스가 심해진 지헌이는 성하와의 약속 장소를 바꾸려고 한다. 그 위치는 다음과 같은 조건을 만족해야 한다. 장소의 번호는 1부터 차례대로 붙어 있다.
#
# 지헌이의 출발 위치와 성하의 출발 위치는 새로운 약속 장소가 될 수 없다.
# 성품도 훌륭한 지헌이는 새로운 약속 장소는 지헌이가 걸리는 최단 시간과 성하가 걸리는 최단 시간의 합이 최소가 되도록 하고 싶다.
# 지헌이가 더 늦게 도착하면 성하에게 안좋은 소리를 들을 것이 뻔하기에, 1번과 2번 조건을 만족하는 장소 중에서도 지헌이가 성하보다 늦게 도착하는 곳은 약속 장소가 될 수 없다.
# 위의 세 조건을 모두 만족하는 약속 장소가 여러 곳이 있다면, 그 중에 지헌이로부터 가장 가까운 곳이 최종 약속 장소가 된다. 그런 장소도 여러 곳이 있다면, 그 중에 번호가 가장 작은 장소가 최종 약속 장소가 된다.
#
# 위와 같은 상황이 있다고 했을 때 새로 바꿀 약속 장소를 찾아보자.
#
# (조건 1) 3번과 6번은 지헌이와 성하의 출발지이기 때문에 새로운 약속 장소 후보에서 제외된다.
# (조건 2) 위 상황에서 성하와 지헌의 최단 거리의 합의 최소는 6분이다. 이 때, 조건을 만족하는 약속 장소는 1번, 2번, 5번, 7번이다.
# (조건 3) 5번은 성하가 먼저 도착하여서 기달리고 있기 때문에 지헌이는 꾸중을 들을 위험이 있다. 그래서 5번은 약속 장소 후보에서 제외된다.
# (조건 4) 2번 위치는 성하와 지헌이가 동시에 도착, 7번은 지헌이는 2분 걸려서 도착하고 성하는 4분 걸려서 도착한다. 1번은 지헌이는 1분, 성하는 5분 걸려서 도착한다. 따라서, 지헌이가 원하는 이상적인 약속 장소는 1번이 된다.
# 연예인을 닮아서 고통받는 지헌이를 위해 새로운 약속장소를 찾아주자.
#
# 입력
# 첫 번째 줄에는 약속 장소 후보의 수 V와 약속 장소를 연결하는 총 길의 수 M이 주어진다. (2 ≤ V ≤ 100, 1 ≤ M ≤ 1,000)
#
# 그리고 다음 M개의 각 줄에는 a, b, c 가 주어진다. a, b는 길의 시작과 끝이며 c는 그 길을 지나가는 데 걸리는 시간을 나타낸다.
#
# (1 ≤ a, b ≤ V, c는 10,000이하의 자연수, 길은 양방향이다)
#
# 그리고 그 다음 줄에는 지헌이의 위치 J 와 성하의 위치 S 가 주어진다. (1 ≤ J, S ≤ V)
#
# 지현이와 성하가 항상 만날 수 있는 입력만 주어진다.
#
# 출력
# 연예인을 닮아서 고통받는 지헌이를 위한 이상적인 약속 장소의 위치를 출력한다. 만약 조건을 만족하는 약속 장소가 없다면 -1을 출력하라.
import heapq
v, m = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
j, s = map(int, input().split())
def get_dists(cur):
    hq = []
    heapq.heappush(hq, (0, cur))
    dists = [1e9 for _ in range(v+1)]
    dists[cur] = 0
    while hq:
        dist, cur = heapq.heappop(hq)
        if dist > dists[cur]:
            continue
        for nxt, dst in graph[cur]:
            nxt_dst = dist+dst
            if dists[nxt] > nxt_dst:
                dists[nxt] = nxt_dst
                heapq.heappush(hq, (nxt_dst, nxt))
    return dists
def find_place(j_dists, s_dists):
    new_dists = []
    for i in range(1, v+1):
        if i != j and i != s:
            new_dists.append((j_dists[i], s_dists[i], i))
    new_dists.sort(key=lambda x: (x[0]+x[1], x[0], x[2]))
    return new_dists
j_dists = get_dists(j)
s_dists = get_dists(s)
answer = find_place(j_dists, s_dists)
if not answer or answer[0][0] > answer[0][1]:
    print(-1)
else:
    print(answer[0][2])
