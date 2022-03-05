# 문제
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
#
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.
#
# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다.
#
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000,000)
#
# 출력
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
n=int(input())
arr=list(map(int, input().split()))
result=[0]
for a in arr:
    if result[-1]<a:
        result.append(a)
    else:
        left, right=0, len(result)-1
        while left<right:
            mid=(left+right)//2
            if result[mid]<a:
                left=mid+1
            else:
                right=mid
        result[right]=a
print(len(result)-1)
