# 알파벳과 사칙연산
# ‘a'에서 'f’ 사이의 소문자 알파벳과 +, -, * 기호 만으로 이루어져 있는 길이가 n인 식이 하나 주어집니다. 이때, 각 소문자 알파벳에 1~4 사이의 적절한 숫자를 집어 넣어 식의 결과를 최대로 하는 프로그램을 작성해보세요. 단, 일반 사칙연산 처럼 *가 우선순위가 더 높은 것이 아닌, 모든 연산의 우선순위가 전부 같다고 가정하고 계산해야 합니다. 예를 들어 3 - 2 * 3 은 -3이 아닌 3으로 계산합니다.

# 입력 형식
# 첫 번째 줄에 식이 주어집니다. 식은 ‘a'에서 'f’사이의 소문자 알파벳과 +, -, * 기호만으로 이루어져 있습니다. 알파벳이나 연산자가 연속하여 2번 이상 나타나는 경우 없이 항상 번갈아가며 주어지며, 식의 시작과 마지막에는 반드시 알파벳이 입력된다고 가정해도 좋습니다.

# 1 ≤ 식의 길이(n) ≤ 200
# 출력 형식
# 가능한 최대 결과를 출력합니다. 계산 도중 값이 항상 -2^{31}−2 
# 31
#   ~ 2^{31} - 12 
# 31
#  −1 사이를 벗어나지 않음을 가정해도 좋습니다.

# 입출력 예제
# 예제1
# 입력:

# c-a*b
# 출력:

# 12
# 예제2
# 입력:

# b-a*b-c+b
# 출력:

# 15
# 예제 설명
# 첫 번째 예제에서는 a = 1, b = 4, c = 4일 때 4 - 1 * 4로 최대인 12가 나옵니다.

# 두 번째 예제에서는 a = 1, b = 4, c = 1 일때 4 - 1 * 4 - 1 + 4로 최대인 15가 나옵니다.

# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
import sys
s=str(input())
alph, culc=[], []
for i in s:
    if i.isalpha() and i not in alph:
        alph.append(i)
def get_result(s):
    result=int(s[0])
    idx=1
    while True:
        if idx>=len(s):
            break
        if not s[idx].isdigit():
            if s[idx]=='+':
                result+=int(s[idx+1])
            if s[idx]=='-':
                result-=int(s[idx+1])
            if s[idx]=='*':
                result*=int(s[idx+1])
        idx+=1
    return result
answer=-sys.maxsize
def get_case(ans):
    global answer
    if len(ans)==len(alph):
        tmp_s=s[:]
        for i in range(len(ans)):
            tmp_s=tmp_s.replace(alph[i], str(ans[i]))
        answer=max(answer, get_result(tmp_s))
        return
    for i in range(1, 5):
        get_case(ans+[i])
get_case([])
print(answer)
