//
//  main.cpp
//  practice.cpp
//
//  Created by 황승환 on 2020/05/06.
//  Copyright © 2020 황승환. All rights reserved.
//

/*
 문제
 nCm의 끝자리 0의 개수를 출력하는 프로그램을 작성하시오.

 입력
 첫째 줄에 정수 n, m(0≤m≤n≤2,000,000,000, n!=0)이 들어온다.

 출력
 첫째 줄에 0의 개수를 출력한다.
 
 nCm=n!/m!(n-m)!
 */
#include <iostream>
#define endl "\n"
using namespace std;

int n,m;
int num1=1, num2=1, num3=1;
int Combination=1;
int cnt2=0, cnt5=0;

void Input(){
    cin>>n>>m;
}

void Solution(){
    for(long long i=5; i<=n; i*=5)
        cnt5+=n/i;
    for(long long i=5; i<=n-m; i*=5)
        cnt5-=(n-m)/i;
    for(long long i=5; i<=m; i*=5)
        cnt5-=m/i;
    for(long long i=2; i<=n; i*=2)
        cnt2+=n/i;
    for(long long i=2; i<=n-m; i*=2)
        cnt2-=(n-m)/i;
    for(long long i=2; i<=m; i*=2)
        cnt2-=m/i;
    if(cnt5>=cnt2)
        cout<<cnt2<<endl;
    else
        cout<<cnt5<<endl;
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
