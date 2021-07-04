/*
 문제
 두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다. 이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다. 예를 들어, 6과 15의 공배수는 30, 60, 90등이 있으며, 최소 공배수는 30이다.

 두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.

 입력
 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 둘째 줄부터 T개의 줄에 걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)

 출력
 첫째 줄부터 T개의 줄에 A와 B의 최소공배수를 입력받은 순서대로 한 줄에 하나씩 출력한다.
 */
#include<iostream>
using namespace std;

int t;
int a, b;

void Init(){
    a=b=0;
}

void Input(){
    cin>>a>>b;
}

int Divide(int x, int y){ //최대공약수
    if(x%y==0){
        return y;
    }
    else
        return Divide(y, x%y);
}

void Print(int x, int y){
    if(x>=y){
        cout<<x*y/Divide(x, y)<<endl;
    }
    else{
        cout<<x*y/Divide(y,x)<<endl;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin>>t;
    for(int i=0; i<t; i++){
        Init();
        Input();
        Print(a, b);
    }
    return 0;
}
