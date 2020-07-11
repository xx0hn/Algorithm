//
//  main.cpp
//  practice.cpp
//
//  Created by 황승환 on 2020/05/06.
//  Copyright © 2020 황승환. All rights reserved.
//

/*
 문제
 45656이란 수를 보자.

 이 수는 인접한 모든 자리수의 차이가 1이 난다. 이런 수를 계단 수라고 한다.

 세준이는 수의 길이가 N인 계단 수가 몇 개 있는지 궁금해졌다.

 N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. (0으로 시작하는 수는 없다.)

 입력
 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

 출력
 첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.
*/

#include <iostream>
#define endl "\n"
#define MAX 100+1
#define Moduler 1000000000
typedef long long ll;
using namespace std;

int n;
ll answer;
ll DP[MAX][11];

void Input()
{
    cin>>n;
}

void Solution()
{
    for(int i=1; i<=9; i++)
    {
        DP[1][i]=1;
    }
    DP[1][0]=0;
    for(int i=2; i<=n; i++)
    {
        for(int j=0; j<=9; j++)
        {
            if(j==0)
                DP[i][j]=DP[i-1][j+1]%Moduler;
            else if(j==9)
                DP[i][j]=DP[i-1][j-1]%Moduler;
            else
                DP[i][j]=(DP[i-1][j+1]+DP[i-1][j-1])%Moduler;
        }
    }
    for(int i=0; i<10; i++)
    {
        answer+=DP[n][i];
    }
    cout<<answer%1000000000<<endl;
}

void Solve()
{
    Input();
    Solution();
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
