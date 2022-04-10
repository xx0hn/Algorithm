# 2n개 중에 n개의 숫자를 적절하게 고르기
# 2n개의 숫자가 주어졌을 때, 이 숫자를 각각 n개씩 2개의 그룹으로 나눠 각 그룹 원소합의 차가 최소가 되도록 하는 프로그램을 작성해주세요.

# 입력 형식
# 첫 번째 줄에는 n이 주어집니다.

# 두 번째 줄에는 2n개의 자연수가 공백을 사이에 두고 주어집니다.

# 1 ≤ n ≤ 10

# 1 ≤ 주어지는 숫자 ≤ 1,000

# 출력 형식
# 두 그룹간의 원소의 합의 차가 최소가 되도록 나눴을 때, 그 차이를 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 2
# 1 3 5 6
# 출력:

# 1
# 예제2
# 입력:

# 3
# 1 8 9 3 5 15
# 출력:

# 1
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
import sys
n=int(input())
nums=list(map(int, input().split()))
a, b=[], []
answer=sys.maxsize
def choose(cur):
    global answer
    if cur==2*n:
        if len(a)==n and len(b)==n:
            answer=min(answer, abs(sum(a)-sum(b)))
        return
    a.append(nums[cur])
    choose(cur+1)
    a.pop()

    b.append(nums[cur])
    choose(cur+1)
    b.pop()
choose(0)
print(answer)
