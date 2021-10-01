/*
 문제

 Moo는 술자리에서 즐겁게 할 수 있는 게임이다. 이 게임은 Moo수열을 각 사람이 하나씩 순서대로 외치면 되는 게임이다.

 Moo 수열은 길이가 무한대이며, 다음과 같이 생겼다.

     m o o m o o o m o o m o o o o m o o m o o o m o o m o o o o o

 Moo 수열은 다음과 같은 방법으로 재귀적으로 만들 수 있다. 먼저, S(0)을 길이가 3인 수열 "m o o"이라고 하자. 1보다 크거나 같은 모든 k에 대해서, S(k)는 S(k-1)과 o가 k+2개인 수열 "m o ... o" 와 S(k-1)을 합쳐서 만들 수 있다.

     S(0) = "m o o"
     S(1) = "m o o m o o o m o o"
     S(2) = "m o o m o o o m o o m o o o o m o o m o o o m o o"

 위와 같은 식으로 만들면, 길이가 무한대인 문자열을 만들 수 있으며, 그 수열을 Moo 수열이라고 한다.

 N이 주어졌을 때, Moo 수열의 N번째 글자를 구하는 프로그램을 작성하시오.

 ####입력####

 첫째 줄에 N (1 ≤ N ≤ 10^9)이 주어진다.

 ####출력####

 N번째 글자를 출력한다.

 출처: https://www.acmicpc.net/problem/5904
 */
#include <iostream>
using namespace std;

long long n;
char s[3]={'m','o','o'};

void Input(){
    cin>>n;
}

void Solution(long long n1, long long k, long long len){
    long long nlen=len*2+k+3;
    if(n1<=3){
        cout<<s[n1-1]<<endl;
        exit(0);
    }
    if(nlen>=n1){
        if(n1>len&&n1<=len+k+3){
            if(n1-len!=1){
                cout<<"o"<<endl;
                exit(0);
            }
            else{
                cout<<"m"<<endl;
                exit(0);
            }
        }
        else{
            Solution(n1-(len+k+3), 1, 3);
        }
    }
    else{
        Solution(n1, k+1, nlen);
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    Solution(n,1,3);
    return 0;
}
