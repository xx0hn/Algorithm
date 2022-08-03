# 문제
# KOI 본선 대회에 N명의 학생이 참가했다. 이 학생들을 각각 1부터 N까지 정수로 표현하자. 대회가 끝나고 성적을 발표하는데, 이 대회는 전체 학생의 등수를 발표 하는 대신, 두 학생 A, B가 대회 본부에 찾아가면 본부는 두 학생 중 어느 학생이 더 잘 했는지를 알려준다. 둘 이상의 학생이 동점인 경우는 없다.
#
# 자신의 전체에서 등수가 궁금한 학생들은 둘 씩 짝을 지어서 대회 본부에 총 M번 질문을 했다. 여러분은 등수를 알고 싶은 학생 X와 대회 본부의 질문에 대한 답들 로부터 이 학생 X의 등수 범위를 찾아서 출력한다. 질문에 대한 답으로 알 수 있는 최대한 정확한 답을 출력한다.
#
# 입력
# 표준 입력으로 다음 정보가 주어진다. 첫 번째 줄에 세 정수 N, M, X가 공백을 사이에 두고 주어진다. (2 ≤ N ≤ 105, 1 ≤ M ≤ min(N(N-1)/2, 5×105), 1 ≤ X ≤ N) . 다음 M 줄에는 각각 두 정수 A, B가 주어지는데, 이 뜻은 학생 A가 학생 B보다 더 잘했다는 뜻이다. 같은 A, B가 둘 이상의 줄에 주어지는 경우는 없고, 입력된 값이 정확함이 보장된다.
#
# 출력
# 표준 출력으로 두 정수 U, V (1 ≤ U ≤ V ≤ N)를 출력한다. 이는 학생 X의 가능한 가장 높은 등수가 U, 가능한 가장 낮은 등수가 V임을 나타낸다. 만약 학생 X의 가능한 등수가 정확하게 하나라면, U = V이다.
#
# 서브태스크
# 번호	배점	제한
# 1	12
# N ≤ 10
#
# 2	11
# N ≤ 1,000, M = N(N-1)/2
#
# 3	34
# N ≤ 1,000
#
# 4	43
# 원래의 제약조건 이외에 아무 제약조건이 없다.
from collections import deque
n, m, x = map(int, input().split())
win = [[] for _ in range(n+1)]
lose = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    win[a].append(b)
    lose[b].append(a)
def find_rank():
    q = deque()
    q.append(x)
    visited = [False for _ in range(n+1)]
    visited[x] = True
    w_cnt = 0
    l_cnt = 0
    while q:
        cur = q.popleft()
        for nxt in win[cur]:
            if not visited[nxt]:
                w_cnt += 1
                visited[nxt] = True
                q.append(nxt)
    visited = [False for _ in range(n+1)]
    visited[x] = True
    q.append(x)
    while q:
        cur = q.popleft()
        for nxt in lose[cur]:
            if not visited[nxt]:
                l_cnt += 1
                visited[nxt] = True
                q.append(nxt)
    return w_cnt, l_cnt
w_cnt, l_cnt = find_rank()
best = 1+l_cnt
worst = n-w_cnt
print(best, worst)
