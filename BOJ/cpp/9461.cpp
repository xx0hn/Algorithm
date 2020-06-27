//
//  main.cpp
//  practice.cpp
//
//  Created by 황승환 on 2020/05/06.
//  Copyright © 2020 황승환. All rights reserved.
//

/*
 문제
 오른쪽 그림과 같이 삼각형이 나선 모양으로 놓여져 있다. 첫 삼각형은 정삼각형으로 변의 길이는 1이다. 그 다음에는 다음과 같은 과정으로 정삼각형을 계속 추가한다. 나선에서 가장 긴 변의 길이를 k라 했을 때, 그 변에 길이가 k인 정삼각형을 추가한다.

 파도반 수열 P(N)은 나선에 있는 정삼각형의 변의 길이이다. P(1)부터 P(10)까지 첫 10개 숫자는 1, 1, 1, 2, 2, 3, 4, 5, 7, 9이다.

 N이 주어졌을 때, P(N)을 구하는 프로그램을 작성하시오.

 입력
 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. (1 ≤ N ≤ 100)

 출력
 각 테스트 케이스마다 P(N)을 출력한다.
 
 
 p[1]=1, p[2]=1, p[3]=1, p[4]=2, p[5]=2, p[6]=3, p[7]=4, p[8]=5, p[9]=7, p[10]=9
 p[n]=p[n-3]+p[n-2];
*/
#include <iostream>
#define endl "\n"
#define MAX 100+1
using namespace std;

int n, t;
long long p[MAX];

void Input()
{
    cin>>n;
}
void Solution()
{
    p[1]=1;
    p[2]=1;
    p[3]=1;
    p[4]=2;
    for(int i=5; i<=t; i++)
    {
        p[i]=p[i-3]+p[i-2];
    }
    cout<<p[t]<<endl;
}
void Solve()
{
    Input();
    for(int i=0; i<n; i++)
    {
        cin>>t;
        Solution();
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
