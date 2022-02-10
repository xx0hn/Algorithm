# 문제
# 종강을 맞은 민준이는 고향인 마산으로 내려갈 계획을 짜고 있었다. 늘 그랬듯, 마산으로 갈 버스를 예약하려던 순간 민준이는 집으로 가는 다른 방법이 떠올랐다. 그것은 직접 지도를 보고 고향으로 가는 가장 짧은 길을 찾는 것이다.
#
# 그때, 먼저 고향으로 내려갔던 친구인 건우에게 연락이 왔다. 건우는 고향으로 내려가던 중 알 수 없는 일에 휘말려 외딴곳에 혼자 남겨지게 되었다. 건우는 유일한 구세주인 민준이에게 도움을 청한 것이었다. 그러나 마산의 남자인 민준이에게는 마산이 먼저였다. 민준이는 처량한 건우를 무시한 채 고향으로 떠나려고 했지만, 만약 고향으로 가는 길에 건우가 있다면 겸사겸사 도움을 줄 수 있을 것 같았다.
#
# 지도는 양방향 그래프 형태로 되어있다. 출발지는 1번 정점 마산은 V번 정점이다. 정점은 1~V까지 있다. 건우는 P번 정점에 있다.
# 그리고 항상 1번 정점에서 P번과 V번 정점으로 갈 수 있는 경로가 존재한다.
# 중복되는 간선과 자기 자신을 가리키는 간선은 존재하지 않는다.
#
# 아래와 같은 그래프가 있을 때,
#
#
#
# 위의 경우는 최단 경로가 두 가지 있다.
# 1→3→4→5→6 또는 1→3→5→6 이다. 이것 중에서 건우가 있는 곳, 즉 4번 정점이 포함된 최단 경로가 있으므로 이 경우에는 민준이가 건우를 도울 수 있다.
#
# 민준이가 건우를 도와주는 경로의 길이가 최단 경로의 길이보다 길어지지 않는다면, 민준이는 반드시 건우를 도와주러 간다.
#
# 어쩌면 지킬 수도 있는 민준이의 우정을 위해 우리가 도와주자!
#
# 입력
# 입력의 첫 번째 줄에 정점의 개수 V와 간선의 개수 E, 그리고 건우가 위치한 정점 P가 주어진다. (2 ≤ V  ≤ 5,000, 1 ≤ E ≤ 10,000, 1 ≤ P  ≤ V)
#
# 두 번째 줄부터 E개의 줄에 걸쳐 각 간선의 정보 a,b,c가 공백으로 구분되어 주어진다. 이는 a번 정점과 b번 정점 사이의 거리가 c임을 의미한다. (1 ≤ a,b ≤ V, 1 ≤ c  ≤ 10,000)
#
# 출력
# 민준이가 찾은 최단 경로 위에 건우가 있다면 "SAVE HIM" 을 아니면 "GOOD BYE" 를 출력한다.
import sys
import heapq
v, e, p=map(int, input().split())
graph=[[] for _ in range(v+1)]
for _ in range(e):
    a, b, c=map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
INF=sys.maxsize
def dijkstra(start, end):
    dist=[INF for _ in range(v+1)]
    dist[start]=0
    q=[]
    heapq.heappush(q, (0, start))
    while q:
        distance, cur=heapq.heappop(q)
        if distance>dist[cur]:
            continue
        for nxt, dst in graph[cur]:
            nxt_distance=distance+dst
            if nxt_distance<dist[nxt]:
                dist[nxt]=nxt_distance
                heapq.heappush(q, (nxt_distance, nxt))
    return dist[end]
if dijkstra(1, v)==dijkstra(1, p)+dijkstra(p, v):
    print('SAVE HIM')
else:
    print('GOOD BYE')
