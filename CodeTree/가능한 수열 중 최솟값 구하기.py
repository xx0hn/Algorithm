# 가능한 수열 중 최솟값 구하기
# 길이가 n인 수열을 세 개의 숫자 4, 5, 6 으로만 구성하려고 합니다. 이 때 임의의 길이를 갖는 두 개의 인접한 연속 부분 수열이 동일한 경우, 이는 불가능한 수열로 간주합니다. <그림 1>은 불가능한 수열의 예시들 입니다. 아래의 그림과 같이 빨간색으로 밑줄이 쳐진 부분 수열과 파란색으로 밑줄 쳐진 인접한 연속 부분 수열이 동일한 경우, 이는 불가능한 수열입니다. 이 때 길이가 n인 가능한 수열 중 앞에서부터 읽었을 때 사전순으로 가장 앞선 수열을 출력하는 코드를 작성해보세요.



# 입력 형식
# 첫 번째 줄에 n이 주어집니다.

# 1 ≤ n ≤ 80
# 출력 형식
# 길이가 n이고 4, 5, 6으로만 이루어진 가능한 수열 중 사전순으로 가장 앞선 수열을 출력합니다.

# 이 때 숫자 사이에는 공백 없이 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 2
# 출력:

# 45
# 예제2
# 입력:

# 3
# 출력:

# 454
# 예제3
# 입력:

# 7
# 출력:

# 4546454
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
n=int(input())
nums=['4', '5', '6']
answer=[]
result=''
def chk(arr):
    l=1
    while True:
        s1, e1=len(arr)-l, len(arr)-1
        s2, e2=s1-l, s1-1
        if s2<0:
            break
        if arr[s1:e1+1]==arr[s2:e2+1]:
            return False
        l+=1
    return True
def get_arr(cur):
    global result
    if cur==n:
        print(''.join(answer))
        quit()
    for i in range(3):
        answer.append(nums[i])
        if chk(answer):
            get_arr(cur+1)
        answer.pop()
get_arr(0)
