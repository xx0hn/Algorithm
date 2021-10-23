/*
 문제
 I'm 23 난 수수께끼

 뭐게요 맞혀봐요

 - 아이유, 스물셋 中

  $23$으로만 이루어진 수는 $23$, $2\,323$, $232\,323$, … 등이 있다.

  $23$으로만 이루어진 수의 합으로 나타낼 수 있는 수는 $23$, $2\,323$, $46(23+23)$, $2\,346(2\,323+23)$, $23\,234\,692(23\,232\,323+2\,323+23+23)$ 등이 있다.

  $23$으로만 이루어진 수의 합으로 나타낼 수 있는 모든 수 중 $k$번째로 작은 수를 구하시오.

 입력
 첫째 줄에 테스트 케이스의 수 $T$가 주어진다.

 둘째 줄부터 $T$줄에 걸쳐 정수 $k$가 주어진다.

 출력
  $T$개의 줄에 걸쳐 답을 순서대로 출력한다.
 */
#include <iostream>
using namespace std;

int t, k;

void Input(){
    cin>>k;
}

void Solution(){
    cout<<k*23<<'\n';
}

void Solve(){
    cin>>t;
    for(int i=0; i<t; i++){
        Input();
        Solution();
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
