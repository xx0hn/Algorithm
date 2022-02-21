# 문제
# 한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.
#
#
#
# N > 1인 경우, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.
#
# 다음 예는 22 × 22 크기의 배열을 방문한 순서이다.
#
#
#
# N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.
#
# 다음은 N=3일 때의 예이다.
#
#
#
# 입력
# 첫째 줄에 정수 N, r, c가 주어진다.
#
# 출력
# r행 c열을 몇 번째로 방문했는지 출력한다.
#
# 제한
# 1 ≤ N ≤ 15
# 0 ≤ r, c < 2N
N, r, c=map(int, input().split())
answer=0
def recursion(size, y, x):
    global answer
    if size==0:
        return
    size-=1
    if y<2**size and x<2**size:
        answer+=(2**size)*(2**size)*0
        recursion(size, y, x)
    elif y<2**size and x>=2**size:
        answer+=(2**size)*(2**size)*1
        x-=(2**size)
        recursion(size, y, x)
    elif y>=2**size and x<2**size:
        answer+=(2**size)*(2**size)*2
        y-=(2**size)
        recursion(size, y, x)
    else:
        answer+=(2**size)*(2**size)*3
        y-=(2**size)
        x-=(2**size)
        recursion(size, y, x)
recursion(N, r, c)
print(answer)
