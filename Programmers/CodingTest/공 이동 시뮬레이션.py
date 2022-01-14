# 공 이동 시뮬레이션
# 문제 설명
# n행 m열의 격자가 있습니다. 격자의 각 행은 0, 1, ..., n-1번의 번호, 그리고 각 열은 0, 1, ..., m-1번의 번호가 순서대로 매겨져 있습니다. 당신은 이 격자에 공을 하나 두고, 그 공에 다음과 같은 쿼리들을 날리고자 합니다.

# 열 번호가 감소하는 방향으로 dx칸 이동하는 쿼리 (query(0, dx))
# 열 번호가 증가하는 방향으로 dx칸 이동하는 쿼리 (query(1, dx))
# 행 번호가 감소하는 방향으로 dx칸 이동하는 쿼리 (query(2, dx))
# 행 번호가 증가하는 방향으로 dx칸 이동하는 쿼리 (query(3, dx))
# 단, 공은 격자 바깥으로 이동할 수 없으며, 목적지가 격자 바깥인 경우 공은 이동하다가 더 이상 이동할 수 없을 때 멈추게 됩니다. 예를 들어, 5행 × 4열 크기의 격자 내의 공이 3행 2열에 있을 때 query(3, 10) 쿼리를 받은 경우 공은 4행 2열에서 멈추게 됩니다. (격자의 크기가 5행 × 4열이므로, 0~4번 행과 0~3번 열로 격자가 구성되기 때문입니다.)

# 격자의 행의 개수 n, 열의 개수 m, 정수 x와 y, 그리고 쿼리들의 목록을 나타내는 2차원 정수 배열 queries가 매개변수로 주어집니다. n × m개의 가능한 시작점에 대해서 해당 시작점에 공을 두고 queries 내의 쿼리들을 순서대로 시뮬레이션했을 때, x행 y열에 도착하는 시작점의 개수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ n ≤ 109
# 1 ≤ m ≤ 109
# 0 ≤ x < n
# 0 ≤ y < m
# 1 ≤ queries의 행의 개수 ≤ 200,000
# queries의 각 행은 [command,dx] 두 정수로 이루어져 있습니다.
# 0 ≤ command ≤ 3
# 1 ≤ dx ≤ 109
# 이는 query(command, dx)를 의미합니다.
# 입출력 예
# n	m	x	y	queries	result
# 2	2	0	0	[[2,1],[0,1],[1,1],[0,1],[2,1]]	4
# 2	5	0	1	[[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]	2
# 입출력 예 설명
# 입출력 예 #1

# 다음 애니메이션은 4개의 가능한 시작점에 대한 모든 시뮬레이션을 나타낸 것입니다.
# ex1

# 어떤 곳에서 출발하더라도 항상 0행 0열에 도착하기 때문에, 4를 return 해야 합니다.
# 입출력 예 #2

# 다음 애니메이션은 10개의 가능한 시작점에 대한 모든 시뮬레이션을 나타낸 것입니다.
# ex2

# 0행 1열, 1행 1열에서 출발했을 때만 0행 1열에 도착하므로, 2를 return 해야 합니다.
def solution(n, m, x, y, queries):
    answer = 0
    t, l, r, b = x, y, y, x
    queries.reverse()
    for i, j in queries:
        if i == 0:
            if r+j<m:
                tmp=r+j
            else:
                tmp=m-1
            if l == 0: 
                r = tmp
            else: 
                l, r = l + j, tmp
        if i == 1:
            if l-j>=0:
                tmp=l-j
            else:
                tmp=0
            if r == m - 1: 
                l = tmp
            else: 
                l, r = tmp, r - j
        if i == 2:
            if b+j<n:
                tmp=b+j
            else:
                tmp=n-1
            if t == 0:
                b = tmp
            else:
                t, b = t + j, tmp
        if i == 3:
            if t-j>=0:
                tmp=t-j
            else:
                tmp=0
            if b == n - 1:
                t = tmp
            else:
                t, b = tmp, b - j
        if l > m - 1 or r < 0 or t > n - 1 or b < 0:
            break
    else:
        answer = ((b - t) + 1) * ((r - l) + 1) 
    return answer
