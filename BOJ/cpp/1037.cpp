/*
 문제
 양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다. 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.

 입력
 첫째 줄에 N의 진짜 약수의 개수가 주어진다. 이 개수는 50보다 작거나 같은 자연수이다. 둘째 줄에는 N의 진짜 약수가 주어진다. 1,000,000보다 작거나 같고, 2보다 크거나 같은 자연수이고, 중복되지 않는다.

 출력
 첫째 줄에 N을 출력한다. N은 항상 32비트 부호있는 정수로 표현할 수 있다.
 */
#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 50+1
#define endl "\n"
using namespace std;

int n;
int Arr[MAX];
int answer;

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
    sort(Arr, Arr+n);
    answer=Arr[0]*Arr[n-1];
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
    cin.tie(NULL);
    cout.tie(NULL);
    Solve();
    return 0;
}
