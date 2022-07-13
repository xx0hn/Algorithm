# 문제
# 모든 값이 0으로 채워져 있는 길이가 N인 배열 A가 있다. 영선이는 다음과 같은 두 연산을 수행할 수 있다.
#
# 배열에 있는 값 하나를 1 증가시킨다.
# 배열에 있는 모든 값을 두 배 시킨다.
# 배열 B가 주어졌을 때, 배열 A를 B로 만들기 위한 연산의 최소 횟수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 배열의 크기 N이 주어진다. (1 ≤ N ≤ 50)
#
# 둘째 줄에는 배열 B에 들어있는 원소가 공백으로 구분해서 주어진다. 배열에 B에 들어있는 값은 0보다 크거나 같고, 1,000보다 작거나 같다.
#
# 출력
# 첫째 줄에 배열 A를 B로 바꾸기 위한 최소 연산 횟수를 출력한다.
n = int(input())
arr = list(map(int, input().split()))
answer = 0
def chk_even():
    for i in range(n):
        if arr[i]%2 == 0:
            continue
        else:
            return False
    return True
while arr != [0 for _ in range(n)]:
    while chk_even():
        for i in range(n):
            arr[i] //= 2
        answer += 1
    for i in range(n):
        if arr[i]%2 == 1:
            arr[i] -= 1
            answer += 1
print(answer)
