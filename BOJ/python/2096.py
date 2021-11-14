# 문제
#
# N줄에 0 이상 9 이하의 숫자가 세 개씩 적혀 있다. 내려가기 게임을 하고 있는데, 이 게임은 첫 줄에서 시작해서 마지막 줄에서 끝나게 되는 놀이이다.
#
# 먼저 처음에 적혀 있는 세 개의 숫자 중에서 하나를 골라서 시작하게 된다. 그리고 다음 줄로 내려가는데, 다음 줄로 내려갈 때에는 다음과 같은 제약 조건이 있다.
#
# 바로 아래의 수로 넘어가거나, 아니면 바로 아래의 수와 붙어 있는 수로만 이동할 수 있다는 것이다.
#
# 숫자표가 주어져 있을 때, 얻을 수 있는 최대 점수, 최소 점수를 구하는 프로그램을 작성하시오.
#
# 점수는 원룡이가 위치한 곳의 수의 합이다.
#
# ####입력####
#
# 첫째 줄에 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 숫자가 세 개씩 주어진다. 숫자는 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 중의 하나가 된다.
#
# ####출력####
#
# 첫째 줄에 얻을 수 있는 최대 점수와 최소 점수를 띄어서 출력한다.
#
# 출처:https://www.acmicpc.net/problem/2096
n=int(input())
maxDP=[0]*3
minDP=[0]*3
maxTemp=[0]*3
minTemp=[0]*3
for i in range(n):
    num1,num2,num3 = map(int, input().split())
    for j in range(3):
        if j==0:
            maxTemp[j]=num1+max(maxDP[j], maxDP[j+1])
            minTemp[j]=num1+min(minDP[j], minDP[j+1])
        elif j==1:
            maxTemp[j]=num2+max(maxDP[j-1], maxDP[j], maxDP[j+1])
            minTemp[j]=num2+min(minDP[j-1], minDP[j], minDP[j+1])
        else:
            maxTemp[j]=num3+max(maxDP[j-1], maxDP[j])
            minTemp[j]=num3+min(minDP[j-1], minDP[j])
    for j in range(3):
        maxDP[j]=maxTemp[j]
        minDP[j]=minTemp[j]
print(max(maxDP), min(minDP))
