/*
 문제
 어떤 자연수 p와 q가 있을 때, 만일 p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수이다.

 6을 예로 들면

 6 ÷ 1 = 6 … 0
 6 ÷ 2 = 3 … 0
 6 ÷ 3 = 2 … 0
 6 ÷ 4 = 1 … 2
 6 ÷ 5 = 1 … 1
 6 ÷ 6 = 1 … 0
 그래서 6의 약수는 1, 2, 3, 6, 총 네 개이다.

 두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.

 입력
 첫째 줄에 N과 K가 빈칸을 사이에 두고 주어진다. N은 1 이상 10,000 이하이다. K는 1 이상 N 이하이다.

 출력
 첫째 줄에 N의 약수들 중 K번째로 작은 수를 출력한다. 만일 N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 0을 출력하시오.
 */
#include <iostream>
using namespace std;

int n, k;

void Input(){
    cin>>n>>k;
}

int Solution(){
    for(int i=1; i<=n; i++){
        if(n%i==0){
            k--;
        }
        if(k==0){
            return i;
        }
    }
    return 0;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    cout<<Solution()<<endl;
    return 0;
}
