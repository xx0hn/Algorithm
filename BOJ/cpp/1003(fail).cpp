//
//  main.cpp
//  practice.cpp
//
//  Created by 황승환 on 2020/05/06.
//  Copyright © 2020 황승환. All rights reserved.
//

/*
 문제
 다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.
 int fibonacci(int n) {
     if (n == 0) {
         printf("0");
         return 0;
     } else if (n == 1) {
         printf("1");
         return 1;
     } else {
         return fibonacci(n‐1) + fibonacci(n‐2);
     }
 }
 fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.

 fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
 fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
 두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
 fibonacci(0)은 0을 출력하고, 0을 리턴한다.
 fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
 첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
 fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
 1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

 입력
 첫째 줄에 테스트 케이스의 개수 T가 주어진다.

 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

 출력
 각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.
 첫째 줄에 n번째 피보나치 수를 출력한다.
*/
#include <iostream>
#include <cstring>
#define endl "\n"
#define MAX 41
using namespace std;

int n, zerocnt, onecnt;
int DP[MAX][2];

void Initialize()
{
    memset(DP, 0, sizeof(DP));
    zerocnt=0;
    onecnt=0;
}
void Input()
{
    cin>>n;
}
void Solution()
{
    DP[0][1]=DP[1][0]=0;
    DP[0][0]=DP[1][1]=1;
    for(int i=2; i<=n; i++)
    {
        DP[i][0]=DP[i-1][0]+DP[i-2][0];
        DP[i][1]=DP[i-1][1]+DP[i-2][1];
    }
}
void Solve()
{
    int t;
    cin>>t;
    for(int i=1; i<=t; i++)
    {
        Initialize();
        Input();
        Solution();
        
        cout<<DP[n][0]<<" "<<DP[n][1]<<endl;
    }
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
