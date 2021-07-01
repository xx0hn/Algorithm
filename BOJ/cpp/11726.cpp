/*
 문제
 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

 아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.



 입력
 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

 출력
 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

 --재귀함수보다 반복문이 더 빠르다...
 
 */
#include <iostream>
#include <cstdio>
#define MAX 1001
using namespace std;

int n;
int cnt=0;
int dp[1000];

void Input(){
    cin>>n;
}

int Solution(int n){
    if(n<=3){
        cnt=n;
        return cnt;
    }
    else{
        cnt=(Solution(n-1)+Solution(n-2))%10007;
        return cnt;
    }
}

int Solution2(int n){
    dp[1]=1;
    dp[2]=2;
    for(int i=3; i<=n; i++){
        dp[i]=(dp[i-1]+dp[i-2])%10007;
    }
    cnt=dp[n];
    return cnt;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    cout<<Solution2(n)<<"\n";
    return 0;
}


