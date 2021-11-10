/*
 문제
 자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

 입력
 첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

 출력
 첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.
 */
#include <iostream>
#include <cmath>
#define endl "\n"
using namespace std;

long long a, b, c;

void Input(){
    cin>>a>>b>>c;
}

long long Pow(long long a, long long b, long long c){
    if(b==0)
        return 1;
    long long result=Pow(a, b/2, c);
    result=result*result%c;
    
    if(b%2==0){
        return result;
    }
    else
        return (result*a)%c;
}

void Solve(){
    Input();
    cout<<Pow(a, b, c)<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    Solve();
    return 0;
}
