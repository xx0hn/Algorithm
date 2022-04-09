# 겹치지 않게 선분 고르기
# 수직선상에 n개의 선분이 주어졌을 때, 겹치지 않게 가장 많은 수의 선분을 고르는 프로그램을 작성해보세요. 단, 끝점을 공유하는 것 역시 겹친 것으로 생각합니다.

# 입력 형식
# 첫 번째 줄에는 선분의 개수를 나타내는 n이 주어집니다.

# 두 번째 줄 부터는 n개의 줄에 걸쳐 각 선분의 정보 (x1, x2)가 공백을 사이에 두고 주어집니다. 이 때 x1, x2는 해당 선분의 수직선상에서의 양끝점 좌표를 나타냅니다. (1 ≤ x1 < x2 ≤ 1,000)

# 1 ≤ n ≤ 15
# 출력 형식
# 겹치지 않게 뽑을 수 있는 최대 선분의 수를 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 3
# 1 2
# 3 4
# 5 6
# 출력:

# 3
# 예제2
# 입력:

# 3
# 1 2
# 1 4
# 3 4
# 출력:

# 2
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
n=int(input())
line=[list(map(int, input().split())) for _ in range(n)]
line.sort(key=lambda x: (x[0], x[1]))
results=[]
answer=0
def get_line(cur, cnt):
    global answer
    if cur==n:
        if cnt<=1:
            answer=max(answer, cnt)
            return
        for i in range(1, len(results)):
            if results[i-1][1]>=results[i][0]:
                return
            else:
                continue
        answer=max(answer, cnt)
        return
    results.append(line[cur])
    get_line(cur+1, cnt+1)
    results.pop()
    get_line(cur+1, cnt)
get_line(0, 0)
print(answer)
