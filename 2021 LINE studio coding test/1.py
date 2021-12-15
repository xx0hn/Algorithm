# 문제 설명
# 문자열 source가 매개변수로 주어집니다. 다음과 같은 방식을 통해 source로부터 새로운 문자열을 만들어 return하도록 solution함수를 완성해주세요.
# 1. 새로운 문자열 dest를 만듭니다.
# 2. source가 빈 문자열일 경우, dest를 return하고 과정을 종료합니다.
# 3. source에 있는 모든 알파벳을 종류별로 1개씩만 제거한 뒤 해당 알파벳들을 dest의 맨 뒤에 알파벳 순서대로 이어붙입니다. 예를 들어 source="bbadd"인 경우 a 1개, b 1개, d 1개를 제거하여 dest의 맨 뒤에 이어 붙입니다. 그 결과 source는 "bd"가 되며, dest의 맨 뒤에 "abd"가 이어 붙여집니다. source에 동일한 알파벳이 여러 개 있다면 그 중 어떤 것을 골라도 상관 없습니다.
# 4. 2번 과정으로 돌아갑니다.
# 제한 사항
# - 1<=source의 길이<=200
# - source는 영어 소문자로 이루어져 있습니다.
def solution(source):
  dest=[]
  source_tmp=list(source)
  while len(source_tmp)>0:
      tmp=set(source_tmp)
      tmp=sorted(tmp)
      for i in tmp:
          dest.append(i)
      for i in tmp:
          source_tmp.pop(source_tmp.index(i))
  result=''
  for i in dest:
      result+=i
  return result
