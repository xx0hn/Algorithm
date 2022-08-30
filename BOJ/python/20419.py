# 문제
# 입력 제한 외 난이도에 따른 문제의 차이는 없다.
#
# 민규는 25년간의 외로운 수련 끝에 드디어 마법사가 되었다. 마법사가 된 민규에게는 꿈이 있었으니.. 마법같이 멋진 테마파크를 짓는 것이었다! 민규는 테마파크의 첫 상품으로 "화살표 미로"를 공개했다.
#
# 화살표 미로는 평범한 미로와 다른 점이 많다. 이 미로는 R×C 개의 방으로 이루어져 있다. 모든 방이 서로 이동할 수 없도록 사방이 벽으로 막혀있고, 각 방마다 완전히 다른 테마의 화려한 볼거리로 꾸며져 있다.
#
# 화살표 미로 지도
#
# <그림 1> 화살표 미로의 지도 (예제1)
#
# 사방이 벽으로 막혀있다면 어떻게 다른 방으로 이동할 수 있을까? 민규는 각 방마다 특별한 마법진을 그려 각 마법진에 그려져 있는 화살표의 방향으로 한 칸 순간이동 할 수 있도록 설계했다! 미로의 가장 바깥벽은 마그마로 둘러싸여 있어, 미로를 둘러싸고 있는 가장 바깥벽을 넘어가 미로 자체를 탈출하지는 못한다.
#
# 화살표 미로를 이용하는 고객들은 미로의 가장 왼쪽 위인 (1,1)방에 있는 입구에서 시작해 다양한 방들을 경험하고, 미로의 가장 오른쪽 아래인 (R,C)방에 있는 출구를 끝으로 미로를 마쳐야한다. 만약 그러지 못한다면 영원히 화살표 미로를 헤매게 될 것이다! 당연하지만, 처음 민규가 그려둔 마법진의 화살표 방향에 따라 출구에 가지 못할 수 있다.
#
# 민규는 화살표 미로를 사람들이 안전하게 즐길 수 있도록 화살표 미로의 입구에서 특별한 주문서를 팔기로 했다. 주문서는 화살표를 반시계 방향으로 회전시키는 'L 주문서'와 시계 방향으로 회전시키는 'R 주문서' 두 종류가 있다. 이 주문서를 사용하면 해당 방향으로 화살표가 90도 회전하게 된다. 몇 장의 주문서를 한 마법진에 연달아 사용해 180도, 270도 회전하도록 만들 수도 있다. 민규는 수익을 극대화 하기 위해 L 주문서와 R 주문서를 각각 한 장씩 묶어 한 세트로만 팔고 있다.
#
# 화살표 미로를 이용하는 고객들은 미로에 입장하고서야 지도를 받을 수 있어, 화살표 미로에서 영원히 헤매지 않으려면 울며 겨자 먹기로 대량의 주문서 세트를 구매해야만 했다. 화살표 미로를 즐겨 이용하던 민규의 친구 준서도 이런 불편을 겪고 있었다.
#
# 준서 : 아니, 적어도 지금 가진 걸론 충분한지 아닌지는 말해 줘야 하는 거 아니야 ??
#
# 준서의 불평에 지친 민규는 특별히 준서에게만, 준서가 가지고 있는 주문서 세트로 출구까지 가는 데 충분하냐는 질문에 단 한 번 "Yes" 또는 "No"로 대답해주기로 했다. 정확하게 답해주는 것은 민규에게 매우 어려운 일이기 때문에, 민규는 당신에게 질문에 대신 답해주는 프로그램을 의뢰했다.
#
# 입력
# 첫번째 줄에는 미로의 행 R, 열 C, 준서가 가진 주문서 세트의 개수 K가 주어진다.
#
# 두번째 줄부터 R줄에 걸쳐 화살표 미로의 지도가 입력된다. 각 줄마다 "UDLR"로만 이루어진 길이 C의 문자열이 입력되며, U는 위, D는 아래, L은 왼쪽, R은 오른쪽으로 이동 가능한 마법진을 뜻한다.
#
# 출력
# 준서의 질문에 대한 답을 "Yes" 또는 "No"로 출력한다.
import heapq
r, c, k = map(int, input().split())
grid = [list(str(input())) for _ in range(r)]
dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]
mapping = {'U': 0, 'L': 1, 'D': 2, 'R': 3}
def move():
    q = []
    heapq.heappush(q, (0, 0, 0, 0, 0))
    costs = [[1e9 for _ in range(c)] for _ in range(r)]
    costs[0][0] = 0
    while q:
        cost, l_cost, r_cost, y, x = heapq.heappop(q)
        if cost > costs[y][x]:
            continue
        if cost > k:
            continue
        l_cur = mapping[grid[y][x]]
        r_cur = mapping[grid[y][x]]
        tmp_l_cost = l_cost
        tmp_r_cost = r_cost
        while tmp_l_cost+1 <= k:
            l_cur = (l_cur+1)%4
            tmp_l_cost += 1
            ny, nx = y+dy[l_cur], x+dx[l_cur]
            if 0 <= ny < r and 0 <= nx < c:
                if costs[ny][nx] > max(tmp_l_cost, r_cost):
                    costs[ny][nx] = max(tmp_l_cost, r_cost)
                    heapq.heappush(q, (max(tmp_l_cost, r_cost), tmp_l_cost, r_cost, ny, nx))
        while tmp_r_cost+1 <= k:
            r_cur = (r_cur+3)%4
            tmp_r_cost += 1
            ny, nx = y + dy[r_cur], x + dx[r_cur]
            if 0 <= ny < r and 0 <= nx < c:
                if costs[ny][nx] > max(tmp_r_cost, l_cost):
                    costs[ny][nx] = max(tmp_r_cost, l_cost)
                    heapq.heappush(q, (max(tmp_r_cost, l_cost), l_cost, tmp_r_cost, ny, nx))
        ny, nx = y+dy[mapping[grid[y][x]]], x+dx[mapping[grid[y][x]]]
        if 0 <= ny < r and 0 <= nx < c:
            if costs[ny][nx] > cost:
                costs[ny][nx] = cost
                heapq.heappush(q, (cost, l_cost, r_cost, ny, nx))
    return costs
ans = move()
if ans[r-1][c-1] == 1e9:
    print('No')
else:
    print('Yes')
