//
//*
 문제
 자연수N과 정수K가 주어졌을 때 이항 계수(KN)를 1,000,000,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

 입력
 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 4,000,000, 0 ≤ K ≤ N)

 출력
 (KN)를 1,000,000,007로 나눈 나머지를 출력한다.
 */
#include <iostream>
#define endl "\n"
typedef long long ll;
const int MOD=1000000007;
using namespace std;

int n, k;
ll Inversion(){
    ll ret=1LL;
    ll temp=1LL;
    ll want=MOD-2;
    for(int i=2; i<=k; i++){
        temp*=i;
        temp%=MOD;
    }
    while(want){
        if(want%2){
            ret*=temp;
            ret%=MOD;
        }
        temp*=temp;
        temp%=MOD;
        want/=2;
    }
    return ret%MOD;
}

ll Combi(){
    ll ret=1LL;
    for(int i=n; i>n-k; i--){
        ret*=i;
        ret%=MOD;
    }
    return ret%MOD;
}

void Solution(){
    cin>>n>>k;
    ll a=Inversion();
    ll b=Combi();
    cout<<(a*b)%MOD<<endl;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    Solution();
    return 0;
}
