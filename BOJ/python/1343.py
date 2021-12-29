# 문제
# 민식이는 다음과 같은 폴리오미노 2개를 무한개만큼 가지고 있다. AAAA와 BB
#
# 이제 '.'와 'X'로 이루어진 보드판이 주어졌을 때, 민식이는 겹침없이 'X'를 모두 폴리오미노로 덮으려고 한다. 이때, '.'는 폴리오미노로 덮으면 안 된다.
#
# 폴리오미노로 모두 덮은 보드판을 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 보드판이 주어진다. 보드판의 크기는 최대 50이다.
#
# 출력
# 첫째 줄에 사전순으로 가장 앞서는 답을 출력한다. 만약 덮을 수 없으면 -1을 출력한다.
board=str(input())
board+='.'
cnt=0
answer=0
for i in range(len(board)):
    if board[i]=='X':
        cnt+=1
    if board[i]=='.':
        if cnt%2==0:
            continue
        else:
            answer=-1
            break
if answer==0:
    board=board.replace('XXXX', 'AAAA')
    board=board.replace('XX', 'BB')
    print(board[:-1])
else:
    print(answer)
