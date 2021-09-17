n=int(input())
DP=[0]*1001
DP[1]=1
DP[2]=0
DP[3]=1
DP[4]=1
for i in range(5,n+1):
    if DP[i-1]==1 and DP[i-3]==1 and DP[i-4]==1:
        DP[i]=0
    else:
        DP[i]=1
if DP[n]==1:
    print("SK")
else:
    print("CY")
