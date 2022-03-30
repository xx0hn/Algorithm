# 최단 Run Length 인코딩
# 길이가 n인 문자열 A가 주어졌을 때, 적절하게 특정 횟수만큼 오른쪽으로 shift하여, shift 된 이후의 문자열에 Run-Length Encoding을 진행했을 때의 길이가 최소가 되도록 하려고 합니다.

# Run-Length Encoding이란 간단한 비손실 압축 방식으로, 연속해서 나온 문자와 연속해서 나온 개수로 나타내는 방식입니다. 예를 들어, 문자열 A가 aaabbbbcaa인 경우 순서대로 a가 3번, b가 4번, c가 1번 그리고 a가 2번 나왔으므로 Run-Length Encoding을 적용하게 되면 a3b4c1a2이 되며 길이는 8이 됩니다.

# 만약 문자열 A에 해당하는 aaabbbbcaa를 오른쪽으로 2번 shift를 하게 되면 aaaaabbbbc가 되며, 이에 Run-Length Encoding을 적용하게 되면 a5b4c1이 되므로 길이가 6이 되어 최소가 됩니다.

# shift를 진행하여 나올 수 있는 Run-Length Encoding 이후의 결과들 중 최소 길이를 구하는 프로그램을 작성해보세요.

# 입력 형식
# 첫 번째 줄에 문자열 A가 주어집니다. 문자열 A는 소문자 알파벳으로만 이루어져 있습니다.

# 1 ≤ 문자열 A의 길이 ≤ 10
# 출력 형식
# 문자열 A를 오른쪽으로 특정 횟수만큼 shift하고 Run-Length Encoding을 적용했을 때 나올 수 있는 길이 중 최소 길이를 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# aaabbbbcaa
# 출력:

# 6
# 예제2
# 입력:

# aaaaaaaaaa
# 출력:

# 3
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
from collections import deque
s=deque(list(str(input())))
answers=[]
if len(s)==1:
    print(2)
    quit()
for _ in range(len(s)+1):
    cnt=1
    result=''
    for i in range(1, len(s)):
        if s[i-1]==s[i]:
            cnt+=1
        elif s[i-1]!=s[i]:
            result+=s[i-1]+str(cnt)
            cnt=1
        if i==len(s)-1:
            result+=s[i]+str(cnt)
    s.rotate(1)
    answers.append(len(result))
print(min(answers))
