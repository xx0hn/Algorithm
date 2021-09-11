# 문제
#
#
# 큰일이다. 시험 문제를 본 쿠기는 1번부터 풀 수가 없다. 시험 시간 동안 할 일이 없었던 쿠기는 교수님께 편지를 쓰려고 한다. 작년 시험에서 교수님께 그동안 감사했다는 편지를 전하고 D+을 받았던 기억이 있다. 그때 성적이 문제였는지, 편지가 문제였는지 궁금하여 이번에도 1번 문제의 답안 칸에 편지를 작성하려고 한다. 혹시나 하는 마음에 쿠기는 D+만은 피하고자 편지를 수정하려고 한다.
#
# 편지의 내용 S에 'A'가 있다면 S에 있는 'B', 'C', 'D', 'F'를 모두 'A'로 변경한다.
# 'A'가 없고 'B'가 있다면 S에 있는 'C', 'D', 'F'를 모두 'B'로 변경한다.
# 'A'와 'B'가 없고 'C'가 있다면 S에 있는 'D', 'F'를 모두 'C'로 변경한다.
# 'A', 'B'와 'C'가 모두 없다면 S에 있는 모든 문자를 'A'로 변경한다.
# 쿠기를 도와 편지를 수정하는 것을 도와주자.
#
# 입력
# 편지의 내용 S(1 ≤ S 의 길이 ≤ 1,000)가 주어진다. 문자열 S는 알파벳 대문자로 이루어져 있다.
s=input()
if s.count('A')>0:
    s=s.replace('B', 'A')
    s=s.replace('C', 'A')
    s=s.replace('D', 'A')
    s=s.replace('F', 'A')
elif s.count('A')==0 and s.count('B')>0:
    s=s.replace('C', 'B')
    s=s.replace('D', 'B')
    s=s.replace('F', 'B')
elif s.count('A')==0 and s.count('B')==0 and s.count('C')>0:
    s=s.replace('D', 'C')
    s=s.replace('F', 'C')
elif s.count('A')==0 and s.count('B')==0 and s.count('C')==0:
    s='A'*(len(s))
print(s)
