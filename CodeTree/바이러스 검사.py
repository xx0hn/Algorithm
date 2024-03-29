# 바이러스 검사
# 실력체크
# 정답률 35% · 제출 2,304회 · 예상 소요 시간 17분

# 추천해요
# 아쉬워요
# ko-kr
# 바이러스의 확산을 막기 위해 총 n개의 식당에 있는 고객들의 체온을 측정하고자 합니다. 체온을 측정하는 검사자는 검사팀장과 검사팀원으로 나뉘어집니다. 팀장과 팀원이 검사할 수 있는 고객의 수가 다르며, 한 가게당 팀장은 오직 한 명, 팀원은 여러명 있을 수 있습니다. 하지만 가게당 팀장 한 명은 무조건 필요합니다. 가게에 검사팀원만 존재하는 경우는 있을 수 없습니다. 팀장이든 팀원이든 담당한 가게에 대해서만 검사합니다.

# n개의 식당 고객들의 체온을 측정하기 위해 필요한 검사자 수의 최솟값을 구하는 프로그램을 작성해주세요.

# 입력 형식
# 첫째 줄에는 식당의 수 n이 주어집니다.

# 둘째 줄에는 각 식당에 있는 고객의 수가 공백을 사이에 두고 주어집니다.

# 셋째줄에는 검사팀장이 검사할 수 있는 최대 고객 수와 검사팀원이 검사할 수 있는 최대 고객 수가 공백을 사이에 두고 주어집니다.

# 1 ≤ n ≤ 1,000,000

# 1 ≤ (각 식당에 있는 고객의 수) ≤ 1,000,000

# 1 ≤ (팀장 혹은 팀원 한 명이 검사 가능한 최대 고객의 수) ≤ 1,000,000

# 출력 형식
# n개의 식당의 고객들을 모두 검사하기 위한 검사자의 최소의 수를 출력하세요

# 입출력 예제
# 예제1
# 입력:

# 1
# 1
# 2 2
# 출력:

# 1
# 예제2
# 입력:

# 5
# 999999 999999 999999 999999 999999
# 111111 5
# 출력:

# 888895
# 예제3
# 입력:

# 3
# 10 15 13
# 7 14
# 출력:

# 6
# 예제 설명
# 밑의 그림에서 REST은 식당, CUST는 고객, LDR은 검사 팀장, MBR은 검사 팀원 입니다.
# 예제 1번에서, 하나의 식당에 한 명의 손님이 있고, 팀장 한 명이 검사를 진행하면 되므로, 총 필요한 검사자는 1명 입니다.





# 예제 2번에서, 5개의 식당에 각 999999명의 손님이 있습니다. 각 식당마다, 팀장 한 명이 111111명을 검사하고, 팀원들이 한 명당 5명씩 총 888888명의 손님을 검사해야 합니다. 팀원 177777명이 5명씩 검사하고, 1명의 팀원이 3명만 검사하면 되므로, 필요한 팀원은 177777 + 1 = 177778명 입니다. 그러므로, 하나의 식당에 필요한 총 검사자는 1 + 177778 = 177779명 이고, 5개의 식당에 필요한 검사자는 177779 x 5 = 888895명 입니다.





# 예제 3번에서, 3개의 식당에 각 10명, 15명, 13명의 손님이 있습니다. 각 식당에서, 팀장이 7명의 사람을 검사하고, 남은 사람들은 한 명의 팀원이 검사할 수 있으므로, 하나의 식당에는 2명의 검사자가 필요합니다. 그러므로 필요한 총 검사자는 2 x 3 = 6명 입니다.





# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
n=int(input())
stores=list(map(int, input().split()))
leader, member=map(int, input().split())
answer=0
for store in stores:
    if store-leader<=0:
        answer+=1
    elif (store-leader)%member==0:
        answer+=(store-leader)//member
        answer+=1
    else:
        answer+=(store-leader)//member
        answer+=2
print(answer)
