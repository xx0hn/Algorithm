# 문제
# 민혁이는 소셜 네트워크 사이트에서 친구를 만드는 것을 좋아하는 친구이다. 우표를 모으는 취미가 있듯이, 민혁이는 소셜 네트워크 사이트에서 친구를 모으는 것이 취미이다.
#
# 어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.
#
# 친구 네트워크란 친구 관계만으로 이동할 수 있는 사이를 말한다.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스의 첫째 줄에는 친구 관계의 수 F가 주어지며, 이 값은 100,000을 넘지 않는다. 다음 F개의 줄에는 친구 관계가 생긴 순서대로 주어진다. 친구 관계는 두 사용자의 아이디로 이루어져 있으며, 알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열이다.
#
# 출력
# 친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.
from collections import defaultdict
t = int(input())
def find(a):
    if a != parents[a]:
        parents[a] = find(parents[a])
    return parents[a]
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        tmp = sorted([a, b])
        parents[tmp[1]] = tmp[0]
        nums[tmp[0]] += nums[tmp[1]]
for _ in range(t):
    f = int(input())
    parents = defaultdict(str)
    nums = defaultdict(int)
    for _ in range(f):
        a, b = map(str, input().split())
        if not parents[a]:
            parents[a] = a
            nums[a] = 1
        if not parents[b]:
            parents[b] = b
            nums[b] = 1
        union(a, b)
        print(nums[find(a)])
