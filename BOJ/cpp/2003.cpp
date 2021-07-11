/*
 문제
 N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

 입력
 첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어진다. 다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.

 출력
 첫째 줄에 경우의 수를 출력한다.
 */
#include <iostream>
#define MAX 10001
using namespace std;

int n, m;
int A[MAX];
int cnt=0;
int result=0;

void Input(){
    cin>>n>>m;
    for(int i=0; i<n; i++){
        cin>>A[i];
    }
}

void Solution(){
    for(int i=0; i<n; i++){
        cnt=A[i];
        if(A[i]==m){
            result++;
        }
        for(int j=i+1; j<n; j++){
            cnt+=A[j];
            if(cnt==m){
                result++;
            }
            else if(cnt<m){
                continue;
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    Solution();
    cout<<result<<endl;
    return 0;
}
