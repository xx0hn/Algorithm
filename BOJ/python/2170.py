# 문제
# 매우 큰 도화지에 자를 대고 선을 그으려고 한다. 선을 그을 때에는 자의 한 점에서 다른 한 점까지 긋게 된다. 선을 그을 때에는 이미 선이 있는 위치에 겹쳐서 그릴 수도 있는데, 여러 번 그은 곳과 한 번 그은 곳의 차이를 구별할 수 없다고 하자.
#
# 이와 같은 식으로 선을 그었을 때, 그려진 선(들)의 총 길이를 구하는 프로그램을 작성하시오. 선이 여러 번 그려진 곳은 한 번씩만 계산한다.
#
# 입력
# 첫째 줄에 선을 그은 횟수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 다음 N개의 줄에는 선을 그을 때 선택한 두 점의 위치 x, y(-1,000,000,000 ≤ x < y ≤ 1,000,000,000)가 주어진다.
#
# 출력
# 첫째 줄에 그은 선의 총 길이를 출력한다.
import sys
input = sys.stdin.readline
n = int(input())
lines = []
for _ in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))
lines.sort(key=lambda x:(x[0], x[1]))
answer = 0
bl, br = 0, 0
for l, r in lines:
    if not answer:
        answer = r-l
        bl, br = l, r
    elif bl <= l and br >= r:
        continue
    answer += r-l
    if br > l:
        answer -= br-l
    bl, br = l, r
print(answer)
