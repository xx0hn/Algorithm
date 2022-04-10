# 최소 점프 횟수
# 각 위치로부터의 최대 점프 가능 거리를 의미하는 n개의 숫자가 주어졌을 때, 첫 번째 위치로부터 n번째 위치에 도달하기 위해 필요한 최소 점프 횟수를 구하는 판단하는 프로그램을 작성해보세요. 여기서 최대 점프 가능 거리란 현재 위치로부터 추가적으로 나아갈 수 있는 최대 칸의 수를 의미하며, 점프는 앞으로만 가능합니다.

# 예를 들어 다음과 같이 n개의 숫자가 주어진 경우라면, 2번 점프하여 n번째 위치가 도달이 가능합니다.



# 입력 형식
# 첫 번째 줄에 n이 주어집니다.

# 두 번째 줄에는 n개의 숫자가 공백을 사이에 두고 주어집니다.

# 2 ≤ n ≤ 10

# 0 ≤ 주어지는 숫자 ≤ 4

# 출력 형식
# 첫 번째 위치로부터 n번째 위치에 도달하기 위해 필요한 최소 점프 횟수를 출력합니다. 만약 불가능하다면 -1을 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 5
# 2 3 1 1 4
# 출력:

# 2
# 예제2
# 입력:

# 5
# 2 1 1 0 4
# 출력:

# -1
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
import sys
n=int(input())
arr=list(map(int, input().split()))
answer=sys.maxsize
def jump(cur, cnt):
    global answer
    for i in range(1, arr[cur]+1):
        if cur+i==n-1:
            answer=min(answer, cnt)
            return
        jump(cur+i, cnt+1)
jump(0, 1)
if answer==sys.maxsize:
    print(-1)
else:
    print(answer)
