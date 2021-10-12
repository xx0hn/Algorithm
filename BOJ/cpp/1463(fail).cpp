/*
 문제
 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

 X가 3으로 나누어 떨어지면, 3으로 나눈다.
 X가 2로 나누어 떨어지면, 2로 나눈다.
 1을 뺀다.
 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

 입력
 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

 출력
 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
*/
#include <iostream>
#define endl "\n"
#define MAX 1000000+1
using namespace std;

int n, arr[MAX];

int Min(int a, int b)
{
    if(a<b)
        return a;
    return b;
}

void Input()
{
    cin>>n;
}

void Solution()
{
    arr[0]=0;
    arr[1]=0;
    
    for(int i=2; i<=n; i++)
    {
        arr[i]=arr[i-1]+1;
        if(i%2==0) arr[i]=Min(arr[i], arr[i/2]+1);
        if(i%3==0) arr[i]=Min(arr[i], arr[i/3]+1);
    }
    cout<<arr[n]<<endl;
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
