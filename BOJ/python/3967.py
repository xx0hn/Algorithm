# 문제
# 매직 스타는 1부터 12까지 숫자가 헥사그램(hexagram)에 채워져 있는 모양으로 이루어져 있다.
#
#
#
# 매직 스타의 이름에 매직이 들어가는 이유는 숫자 네 개로 이루어진 줄의 숫자를 모두 합하면 26이 되기 때문이다. 위의 그림의 여섯 줄에 쓰여 있는 숫자는 다음과 같다.
#
# 1 + 4 + 10 + 11
# 11 + 5 + 3 + 7
# 7 + 6 + 12 + 1
# 2 + 10 + 5 + 9
# 9 + 3 + 6 + 8
# 8 + 12 + 4 + 2
# 매직 스타를 채우는 방법은 여러 가지가 있다. 일부만 채워진 매직 스타가 주어졌을 때, 수를 전부 다 채워서 매직 스타를 만드는 프로그램을 작성하시오.
#
# 입력
# 매직 스타의 모양이 주어진다. 수가 채워져 있지 않은 곳은 x로, 채워져 있는 곳은 'A'부터 'L'까지 알파벳으로 채워져 있다. i번째 알파벳은 숫자 i를 의미한다. '.'는 매직 스타의 형태를 만들기 위해서 사용하는 문자이다. 모든 입력은 예제 입력과 같은 형태로 주어진다.
#
# 출력
# 매직 스타를 만들 수 있는 방법 중에 사전 순으로 가장 앞서는 방법을 출력한다. (모든 줄을 순서대로 붙여서 하나의 문자열로 만든 뒤, 사전 순으로 비교한다.) 항상 정답이 존재하는 경우만 입력으로 주어진다.
from collections import defaultdict
s = [list(str(input())) for _ in range(5)]
star = ['' for _ in range(12)]
idx = 0
visited = defaultdict(bool)
for i in range(5):
    for j in range(9):
        if s[i][j].isalpha():
            star[idx] = s[i][j]
            idx += 1
            if s[i][j] != 'x':
                visited[s[i][j]] = True
apb = [chr(i) for i in range(ord('A'), ord('L')+1)]
def chk():
    if not (ord(star[0]) + ord(star[2]) + ord(star[5]) + ord(star[7]) == 22 + ord('A')*4):
        return False
    if not (ord(star[1]) + ord(star[2]) + ord(star[3]) + ord(star[4]) == 22 + ord('A')*4):
        return False
    if not (ord(star[0]) + ord(star[3]) + ord(star[6]) + ord(star[10]) == 22 + ord('A')*4):
        return False
    if not (ord(star[7]) + ord(star[8]) + ord(star[9]) + ord(star[10]) == 22 + ord('A')*4):
        return False
    if not (ord(star[1]) + ord(star[5]) + ord(star[8]) + ord(star[11]) == 22 + ord('A')*4):
        return False
    if not (ord(star[4]) + ord(star[6]) + ord(star[9]) + ord(star[11]) == 22 + ord('A')*4):
        return False
    return True
ans = []
flag = False
def magic_star(cur, mstar,):
    global ans, flag
    if flag:
        return
    if cur == 12:
        if chk():
            flag = True
            ans = mstar[:]
        return
    if mstar[cur] != 'x':
        magic_star(cur+1, mstar)
    else:
        for i in range(len(apb)):
            if not visited[apb[i]]:
                mstar[cur] = apb[i]
                visited[apb[i]] = True
                magic_star(cur+1, mstar)
                visited[apb[i]] = False
                mstar[cur] = 'x'
                if flag:
                    return
magic_star(0, star)
idx = 0
for i in range(5):
    for j in range(9):
        if s[i][j].isalpha():
            s[i][j] = ans[idx]
            idx += 1
for i in range(5):
    print(''.join(s[i]))
