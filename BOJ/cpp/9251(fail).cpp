//
//  main.cpp
//  practice.cpp
//
//  Created by 황승환 on 2020/05/06.
//  Copyright © 2020 황승환. All rights reserved.
//

/*
 문제
 LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

 입력
 첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

 출력
 첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.
*/

#include <iostream>
#include <cstring>
#include <string>
#define endl "\n"
#define MAX 1000+1
using namespace std;

char a[MAX], b[MAX];
int DP[MAX][MAX];

int Bigger(int a, int b){if(a>b)return a;return b;}

void Input()
{
    cin>>a>>b;
}

void Solution()
{
    for(int i=1; i<=strlen(a); i++)
    {
        for(int j=1; j<=strlen(b); j++)
        {
            if(a[i-1]==b[j-1])
                DP[i][j]=DP[i-1][j-1]+1;
            else
                DP[i][j]=Bigger(DP[i-1][j], DP[i][j-1]);
        }
    }
    cout<<DP[strlen(a)][strlen(b)]<<endl;
}

void Solve()
{
    Input();
    Solution();
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    Solve();
    return 0;
}
