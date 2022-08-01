# 문제
# 1부터 N2까지 수가 지그재그 대각선 순서로 N*N 행렬에 채워져 있다. 아래 그림은 N=6일 때, 행렬의 모습이다.
#
# 1	2	6	7	15	16
# 3	5	8	14	17	26
# 4	9	13	18	25	27
# 10	12	19	24	28	33
# 11	20	23	29	32	34
# 21	22	30	31	35	36
# 토끼는 지금 1이 있는 칸에 있다. 토끼는 인접한 칸으로 점프할 수 있다. (위, 아래, 오른쪽, 왼쪽)
#
# 토끼가 점프한 방법이 주어졌을 때, 토끼가 방문한 칸에 있는 수의 합을 구하는 프로그램을 작성하시오. 같은 칸을 여러 번 방문할 경우에도, 방문할 때 마다 더해야 한다. 토끼가 행렬을 벗어나는 경우는 없다.
#
# 입력
# 첫째 줄에 N, K가 주어진다. (1 ≤ N ≤ 100,000, 1 ≤ K ≤ 300,000) N은 행렬의 크기, K는 토끼가 점프한 횟수이다.
#
# 둘째 줄에는 'U','D','L','R'로 이루어진 문자열이 주어진다. 이 문자열의 길이는 K이며, 토끼가 점프한 방향이다.
#
# 출력
# 첫째 줄에, 방문한 칸의 수의 합을 출력한다. 이 값은 32비트 정수를 넘을 수도 있다.
n, k = map(int, input().split())
commands = list(str(input()))
dy, dx = [0, 1, 1, -1], [1, -1, 0, 1]
rdy, rdx = [0, 1, 0, -1], [1, 0, -1, 0]
mapping = {'R': 0, 'D': 1, 'L': 2, 'U': 3}
rabbit = [1, 1]
firsts = [0 for _ in range(n*2)]
firsts[1] = 1
answer = 1
def find_value(idx):
    if idx <= n:
        return idx
    return n-idx%n
def move_rabbit(y, x):
    global answer
    line = y+x-1
    first = firsts[line]
    if line <= n:
        if line%2 == 0:
            answer += (first+y-1)
        else:
            answer += (first+x-1)
    else:
        if line%2 == 0:
            answer += (first+n-x)
        else:
            answer += (first+n-y)
for i in range(2, n*2):
    firsts[i] = firsts[i-1]+find_value(i-1)
for command in commands:
    d = mapping[command]
    rabbit[0] += rdy[d]
    rabbit[1] += rdx[d]
    move_rabbit(rabbit[0], rabbit[1])
print(answer)
