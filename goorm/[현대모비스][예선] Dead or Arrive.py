from collections import defaultdict
n = int(input())
cars = []
speed = defaultdict(list)
for i in range(1, n+1):
	a, b = map(int, input().split())
	cars.append((i, a, b))
	if not speed[a] or (speed[a][1] <= b or speed[a][1]==b and speed[a][0]<=i):
		speed[a] = [i, b]
answer = 0
for key, lst in speed.items():
	answer += lst[0]
print(answer)
