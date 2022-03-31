# 1차원 폭발 게임
# 1부터 100 사이의 숫자가 적혀있는 N개의 폭탄이 쌓여있습니다.



# 이때 M개 이상 연속으로 같은 숫자가 적혀있는 폭탄들은 터지게 되고, 중력에 의해 위에 있던 폭탄들은 밑으로 떨어지게 됩니다. M개 이상 연속한 폭탄은 부분만 터져서는 안되고 전부 다 터져야 합니다.

# 예를 들어 다음과 같은 예시에서 M이 2인 경우 3이라는 숫자가 연속하여 M번 이상 나오므로 그 폭탄들이 터지게 됩니다.



# 만약 M개 이상인 폭탄들의 쌍이 여러 개라면 동시에 터지게 됩니다.



# 이 과정을 M개 이상 연속한 숫자를 갖는 폭탄들이 존재하지 않을때까지 계속 반복했을 때, 최종 결과를 출력하는 프로그램을 작성해주세요.

# 위의 예에서 M=2인 경우 진행 과정은 다음과 같습니다.



# 입력 형식
# 첫째 줄에는 N과 M이 공백을 사이에 두고 주어집니다.

# 두 번째 줄 부터 N개의 줄에 걸쳐 각 폭탄의 숫자가 주어집니다. 숫자는 위에 있는 폭탄에 적혀있는 숫자부터 아래 방향으로 순서대로 주어집니다.

# 1 ≤ N ≤ 100

# 1 ≤ M ≤ 100

# 출력 형식
# 첫 번째 줄에는 최종적으로 남게 된 폭탄의 개수를 출력합니다.

# 두 번째 줄 부터는 한 줄에 하나씩 위에서부터 아래 방향으로 각 폭탄에 적혀있는 숫자를 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 4 2
# 1
# 2
# 2
# 1
# 출력:

# 0
# 예제2
# 입력:

# 4 2
# 1
# 2
# 2
# 3
# 출력:

# 2
# 1
# 3
# 예제3
# 입력:

# 8 2
# 1
# 3
# 3
# 3
# 2
# 1
# 1
# 2
# 출력:

# 1
# 1
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
import copy
n, m=map(int, input().split())
bomb=[int(input()) for _ in range(n)]
def drop(l):
    global bomb
    cnt=1
    idx=0
    tmp=[1 for _ in range(l)]
    for i in range(1, l):
        if bomb[i]==bomb[i-1]:
            tmp[i]=tmp[i-1]+1
    for i in range(l-1, -1, -1):
        if tmp[i]>=m:
            for j in range(i, i-tmp[i], -1):
                tmp[j]=0
    result=[]
    for i in range(l):
        if tmp[i]:
            result.append(bomb[i])
    bomb=copy.deepcopy(result)
    return bomb
while True:
    if bomb==drop(len(bomb)):
        break
print(len(bomb))
for i in range(len(bomb)):
    print(bomb[i])
