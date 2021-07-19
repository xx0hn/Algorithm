/*
 문제
 어떤 자연수 N은 그보다 작거나 같은 제곱수들의 합으로 나타낼 수 있다. 예를 들어 11=32+12+12(3개 항)이다. 이런 표현방법은 여러 가지가 될 수 있는데, 11의 경우 11=22+22+12+12+12(5개 항)도 가능하다. 이 경우, 수학자 숌크라테스는 “11은 3개 항의 제곱수 합으로 표현할 수 있다.”라고 말한다. 또한 11은 그보다 적은 항의 제곱수 합으로 표현할 수 없으므로, 11을 그 합으로써 표현할 수 있는 제곱수 항의 최소 개수는 3이다.

 주어진 자연수 N을 이렇게 제곱수들의 합으로 표현할 때에 그 항의 최소개수를 구하는 프로그램을 작성하시오.

 입력
 첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 100,000)

 출력
 주어진 자연수를 제곱수의 합으로 나타낼 때에 그 제곱수 항의 최소 개수를 출력한다.
 */
#include <iostream>
#include <math.h>
#include <algorithm>
#define MAX 100001
using namespace std;

int n;
int cnt[MAX]={0};

void Input(){
    cin>>n;
}

int Solution(int num){
    for(int i=1; i<=n; i++){
        cnt[i]=i;
        for(int j=1; j<=sqrt(i); j++){
            cnt[i]=min(cnt[i], cnt[i-j*j]+1);
        }
    }
    return cnt[num];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    cout<<Solution(n)<<endl;
    return 0;
}
