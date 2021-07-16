/*
 문제
 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

 입력
 첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

 출력
 총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.
 */
#include <iostream>
#define MAX 100001
using namespace std;

int n, m;
int arr[MAX];
int psum[MAX];
int a, b;

void Input(){
    cin>>n>>m;
    for(int i=1; i<=n; i++){
        cin>>arr[i];
        if(i==1)
            psum[i]==arr[i];
        psum[i]=psum[i-1]+arr[i];
    }
}

int Solution(int a, int b){
    return psum[b]-psum[a-1];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    for(int j=0; j<m; j++){
        cin>>a>>b;
        cout<<Solution(a, b)<<'\n';
    }
    return 0;
}
