# 아름다운 수
# 1-4 사이의 숫자로만 이루어져 있으면서, 정확히 해당 숫자만큼 연달아 같은 숫자가 나오는 숫자를 아름다운 수 라고 부릅니다.

# 예를 들어 1333221는 1이 1번, 3이 3번, 2가 2번 그리고 1이 1번 연속하여 나오므로 아름다운 수 입니다.

# 이때 동일한 숫자에 대해 연달아 같은 숫자의 묶음이 나오는 것 또한 아름다운 수 입니다. 예를 들어 111, 22222222와 같은 수 역시 1이 1번 나온 것이 3번 반복되었고, 2가 2번 나온 것이 4번 반복되었다고 할 수 있기 때문에 아름다운 수라고 할 수 있습니다.
# 다만, 222의 경우에는 2가 2번 나온 뒤, 다시 2가 1번 나왔으므로 아름다운 수가 아닙니다.

# n자리 아름다운 수가 몇 개 있는지를 구하는 프로그램을 작성해보세요.

# 입력 형식
# 첫 번째 줄에는 n이 주어집니다.

# 1 ≤ n ≤ 10
# 출력 형식
# n자리 아름다운 수의 개수를 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 1
# 출력:

# 1
# 예제2
# 입력:

# 3
# 출력:

# 4
# 예제 설명
# 두 번째 예제에서는 3자리인 아름다운 수에 111, 122, 221, 333이 있으므로 답이 4가 됩니다.

# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
n=int(input())
answers=[]
def chk(num):
    idx=0
    while idx<n:
        if idx+int(num[idx])-1>=n:
            return False
        for i in range(idx, idx+int(num[idx])):
            if num[i]!=num[idx]:
                return False
        idx+=int(num[idx])
    return True
def Backtracking(num):
    if len(num)==n:
        if chk(num):
            answers.append(num)
        return
    for i in range(1, 5):
        Backtracking(num+str(i))
Backtracking('')
print(len(answers))
