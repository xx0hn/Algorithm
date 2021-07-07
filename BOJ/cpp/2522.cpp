/*
 문제
 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

 입력
 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

 출력
 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
 예제 입력 1
 3
 예제 출력 1
   *
  **
 ***
  **
   *
 */
#include <iostream>
using namespace std;

int n;

void Input(){
    cin>>n;
}

void Solution(){
    for(int i=1; i<=n; i++){
        for(int l=1; l<=n-i; l++){
            cout<<" ";
        }
        for(int j=1; j<=i; j++){
            cout<<"*";
        }
        cout<<endl;
    }
    for(int i=n; i>0; i--){
        for(int l=n-i+1; l>0; l--){
            cout<<" ";
        }
        for(int j=i-1; j>0; j--){
            cout<<"*";
        }
        cout<<endl;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    Solution();
    return 0;
}
