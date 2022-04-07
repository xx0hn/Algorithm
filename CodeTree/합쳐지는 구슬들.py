# 합쳐지는 구슬들
# m개의 구슬이 n*n 격자 안에 놓여져 있고, 격자는 벽으로 둘러쌓여 있습니다. 각 구슬은 상하좌우 중 한 방향으로 이동하고 1초에 한 칸씩 움직입니다. 각 구슬에는 번호가 매겨져 있고, 구슬마다의 무게가 주어져 있습니다. 아래 그림에서 하얀색으로 적혀있는 숫자는 무게를 의미합니다.



# 구슬이 벽에 부딪히면 움직이는 방향이 반대로 뒤집혀 동일한 속도로 움직이는 것을 반복합니다. 이때 방향을 바꾸는 데 역시 1초의 시간이 소요됩니다.



# 또, 아래처럼 칸에서 충돌하는게 아닌 경우는 충돌으로 간주하지 않음에 유의합니다.


# 하지만 만약 1초의 시간이 지난 후 두 개 이상의 구슬이 같은 위치로 오게 된다면 이는 충돌이 발생하게 되고, 충돌이 일어나면 해당 위치에 있던 구슬들은 전부 합쳐지게 됩니다. 이 구슬들이 합쳐지게 되면 하나의 구슬이 만들어지게 되고, 이 구슬의 무게는 해당 위치에 모인 모든 구슬의 합으로 결정되고, 방향은 합쳐진 구슬들 중 가장 큰 번호가 매겨져있는 구슬의 방향을 따르게 되고, 번호는 마찬가지로 충돌이 일어난 구슬들 중 가장 큰 번호를 갖게 됩니다.

# 예를 들어 다음의 경우에 1초의 시간이 흐르게 되면 무게 8을 갖고 번호가 4인 구슬이 오른쪽 방향으로 움직이게 됩니다.



# 처음 주어진 그림을 예로 1초 뒤의 모습을 그려보면 다음과 같습니다.



# 그리고 다시 1초 뒤의 모습을 그려보면 다음과 같습니다.



# 각 구슬의 초기상태가 주어졌을 때, t초가 지난 이후에도 여전히 격자 안에 남아있는 구슬의 개수와 가장 무거운 구슬의 무게를 출력하는 프로그램을 작성해보세요.
# 입력 형식
# 첫 번째 줄에는 격자의 크기를 나타내는 n과 구슬의 개수를 나타내는 m, 시간 t가 각각 공백을 사이에 두고 주어집니다.

# 두 번째 줄 부터는 m개의 줄에 걸쳐 구슬의 정보 (r, c, d, w)가 공백을 사이에 두고 주어집니다. 각 구슬이 r행 c열에서 d방향으로 무게 w를 갖고 이동중이라는 의미이며 d는 위 아래 오른쪽 왼쪽을 의미하는 ‘U', ‘D’, ‘R’, 'L’ 4개의 문자 중 하나가 주어집니다. 번호는 정보가 따로 주어지진 않고 입력된 순서대로 부여됩니다. 즉 첫 번째로 입력된 구슬은 1, i번째로 입력된 구슬은 i입니다. 처음부터 구슬이 겹쳐져 주어지는 경우는 없다고 가정해도 좋습니다. (1 ≤ r ≤ n, 1 ≤ c ≤ n, 1 ≤ w ≤ 100)

# 1 ≤ n ≤ 50

# 1 ≤ m ≤ n * n

# 1 ≤ t ≤ 100

# 출력 형식
# t초 후에도 여전히 남아있는 구슬의 수와 가장 무거운 구슬의 무게를 공백을 사이에 두고 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 4 5 2
# 1 2 L 5
# 2 3 U 2
# 3 1 R 2
# 4 2 U 3
# 3 4 D 5
# 출력:

# 4 5
# 예제2
# 입력:

# 4 5 3
# 1 2 L 5
# 2 3 U 2
# 3 1 R 2
# 4 2 U 3
# 3 4 D 5
# 출력:

# 3 10
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
n, m, t=map(int, input().split())
marbles=[]
mapping={'U': 0, 'R': 1, 'L': 2, 'D': 3}
dy, dx=[-1, 0, 0, 1], [0, 1, -1, 0]
for i in range(1, m+1):
    y, x, d, w=map(str, input().split())
    y, x, w, i=int(y)-1, int(x)-1, int(w), int(i)
    marbles.append((y, x, mapping[d], w, i))
def move(marble):
    y, x, d, w, i=marble
    ny, nx=y+dy[d], x+dx[d]
    if 0<=ny<n and 0<=nx<n:
        return (ny, nx, d, w, i)
    else:
        return (y, x, 3-d, w, i)
def moving():
    for i in range(len(marbles)):
        marbles[i]=move(marbles[i])
def rmv():
    global marbles
    new_marbles=[]
    for i in range(len(marbles)):
        tmp=[(marbles[i][0], marbles[i][1], marbles[i][2], marbles[i][3], marbles[i][4])]
        for j in range(len(marbles)):
            if i==j:
                continue
            if (marbles[i][0], marbles[i][1])==(marbles[j][0], marbles[j][1]):
                tmp.append((marbles[j][0], marbles[j][1], marbles[j][2], marbles[j][3], marbles[j][4]))
        if len(tmp)>1:
            tmp.sort(key=lambda x:(x[4]), reverse=True)
        s=0
        for j in range(len(tmp)):
            s+=tmp[j][3]
        new_marbles.append((tmp[0][0], tmp[0][1], tmp[0][2], s, tmp[0][4]))
    result=[]
    for i in range(len(new_marbles)):
        chk=True
        for j in range(len(result)):
            if (new_marbles[i][0], new_marbles[i][1])==(result[j][0], result[j][1]):
                chk=False
                break
        if chk:
            result.append(new_marbles[i])
    marbles=result
for _ in range(t):
    moving()
    rmv()
marbles.sort(key=lambda x:(x[3]), reverse=True)
print(len(marbles), marbles[0][3])
