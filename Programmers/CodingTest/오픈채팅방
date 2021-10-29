def solution(record):
    answer = []
    act=[]
    userInfo=dict()
    for i in record:
        data=i.split()
        action=data[0]
        userId=data[1]
        if action == 'Enter' or action =='Change':
            nickname=data[2]
            userInfo[userId]=nickname
        act.append((action, userId))
    for i in act:
        action=i[0]
        id=i[1]
        if action=='Enter':
            answer.append(f'{userInfo[id]}님이 들어왔습니다.')
        elif action=='Leave':
            answer.append(f'{userInfo[id]}님이 나갔습니다.')
    return answer
