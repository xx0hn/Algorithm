# 1차원 윷놀이
# 1번부터 m번까지 번호 순서대로 연결되어 있는 1차원 윷놀이 판에서 게임을 진행해보려고 합니다. m이 6인 경우 윷놀이 판의 모습은 다음과 같습니다.



# 처음에는 k개의 말이 1번 지점에 놓여있으며, n번의 턴에 숫자가 주어지고 각 턴마다 하나의 말을 선택하여 해당 숫자만큼 앞으로 나아갈 수 있습니다. 말은 앞으로 나아갈 때 한 칸 단위로 움직이며, 이때 앞으로 나아가던 말이 숫자 m번에 도달하게 되면 1점을 얻게 됩니다. 숫자 m에 도달한 말을 또 선택할 수는 있지만 이 경우에는 아무런 변화가 나타나지 않습니다.

# 위의 그림에서 k = 3인 경우를 예로 들어봅시다.



# 이때, n = 4이고 주어진 숫자들이 순서대로 2, 4, 2, 4 인 경우를 생각해봅시다.

# 만약 4회에 걸쳐 순서대로 1번, 2번, 1번, 2번 말을 고른다면 2번 말만 점수를 얻게 됩니다.



# 하지만 만약 1번, 1번, 2번, 2번 순서대로 말을 고르게 되면, 점수를 2점 얻게 됩니다.



# n번의 턴에 대해 움직일 말을 적절하게 선택하여 얻을 수 있는 점수를 최대로 하는 프로그램을 작성해보세요.
# 입력 형식
# 첫 번째 줄에는 턴의 수를 나타내는 n과 윷놀이 판의 상태를 나타내는 m, 그리고 말의 수를 나타내는 k가 각각 공백을 사이에 두고 주어집니다.

# 두 번째 줄에는 n개의 숫자가 공백을 사이에 두고 주어집니다. 이 숫자들은 각 턴마다 나아갈 수 있는 거리를 의미합니다. (1 ≤ 주어지는 숫자 ≤ 100)

# 1 ≤ n ≤ 12

# 2 ≤ m ≤ 100

# 1 ≤ k ≤ 4

# 출력 형식
# n번의 턴을 거친 이후에 최대로 얻을 수 있는 점수를 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 4 6 3
# 2 4 2 4
# 출력:

# 2
# 예제2
# 입력:

# 6 10 3
# 5 3 2 2 3 3
# 출력:

# 2
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
n, m, k=map(int, input().split())
d=list(map(int, input().split()))
locates=[1 for _ in range(k)]
answers=[]
def chk(l):
    cnt=0
    for i in range(k):
        if l[i]>=m:
            cnt+=1
    return cnt
def move(cur):
    if cur==n:
        answers.append(chk(locates))
        return
    for i in range(k):
        locates[i]+=d[cur]
        move(cur+1)
        locates[i]-=d[cur]
move(0)
print(max(answers))
