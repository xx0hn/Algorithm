# 문제
# 1부터 N까지의 수로 이루어진 순열이 있다. 이때, 사전순으로 바로 이전에 오는 순열을 구하는 프로그램을 작성하시오.
#
# 사전 순으로 가장 앞서는 순열은 오름차순으로 이루어진 순열이고, 가장 마지막에 오는 순열은 내림차순으로 이루어진 순열이다.
#
# N = 3인 경우에 사전순으로 순열을 나열하면 다음과 같다.
#
# 1, 2, 3
# 1, 3, 2
# 2, 1, 3
# 2, 3, 1
# 3, 1, 2
# 3, 2, 1
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄에 순열이 주어진다.
#
# 출력
# 첫째 줄에 입력으로 주어진 순열의 이전에 오는 순열을 출력한다. 만약, 사전순으로 가장 처음에 오는 순열인 경우에는 -1을 출력한다.
n=int(input())
arr=list(map(int, input().split()))
k=-1
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        k=i
if k==-1:
    print(-1)
else:
    for i in range(k+1, len(arr)):
        if arr[i]<arr[k]:
            m=i
    arr[k], arr[m]=arr[m], arr[k]
    tmp=sorted(arr[k+1:], reverse=True)
    arr=arr[:k+1]+tmp
    print(*arr)
