# 문제
# 0과 1로 이루어진 길이가 무한한 문자열 X가 있다. 이 문자열은 다음과 같은 과정으로 만들어진다.
#
# X는 맨 처음에 "0"으로 시작한다.
# X에서 0을 1로, 1을 0으로 뒤바꾼 문자열 X'을 만든다.
# X의 뒤에 X'를 붙인 문자열을 X로 다시 정의한다.
# 2~3의 과정을 무한히 반복한다.
# 즉, X는 처음에 "0"으로 시작하여 "01"이 되고, "0110"이 되고, "01101001"이 되고, ⋯ 의 과정을 거쳐 다음과 같이 나타내어진다.
#
#     "011010011001011010010110011010011001011001101001⋯⋯"
#
# 자연수 k가 주어졌을 때 X의 k번째에는 무슨 문자가 오는지 구하여라.
#
# 입력
# 첫 번째 줄에 자연수 k (1 ≤ k ≤ 1018) 가 주어진다.
#
# 출력
# 첫 번째 줄에 k번째에 오는 문자를 출력하라.
def recursion(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n%2:
        return 1-recursion(n//2)
    else:
        return recursion(n//2)
k=int(input())
print(recursion(k-1))
