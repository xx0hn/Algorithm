# 문제
# n×m 크기의 체스 판과, 상대팀의 Queen, Knight, Pawn의 위치가 주어져 있을 때, 안전한 칸이 몇 칸인지 세는 프로그램을 작성하시오. (안전한 칸이란 말은 그 곳에 자신의 말이 있어도 잡힐 가능성이 없다는 것이다.)
#
# 참고로 Queen은 가로, 세로, 대각선으로 갈 수 있는 만큼 최대한 많이 이동을 할 수 있는데 만약 그 중간에 장애물이 있다면 이동을 할 수 없다. 그리고 Knight는 2×3 직사각형을 그렸을 때, 반대쪽 꼭짓점으로 이동을 할 수 있다. 아래 그림과 같은 8칸이 이에 해당한다.
#
#
#
# 이때 Knight는 중간에 장애물이 있더라도 이동을 할 수 있다. 그리고 Pawn은 상대팀의 말은 잡을 수 없다고 하자(즉, 장애물의 역할만 한다는 것이다).
#
# 예를 들어 다음과 같이 말이 배치가 되어 있다면 진하게 표시된 부분이 안전한 칸이 될 것이다. (K : Knight, Q : Queen, P : Pawn)
#
#
#
# 입력
# 첫째 줄에는 체스 판의 크기 n과 m이 주어진다. (1 ≤ n, m ≤ 1000) 그리고 둘째 줄에는 Queen의 개수와 그 개수만큼의 Queen의 위치가 입력된다. 그리고 마찬가지로 셋째 줄에는 Knight의 개수와 위치, 넷째 줄에는 Pawn의 개수와 위치가 입력된다. 즉 둘째 줄, 셋째 줄, 넷째 줄은  k, r1, c1, r2, c2, ..., rk, ck 이 빈 칸을 사이에 두고 주어진다는 것이다. 여기서 ri는 i번째 말의 행 위치, ci는 i번째 말의 열 위치를 의미한다. 한 칸에는 하나의 말만 놓인다고 가정한다. Knight, Queen, Pawn의 개수는 각각 100을 넘지 않는 음이 아닌 정수이다.
#
# 출력
# 첫째 줄에 n×m 체스판에 안전한 칸이 몇 칸인지 출력하시오.
n, m=map(int, input().split())
q_info=list(map(int, input().split()))
k_info=list(map(int, input().split()))
p_info=list(map(int, input().split()))
q_info, k_info, p_info=q_info[1:], k_info[1:], p_info[1:]
grid=[['' for _ in range(m)] for _ in range(n)]
qdy, qdx=[0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]
kdy, kdx=[-1, 1, 2, 2, -1, 1, -2, -2], [2, 2, 1, -1, -2, -2, -1, 1]
mxln=max(n, m)
chk=[[0 for _ in range(m)] for _ in range(n)]
for i in range(len(q_info)):
    if i%2==0:
        grid[q_info[i]-1][q_info[i+1]-1]='Q'

for i in range(len(k_info)):
    if i%2==0:
        grid[k_info[i]-1][k_info[i+1]-1]='K'
for i in range(len(p_info)):
    if i%2==0:
        grid[p_info[i]-1][p_info[i+1]-1]='P'
for i in range(n):
    for j in range(m):
        if grid[i][j]=='Q':
            chk[i][j]+=1
            for d in range(8):
                for ln in range(1, mxln):
                    ni, nj=i+(ln*qdy[d]), j+(ln*qdx[d])
                    if not (0<=ni<n and 0<=nj<m) or grid[ni][nj]!='':
                        break
                    chk[ni][nj]+=1
        if grid[i][j]=='K':
            chk[i][j]+=1
            for d in range(8):
                ni, nj=i+kdy[d], j+kdx[d]
                if 0<=ni<n and 0<=nj<m and grid[ni][nj]=='':
                    chk[ni][nj]+=1
        if grid[i][j]=='P':
            chk[i][j]+=1
answer=0
for i in range(n):
    for j in range(m):
        if chk[i][j]==0:
            answer+=1
print(answer)
