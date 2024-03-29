# 컨베이어 벨트
# 시계 방향으로 한 칸씩 회전하는 컨베이어 벨트가 있습니다. 컨베이어 벨트 위아래로 n개씩 총 2 * n 개의 숫자가 두 줄로 적혀 있고, 1초에 한 칸씩 움직입니다.



# 위의 그림에서 1초가 흐른 뒤에는 다음과 같이 그림이 바뀌게 됩니다.



# t초의 시간이 흐른 뒤 컨베이어 벨트에 놓여있는 숫자들의 상태를 출력하는 프로그램을 작성해보세요.

# 입력 형식
# 첫 번째 줄에는 n과 t가 공백을 사이에 두고 주어집니다.

# 두 번째 줄에는 위 변에 있는 초기 n개의 숫자들이 공백을 사이에 두고 주어집니다.

# 세 번째 줄에는 아래 변에 있는 초기 n개의 숫자들이 공백을 사이에 두고 주어집니다.

# 숫자는 각 변마다 숫자가 올바르게 보이는 방향에서 바라봤을 때 왼쪽에서 오른쪽 순으로 주어집니다.

# 1 ≤ n ≤ 200

# 1 ≤ t ≤ 1,000

# 1 ≤ 주어지는 숫자 ≤ 9

# 출력 형식
# t초 후 컨베이어 벨트에 놓여있는 숫자들의 상태를 출력합니다.

# 첫 번째 줄에는 위 위 변에 있는 n개의 숫자들을 공백을 사이에 두고 출력합니다.

# 두 번째 줄에는 아래 변에 있는 n개의 숫자들을 공백을 사이에 두고 출력합니다.

# 숫자는 각 변마다 입력으로 주어지는 순서대로 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 3 1
# 1 2 3
# 6 5 1
# 출력:

# 1 1 2
# 3 6 5
# 예제2
# 입력:

# 3 3
# 1 2 3
# 6 5 1
# 출력:

# 6 5 1
# 1 2 3
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
n, t=map(int, input().split())
up=list(map(int, input().split()))
down=list(map(int, input().split()))
for i in range(t):
    u_tmp, d_tmp=[down[-1]]+up[:-1], [up[-1]]+down[:-1]
    up, down=u_tmp, d_tmp
print(*up)
print(*down)
