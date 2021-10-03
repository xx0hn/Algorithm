/*
 문제
 RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
 N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
 i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
 입력
 첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

 출력
 첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.
*/
#include <iostream>
#define endl "\n"
#define MAX 1000+1
using namespace std;

int n, answer;
int MAP[MAX][3];
int DP[MAX][3];

int Min(int a, int b){if (a<b) return a; return b;}

void Input()
{
    cin>>n;
    for(int i=1; i<=n; i++)
    {
        for(int j=0; j<3; j++)
        {
            cin>>MAP[i][j];
        }
    }
    MAP[0][0]=MAP[0][1]=MAP[0][2]=0;
    DP[0][0]=DP[0][1]=DP[0][2]=0;
}
void Solution()
{
    for(int i=1; i<=n; i++)
    {
        DP[i][0]=Min(DP[i-1][1], DP[i-1][2])+MAP[i][0];
        DP[i][1]=Min(DP[i-1][0], DP[i-1][2])+MAP[i][1];
        DP[i][2]=Min(DP[i-1][0], DP[i-1][1])+MAP[i][2];
    }
    answer=Min(Min(DP[n][0], DP[n][1]), DP[n][2]);
    cout<<answer<<endl;
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
