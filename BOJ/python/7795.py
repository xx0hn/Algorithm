# 문제
# 심해에는 두 종류의 생명체 A와 B가 존재한다. A는 B를 먹는다. A는 자기보다 크기가 작은 먹이만 먹을 수 있다. 예를 들어, A의 크기가 {8, 1, 7, 3, 1}이고, B의 크기가 {3, 6, 1}인 경우에 A가 B를 먹을 수 있는 쌍의 개수는 7가지가 있다. 8-3, 8-6, 8-1, 7-3, 7-6, 7-1, 3-1.
#
#
#
# 두 생명체 A와 B의 크기가 주어졌을 때, A의 크기가 B보다 큰 쌍이 몇 개나 있는지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 A의 수 N과 B의 수 M이 주어진다. 둘째 줄에는 A의 크기가 모두 주어지며, 셋째 줄에는 B의 크기가 모두 주어진다. 크기는 양의 정수이다. (1 ≤ N, M ≤ 20,000)
#
# 출력
# 각 테스트 케이스마다, A가 B보다 큰 쌍의 개수를 출력한다.
def binary_search(left, right, target):
    result=0
    while left<=right:
        mid=(left+right)//2
        if B[mid]<target:
            left=mid+1
            result=mid
        else:
            right=mid-1
    return result+1

t=int(input())
for _ in range(t):
    a, b=map(int, input().split())
    A=sorted(list(map(int, input().split())))
    B=sorted(list(map(int, input().split())))
    answer=0
    for i in A:
        if i<=B[0]:
            continue
        left, right=0, b-1
        answer+=binary_search(left, right, i)
    print(answer)
