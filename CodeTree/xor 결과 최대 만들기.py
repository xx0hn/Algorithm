# xor 결과 최대 만들기
# n개의 음이 아닌 정수가 입력으로 주어졌을 때, 그 중 m개의 숫자를 뽑아 모두 xor한 결과의 최댓값을 출력하는 코드를 작성해보세요.

# 입력 형식
# 첫 번째 줄에는 n과 m이 공백을 사이에 두고 주어지고, 두 번째 줄에는 n개의 정수가 공백을 사이에 두고 주어집니다.

# 정수는 0 ~ 1,000,000 사이의 범위를 갖습니다.

# 1 ≤ m ≤ n ≤ 20

# 출력 형식
# m개의 숫자를 골랐을 때 가능한 xor 결과의 최댓값을 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 5 3 
# 1 2 3 4 5
# 출력:

# 7
# 예제 설명
# 2, 4, 5을 뽑으면 2 xor 4 xor 5 = 3 이지만

# 1, 3, 5를 뽑으면 1 xor 3 xor 5 = 7 로 최대가 됩니다.

# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
n, m=map(int, input().split())
nums=list(map(int, input().split()))
result=[]
answer=0
def xor_cul(cur, cnt):
    global answer
    if cur==n:
        if cnt==m:
            tmp=0
            for i in range(len(result)):
                if result[i]==1:
                    tmp^=nums[i]
            answer=max(answer, tmp)
        return
    result.append(1)
    xor_cul(cur+1, cnt+1)
    result.pop()

    result.append(0)
    xor_cul(cur+1, cnt)
    result.pop()
xor_cul(0, 0)
print(answer)
