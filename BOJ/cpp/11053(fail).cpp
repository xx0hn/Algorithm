//
//  main.cpp
//  practice.cpp
//
//  Created by 황승환 on 2020/05/06.
//  Copyright © 2020 황승환. All rights reserved.
//

/*
 문제
 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

 입력
 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

 출력
 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
*/

#include <iostream>
#include <cstring>
#define endl "\n"
#define MAX 1000+1
using namespace std;

int n;
int Arr[MAX];
int DP[MAX];
int sum=0;

void Input()
{
    cin>>n;
    for(int i=0; i<n; i++)
    {
        cin>>Arr[i];
    }
}

void Solution()
{
    for(int i=0; i<n; i++)
    {
        DP[i]=1;
        for(int j=0; j<i; j++)
        {
            if(Arr[i]>Arr[j])
            {
                DP[i]=max(DP[i], DP[j]+1);
            }
        }
        sum=max(sum, DP[i]);
    }
    cout<<sum<<endl;
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
