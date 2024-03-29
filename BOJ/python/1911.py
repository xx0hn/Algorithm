# 문제
# 어젯밤 겨울 캠프 장소에서 월드 본원까지 이어지는, 흙으로 된 비밀길 위에 폭우가 내려서 N (1 <= N <= 10,000) 개의 물웅덩이가 생겼다. 월드학원은 물웅덩이를 덮을 수 있는 길이 L (L은 양의 정수) 짜리 널빤지들을 충분히 가지고 있어서, 이들로 다리를 만들어 물웅덩이들을 모두 덮으려고 한다. 물웅덩이들의 위치와 크기에 대한 정보가 주어질 때, 모든 물웅덩이들을 덮기 위해 필요한 널빤지들의 최소 개수를 구하여라.
#
# 입력
# 첫째 줄에 N과 L이 들어온다.
#
# 둘째 줄부터 N+1번째 줄까지 총 N개의 줄에 각각의 웅덩이들의 정보가 주어진다. 웅덩이의 정보는 웅덩이의 시작 위치와 끝 위치로 이루어진다. 각 위치는 0이상 1,000,000,000이하의 정수이다.
#
# 출력
# 첫째 줄에 모든 물웅덩이들을 덮기 위해 필요한 널빤지들의 최소 개수를 출력한다.
n, l = map(int, input().split())
pot = [list(map(int, input().split())) for _ in range(n)]
pot.sort()
cur = pot[0][0]
answer = 0
for s, e in pot:
    if cur > e:
        continue
    elif cur < s:
        cur = s
    if (e-cur)%l == 0:
        answer += (e-cur)//l
        cur += ((e-cur)//l) * l
    else:
        answer += (e-cur)//l + 1
        cur += ((e-cur)//l + 1) * l
print(answer)
