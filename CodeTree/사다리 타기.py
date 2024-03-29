# 사다리 타기
# 사다리 타기 게임은 사람 수(n) 만큼 세로줄을 긋고 위쪽 편에는 1부터 n까지의 숫자를 순서대로 적은 다음, 몇몇 인접한 세로줄 사이에 가로줄(m)을 서로 겹치지 않게 긋고 위쪽에 있는 각 숫자에서 부터 시작하여 내려가다가 교점을 만날 때마다 90도로 방향을 꺾다 끝에 도착하게 되면 해당 숫자를 적는 게임입니다. 이 게임에서는 가로줄끼리 서로 맞닿아 있는 경우가 없다고 가정해도 좋습니다.

# 예를 들어 n이 4, m이 6이고 다음과 같이 가로줄이 주어졌을 때의 결과는 3, 4, 1, 2가 됩니다.



# 하지만 주어진 가로줄 중 다음과 같이 4개의 가로줄 만 갖고 사다리 게임을 진행해도 처음 주어진 사다리와 동일한 결과를 얻을 수 있습니다.



# 세로줄의 수 n과 m개의 가로줄의 상태가 주어졌을 때, 사용한 가로줄을 적절하게 선택해 모든 가로줄을 이용했을 때의 결과와 동일하게 되도록 하는 최소 가로줄의 수를 구하는 프로그램을 작성해보세요.

# 입력 형식
# 첫 번째 줄에는 세로줄의 수 n과 가로줄의 수 m이 공백을 사이에 두고 주어집니다.

# 그 다음 줄부터는 m개의 줄에 걸쳐 각 가로줄의 상태 (a, b)가 공백을 사이에 두고 주어집니다. 해당 가로줄은 왼쪽에서부터 a번째 세로줄과 a+1번째 세로줄을 연결하며, 위에서부터 b번째 위치에 가로줄이 그어짐을 나타냅니다. 가로줄이 겹쳐 주어지는 경우는 없다고 가정해도 좋습니다. (1 ≤ a < n, 1 ≤ b ≤ 15)

# 2 ≤ n ≤ 11

# 1 ≤ m ≤ 15

# 출력 형식
# 처음 상황에서의 결과와 동일한 결과를 얻기 위해 필요한 최소 가로줄의 수를 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 4 6
# 1 1
# 1 3
# 2 2
# 2 4
# 3 3
# 3 5
# 출력:

# 4
# 예제2
# 입력:

# 4 6
# 1 1
# 2 2
# 3 3
# 3 4
# 2 5
# 1 6
# 출력:

# 0
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
import sys
n, m=map(int, input().split())
lines=[]
for _ in range(m):
    a, b=map(int, input().split())
    lines.append((b, a-1))
lines.sort()
tmp_lines=[]
answer=sys.maxsize
def chk():
    n1, n2=list(range(n)), list(range(n))
    for y, x in lines:
        n1[x], n1[x+1]=n1[x+1], n1[x]
    for y, x in tmp_lines:
        n2[x], n2[x+1]=n2[x+1], n2[x]
    return n1==n2
def get_line(cnt):
    global answer
    if cnt==m:
        if chk():
            answer=min(answer, len(tmp_lines))
        return
    tmp_lines.append(lines[cnt])
    get_line(cnt+1)
    tmp_lines.pop()
    get_line(cnt+1)
get_line(0)
print(answer)
