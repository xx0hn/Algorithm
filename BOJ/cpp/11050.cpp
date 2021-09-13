
/*
 문제
 자연수
 과 정수
 가 주어졌을 때 이항 계수
 를 구하는 프로그램을 작성하시오.

 입력
 첫째 줄에
 과
 가 주어진다. (1 ≤
  ≤ 10, 0 ≤
  ≤
 )

 출력
  
 를 출력한다.
 */
#include <iostream>
#define endl "\n"
using namespace std;

int n, k;
int n1=1, nk1=1, k1=1;
int answer;

void Input(){
    cin>>n>>k;
}

void Solution(){
    for(int i=n; i>=1; i--){
        n1*=i;
    }
    for(int i=(n-k); i>=1; i--){
        nk1*=i;
    }
    for(int i=k; i>=1; i--){
        k1*=i;
    }
    answer=n1/(k1*nk1);
    cout<<answer<<endl;
}

void Solve(){
    Input();
    Solution();
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    Solve();
    return 0;
}
