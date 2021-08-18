/*
 문제
 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

 입력
 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

 출력
 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

 예제 입력 1
 5
 예제 출력 1
 *        *
 **      **
 ***    ***
 ****  ****
 **********
 ****  ****
 ***    ***
 **      **
 *        *
 */
#include <iostream>
using namespace std;

int n;

void Input(){
    cin>>n;
}

void Solution(){
    for (int i=1; i<=n; i++){
        for(int j=1; j<=i; j++){
            cout<<"*";
        }
        for(int j=1; j<=2*(n-i); j++){
            cout<<" ";
        }
        for(int j=1; j<=i; j++){
            cout<<"*";
        }
        cout<<endl;
    }
    for (int i=1; i<=n-1; i++){
        for (int j=i; j<n; j++){
            cout<<"*";
        }
        for (int j=1; j<=2*i; j++){
            cout<<" ";
        }
        for (int j=i; j<n; j++){
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
