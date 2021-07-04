/*
 문제
 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

 입력
 첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

 출력
 첫째 줄에 자연수 N의 최댓값을 출력한다.
 */
#include <iostream>
using namespace std;

long long S;
long long sum=0;
long long N=0;
long long num=1;

void Input(){
    cin>>S;
}

long long Solution(){
    while(sum<=S){
        sum+=num;
        N++;
        num++;
    }
    N--;
    return N;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    cout<<Solution();
    return 0;
}
