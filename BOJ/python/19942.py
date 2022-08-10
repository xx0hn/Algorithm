# 문제
# 식재료 N개 중에서 몇 개를 선택해서 이들의 영양분(단백질, 탄수화물, 지방, 비타민)이 일정 이상이 되어야 한다. 아래 표에 제시된 6가지의 식재료 중에서 몇 개를 선택해서 이들의 영양분의 각각 합이 최소 100, 70, 90, 10가 되도록 하는 경우를 생각해보자. 이 경우 모든 재료를 선택하면 쉽게 해결되지만, 우리는 조건을 만족시키면서도 비용이 최소가 되는 선택을 하려고 한다.
#
# 재료	단백질	지방	탄수화물	비타민	가격
# 1	30	55	10	8	100
# 2	60	10	10	2	70
# 3	10	80	50	0	50
# 4	40	30	30	8	60
# 5	60	10	70	2	120
# 6	20	70	50	4	40
# 예를 들어, 식재료 1, 3, 5를 선택하면 영양분은 100, 145, 130, 10으로 조건을 만족하지만 가격은 270이 된다. 대신 2, 3, 4를 선택하면 영양분의 합은 110, 130, 90, 10, 비용은 180이 되므로, 앞의 방법보다는 더 나은 선택이 된다.
#
# 입력으로 식재료 표가 주어졌을 때, 최저 영양소 기준을 만족하는 최소 비용의 식재료 집합을 찾아야 한다.
#
# 입력
# 첫 줄에 식재료의 개수 $N$이 주어진다.
#
# 다음 줄에는 단백질, 지방, 탄수화물, 비타민의 최소 영양성분을 나타내는 정수 $mp$, $mf$, $ms$, $mv$가 주어진다.
#
# 이어지는 $N$개의 각 줄에는 $i$번째 식재료의 단백질, 지방, 탄수화물, 비타민과 가격이 5개의 정수 $p_i$, $f_i$, $s_i$, $v_i$, $c_i$와 같이 주어진다. 식재료의 번호는 1부터 시작한다.
#
# 출력
# 첫 번째 줄에 최소 비용을 출력하고, 두 번째 줄에 조건을 만족하는 최소 비용 식재료의 번호를 공백으로 구분해 오름차순으로 한 줄에 출력한다. 같은 비용의 집합이 하나 이상이면 사전 순으로 가장 빠른 것을 출력한다.
#
# 조건을 만족하는 답이 없다면 -1을 출력하고, 둘째 줄에 아무것도 출력하지 않는다.
#
# 제한
#  $3 \le N \le 15$ 
#  $0 \le mp, mf, ms, mv \le 500$ 
#  $mp + mf + ms + mv > 0$ 
#  $0 \le p_i, f_i, s_i, v_i, c_i \le 500$ 
n = int(input())
info = [[] for _ in range(n+1)]
dan, gi, tan, vi = map(int, input().split())
for i in range(1, n+1):
    d, g, t, v, c = map(int, input().split())
    info[i] = [d, g, t, v, c]
answer = 1e9
answer_path = []
def chk(cd, cg, ct, cv):
    if cd >= dan and cg >= gi and ct >= tan and cv >= vi:
        return True
    return False
def find_min(cur, cd, cg, ct, cv, cc, path):
    global answer, answer_path
    if chk(cd, cg, ct, cv):
        if answer > cc:
            answer = cc
            answer_path = path
    if cur == len(info):
        return
    if cc > answer:
        return
    find_min(cur+1, cd+info[cur][0], cg+info[cur][1], ct+info[cur][2], cv+info[cur][3], cc+info[cur][4], path+[cur])
    find_min(cur+1, cd, cg, ct, cv, cc, path)
find_min(1, 0, 0, 0, 0, 0, [])
if answer == 1e9:
    print(-1)
    quit()
print(answer)
print(*answer_path)
