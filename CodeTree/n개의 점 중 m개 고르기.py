# n개의 점 중 m개 고르기
# 좌표 평면 위에 점 n개가 주어졌을 때, 점 m개를 적절히 선택하여 선택한 점들 중 거리가 가장 먼 두 점 사이의 거리값이 최소가 되도록 하는 프로그램을 작성해주세요.
# 단 여기서의 거리란 유클리디안 거리를 뜻합니다. 두 점 (x1, y1), (x2, y2) 사이의 유클리디안 거리 dist는 다음과 같이 정의됩니다.

# dist = \sqrt{(x_1-x_2)^2 + (y_1 - y_2)^2}dist= 
# (x 
# 1
# ​
#  −x 
# 2
# ​
#  ) 
# 2
#  +(y 
# 1
# ​
#  −y 
# 2
# ​
#  ) 
# 2
 
# ​
 

# 입력 형식
# 첫 번째 줄에는 n과 m이 공백을 사이에 두고 주어집니다.

# 두 번째 줄부터는 n개의 줄에 걸쳐 점의 정보 (x, y)가 주어집니다. 주어지는 모든 점의 위치는 전부 다르다고 가정해도 좋습니다. (1 ≤ x ≤ 100, 1 ≤ y ≤ 100)

# 2 ≤ m ≤ n ≤ 20
# 출력 형식
# 점 m개를 적절히 선택하여 가장 먼 두 점 사이의 거리가 최소가 되었을 때, 그때의 최소 거리에 제곱한 값을 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 2 2
# 1 1
# 1 3
# 출력:

# 4
# 예제2
# 입력:

# 3 2
# 1 1
# 4 4
# 3 5
# 출력:

# 2
# 예제 설명
# 두 번째 예제에서는 2, 3번 점을 선택했을 때 거리가 최소가 됩니다.

# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
import sys
n, m=map(int, input().split())
points=[list(map(int, input().split())) for _ in range(n)]
def get_dist(point1, point2):
    y1, x1=point1
    y2, x2=point2
    return (y1-y2)**2 + (x1-x2)**2
answer=sys.maxsize
p=[]
def get_case(cur, cnt):
    global answer
    if cur==n:
        if cnt==m:
            dist=0
            for i in range(m):
                for j in range(m):
                    dist=max(dist, get_dist(p[i], p[j]))
            answer=min(answer, dist)
        return
    p.append(points[cur])
    get_case(cur+1, cnt+1)
    p.pop()
    get_case(cur+1, cnt)
get_case(0, 0)
print(answer)
