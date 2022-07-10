# 문제
# 남자 N명과 여자 N명이 상근이가 주최한 댄스 파티에 왔다. 상근이는 모든 사람의 키를 알고있다. 각 남자는 모두 여자와 춤을 출 수 있고, 여자는 남자와 춤을 출 수 있다. 모든 사람은 많아야 한 사람과 춤을 출 수 있다.
#
# 모든 남자는 자신이 선호하는 여자와 춤을 추려고 한다. 각 남자가 선호하는 여자는 두 가지 유형이 있는데, 한 유형은 자신보다 키가 큰 여자이고, 다른 유형은 자신보다 키가 작은 유형이다. 여자도 남자와 마찬가지로 자신이 선호하는 남자와 춤을 추려고 한다. 각 여자가 선호하는 남자도 남자와 비슷하게 두 유형이 있다. (자신보다 키가 큰 남자, 작은 남자) 키가 같은 남자와 여자가 춤을 추는 일은 일어나지 않는다.
#
# 이때, 상근이는 각 사람의 키와 선호하는 이성 유형을 알고 있다. 이런 조건을 가지고 춤을 출 쌍을 만들어 주려고 한다. 상근이는 최대 몇 쌍을 만들 수 있을까?
#
# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100,000)
#
# 둘째 줄에는 남자의 키가 밀리미터 단위로 주어진다. 키는 절댓값이 1500보다 크거나 같고, 2500보다 작거나 같은 정수이다. 사람의 키는 주어지는 값의 절댓값이다. 키가 양수인 경우에는 자신보다 키가 큰 여자와 춤을 추기를 원하는 남자이고, 음수인 경우에는 키가 작은 사람과 춤을 추기를 원하는 남자이다.
#
# 셋째 줄에는 여자의 키가 밀리미터 단위로 주어진다. 키의 범위나 의미 역시 남자와 동일하다.
#
# 출력
# 첫째 줄에 상근이가 만들어 줄 수 있는 쌍의 최댓값을 출력한다.
n = int(input())
man = sorted(list(map(int, input().split())))
woman = sorted(list(map(int, input().split())))
mp, wp = 0, n-1
answer = 0
while mp < n and wp >= 0:
    if man[mp] < 0:
        if woman[wp] > 0:
            if abs(man[mp]) > abs(woman[wp]):
                answer += 1
                mp += 1
                wp -= 1
            else:
                wp -= 1
        else:
            mp += 1
    else:
        if woman[wp] < 0:
            if abs(man[mp]) < abs(woman[wp]):
                answer += 1
                mp += 1
                wp -= 1
            else:
                wp -= 1
        else:
            wp -= 1
print(answer)