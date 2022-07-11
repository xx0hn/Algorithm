# 문제
# 상욱 조교는 동호에게 N개의 문제를 주고서, 각각의 문제를 풀었을 때 컵라면을 몇 개 줄 것인지 제시 하였다. 하지만 동호의 찌를듯한 자신감에 소심한 상욱 조교는 각각의 문제에 대해 데드라인을 정하였다.
#
# 문제 번호	1	2	3	4	5	6	7
# 데드라인	1	1	3	3	2	2	6
# 컵라면 수	6	7	2	1	4	5	1
# 위와 같은 상황에서 동호가 2, 6, 3, 1, 7, 5, 4 순으로 숙제를 한다면 2, 6, 3, 7번 문제를 시간 내에 풀어 총 15개의 컵라면을 받을 수 있다.
#
# 문제는 동호가 받을 수 있는 최대 컵라면 수를 구하는 것이다. 위의 예에서는 15가 최대이다.
#
# 문제를 푸는데는 단위 시간 1이 걸리며, 각 문제의 데드라인은 N이하의 자연수이다. 또, 각 문제를 풀 때 받을 수 있는 컵라면 수와 최대로 받을 수 있는 컵라면 수는 모두 231보다 작거나 같은 자연수이다.
#
# 입력
# 첫 줄에 숙제의 개수 N (1 ≤ N ≤ 200,000)이 들어온다. 다음 줄부터 N+1번째 줄까지 i+1번째 줄에 i번째 문제에 대한 데드라인과 풀면 받을 수 있는 컵라면 수가 공백으로 구분되어 입력된다.
#
# 출력
# 첫 줄에 동호가 받을 수 있는 최대 컵라면 수를 출력한다.
import heapq
n = int(input())
noodles = sorted([list(map(int, input().split())) for _ in range(n)], key= lambda x:(x[0]))
answers = []
for i in range(n):
    heapq.heappush(answers, (noodles[i][1], noodles[i][0]))
    if len(answers) > noodles[i][0]:
        heapq.heappop(answers)
answer = 0
while answers:
    tmp = answers.pop()
    answer += tmp[0]
print(answer)
