# 문제
# 세준이는 도서관에서 일한다. 도서관의 개방시간이 끝나서 세준이는 사람들이 마구 놓은 책을 다시 가져다 놓아야 한다. 세준이는 현재 0에 있고, 사람들이 마구 놓은 책도 전부 0에 있다. 각 책들의 원래 위치가 주어질 때, 책을 모두 제자리에 놔둘 때 드는 최소 걸음 수를 계산하는 프로그램을 작성하시오. 세준이는 한 걸음에 좌표 1칸씩 가며, 책의 원래 위치는 정수 좌표이다. 책을 모두 제자리에 놔둔 후에는 다시 0으로 돌아올 필요는 없다. 그리고 세준이는 한 번에 최대 M권의 책을 들 수 있다.
#
# 입력
# 첫째 줄에 책의 개수 N과, 세준이가 한 번에 들 수 있는 책의 개수 M이 주어진다. 둘째 줄에는 책의 위치가 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 책의 위치는 0이 아니며, 절댓값은 10,000보다 작거나 같은 정수이다.
#
# 출력
# 첫째 줄에 정답을 출력한다.
n, m=map(int, input().split())
location=list(map(int, input().split()))
positive=[]
negative=[]
distance=[]
for i in location:
    if i>0:
        positive.append(i)
    else:
        negative.append(i)
positive.sort(reverse=True)
negative.sort()
for i in range(len(positive)//m):
    distance.append(positive[m*i])
if len(positive)%m>0:
    distance.append(positive[(len(positive)//m)*m])
for i in range(len(negative)//m):
    distance.append(abs(negative[m*i]))
if len(negative)%m>0:
    distance.append(abs(negative[(len(negative)//m)*m]))
distance.sort()
answer=distance.pop()
answer+=2*sum(distance)
print(answer)
