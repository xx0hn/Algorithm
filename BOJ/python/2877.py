# 문제
# 창영이는 4와 7로 이루어진 수를 좋아한다. 창영이가 좋아하는 수 중에 K번째 작은 수를 구해 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 K(1 ≤ K ≤ 109)가 주어진다.
#
# 출력
# 첫째 줄에 창영이가 좋아하는 숫자 중 K번째 작은 수를 출력한다.
k=int(input())
cnt=0
n=0
answer=[]
result=''
while 1:
    n+=1
    cnt+=2**n
    if cnt>=k:
        break
idx=k-2**n+1
for i in range(n):
    answer.append(idx%2)
    idx//=2
answer.reverse()
for i in range(len(answer)):
    if answer[i]==1:
        result+='7'
    else:
        result+='4'
print(int(result))
