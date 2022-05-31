# 문제
# 웅찬이는 과제가 많다. 하루에 한 과제를 끝낼 수 있는데, 과제마다 마감일이 있으므로 모든 과제를 끝내지 못할 수도 있다. 과제마다 끝냈을 때 얻을 수 있는 점수가 있는데, 마감일이 지난 과제는 점수를 받을 수 없다.
#
# 웅찬이는 가장 점수를 많이 받을 수 있도록 과제를 수행하고 싶다. 웅찬이를 도와 얻을 수 있는 점수의 최댓값을 구하시오.
#
# 입력
# 첫 줄에 정수 N (1 ≤ N ≤ 1,000)이 주어진다.
#
# 다음 줄부터 N개의 줄에는 각각 두 정수 d (1 ≤ d ≤ 1,000)와 w (1 ≤ w ≤ 100)가 주어진다. d는 과제 마감일까지 남은 일수를 의미하며, w는 과제의 점수를 의미한다.
#
# 출력
# 얻을 수 있는 점수의 최댓값을 출력한다.
# from collections import deque
# n=int(input())
# tasks=[list(map(int, input().split())) for _ in range(n)]
# tasks=deque(sorted(tasks, key=lambda x:(x[1]/x[0], -x[0]), reverse=True))
# answer=0
# cur=1
# while tasks:
#     deadline, point=tasks.popleft()
#     if cur<=deadline:
#         answer+=point
#         cur+=1
# print(answer)
import heapq
n=int(input())
tasks=[list(map(int, input().split())) for _ in range(n)]
tasks.sort()
available=[]
cur=tasks[-1][0]
answer=0
while cur>0:
    while tasks and tasks[-1][0]>=cur:
        heapq.heappush(available, -tasks.pop()[1])
    cur-=1
    if not available:
        continue
    answer-=heapq.heappop(available)
print(answer)
