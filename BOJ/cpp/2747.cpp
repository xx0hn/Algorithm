/*
 문제
 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

 n=17일때 까지 피보나치 수를 써보면 다음과 같다.

 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

 n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

 입력
 첫째 줄에 n이 주어진다. n은 45보다 작거나 같은 자연수이다.

 출력
 첫째 줄에 n번째 피보나치 수를 출력한다.
 */
#include <iostream>
#define MAX 46
using namespace std;

int n;
int fibo[MAX];
int result;


void Input(){
    cin>>n;
}

int Fibo(int num){
    fibo[0]=0;
    fibo[1]=1;
    for(int i=2; i<=num; i++){
        fibo[i]=fibo[i-1]+fibo[i-2];
    }
    result=fibo[num];
    return result;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    cout<<Fibo(n)<<endl;
    return 0;
}
