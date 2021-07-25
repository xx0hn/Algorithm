/*
 문제
 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

 2를 곱한다.
 1을 수의 가장 오른쪽에 추가한다.
 A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

 입력
 첫째 줄에 A, B (1 ≤ A < B ≤ 109)가 주어진다.

 출력
 A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.
 */
#include <iostream>
#include <algorithm>
#define MAX 1000000
using namespace std;

long long a, b;
long long cnt=1;
long long result=MAX;


void Input(){
    cin>>a>>b;
}

void DFS(long long n, long long cnt){
    if(n==b){
        result=min(cnt, result);
    }
    if(n>b)
        return;
    DFS(n*2, cnt+1);
    DFS((n*10)+1, cnt+1);
}

void Solution(){
    DFS(a, cnt);
    if(result==MAX){
        cout<<-1<<endl;
    }
    else{
        cout<<result<<endl;
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
