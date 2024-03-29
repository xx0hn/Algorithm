# 서로 다른 BST 개수 세기
# 실력체크
# 정답률 28% · 제출 1,208회 · 예상 소요 시간 36분

# 추천해요
# 아쉬워요
# ko-kr
# BST란 자식을 2개 이하로 갖는 이진 탐색 트리입니다. 각 노드마다 왼쪽에 있는 모든 노드들의 값이 해당 노드의 값 보다 작아야 하고, 오른쪽에 있는 모든 노드들의 값이 해당 노드의 값 보다 커야 합니다.

# 1부터 N까지의 숫자들을 단 한 번씩만 써서 만들 수 있는 노드의 개수가 N인 서로 다른 이진 탐색 트리 개수를 세는 프로그램을 작성해보세요.

# 예를 들어 N = 4 일때,

# 다음은 모든 정점이 연결되어 있지 않기 때문에 트리가 아닙니다.



# 이 그림은 사이클이 존재하므로 트리가 아닙니다.



# 이 그림은 트리이긴 하지만, 자식을 2개보다 많이 갖고 있는 노드가 있으므로 이진 탐색 트리가 아닙니다.



# 다음은 노드 2를 기준으로 왼쪽 자식에 자신보다 값이 큰 노드 4가 있기 때문에 이진 탐색 트리가 아닙니다.



# 다음은 올바른 이진 탐색 트리입니다.



# N = 3일 때 가능한 BST는 총 5개 입니다.



# 입력 형식
# 첫째 줄에는 N이 주어집니다.

# 1 ≤ N ≤ 19
# 출력 형식
# N개의 노드로 만들 수 있는 서로 다른 BST의 개수를 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 2
# 출력:

# 2
# 예제2
# 입력:

# 3
# 출력:

# 5
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
n=int(input())
dp=[0 for _ in range(n+1)]
dp[0]=1
for i in range(1, n+1):
    for j in range(i):
        dp[i]+=(dp[j]*dp[i-j-1])
print(dp[n])
