# 문제
# 정수 x가 주어졌을 때, 10보다 크다면, 1의 자리에서 반올림하고, 결과가 100보다 크면, 10의 자리에서 반올림하고, 1000보다 크면, 100의 자리에서 반올림하고... 이와 같이 계속 반올림하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수 n이 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 정수 x가 주어진다. (0 ≤ x ≤ 99999999)
#
# 출력
# 각 테스트 케이스마다 입력으로 주어지는 정수를 문제 설명에 나온 것처럼 반올림한 결과를 출력한다.
n=int(input())
for i in range(n):
    num=int(input())
    cal=10
    while num>cal:
        if num%cal>=cal/2:
            num=((num//cal)+1)*cal
        else:
            num=(num//cal)*cal
        cal*=10
    print(num)
