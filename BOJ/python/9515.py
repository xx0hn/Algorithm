# 문제
# 선영이는 다가오는 COCI에 사용할 데이터를 만드느라 삼일동안 깨어있었다. 더 이상 데이터를 만들 수 없는 상황에 이르렀고, 심지어 선영이는 신경쇠약에 걸려 아무것도 제대로 보지 못하는 상황이 되었다.
#
# 선영이가 무엇인가를 읽다가 눈을 한 번 깜박하면 단어의 뒷 부분 절반이 앞 부분과 섞이게 된다. (길이가 홀수인 경우에는 뒷 부분의 길이가 짧다) 섞이는 방법은 아래와 같다.
#
# 마지막 글자가 첫 번째 글자와 두 번째 글자 사이로 이동한다.
# 뒤에서 두 번째 글자가 두 번째 글자와 세 번째 글자 사이로 이동한다.
# 뒤에서 k번째 글자는 앞에서부터 k번째와 k+1번째 글자 사이로 이동한다.
# 예를 들어, 선영이가 "abcdef"란 단어를 보다가 눈을 한 번 깜박이면, 단어가 "afbecd"가 된다. 여기서 한 번 더 깜박이면 "adfcbe"가 된다.
#
# 선영이는 한 단어를 쓰고난 이후에 눈을 X번 깜박였고, 처음에 작성한 단어가 무엇인지 궁금해졌다. X와 눈을 X번 깜박인 후에 선영이가 보고 있는 단어가 주어졌을 때, 원래 단어가 무엇이었는지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 X(1 ≤ X ≤ 1,000,000,000) 가 주어지고, 둘째 줄에 X번 깜박인 후의 단어가 주어진다. 단어는 알파벳 소문자로만 이루어져 있고, 길이는 구간 [3,1000]에 포함된다.
#
# 출력
# 첫째 줄에 X번 깜박이기 전 단어를 출력한다.
x = int(input())
after = list(str(input()))
tmp = after[:]
def blinking():
    before = ['' for _ in range(len(after))]
    left = 0
    right = len(after) - 1
    for i in range(len(after)):
        if i % 2 == 0:
           before[left] = after[i]
           left += 1
        else:
            before[right] = after[i]
            right -= 1
    return before
visited = [tuple(after)]
for _ in range(x):
    after = blinking()
    if tuple(after) not in set(visited):
        visited.append(tuple(after))
    else:
        break
x %= len(visited)
after = tmp[:]
for _ in range(x):
    after = blinking()
print(''.join(after))
