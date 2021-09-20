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
#define MAX 1001
#define Moduler 10007
using namespace std;

int n, k;
int DP[MAX][MAX];

void Input(){
    cin>>n>>k;
}

void Solution(){
    for(int i=1; i<=n; i++){
        DP[i][1]=i;
        DP[i][i]=DP[i][0]=1;
    }
    for(int i=3; i<=n; i++){
        for(int j=2; j<i; j++){
            DP[i][j]=(DP[i-1][j-1]+DP[i-1][j])%Moduler;
        }
    }
    cout<<DP[n][k]%Moduler<<endl;
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
