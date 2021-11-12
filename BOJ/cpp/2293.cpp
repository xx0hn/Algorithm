/*
문제

n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다. 이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 

그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.

사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

####입력####

첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다.

####출력####

첫째 줄에 경우의 수를 출력한다. 경우의 수는 2^31보다 작다.

출처:https://www.acmicpc.net/problem/2293
*/
#include <iostream>
#include <cstring>
#define MAX 10001
#define CMAX 101
using namespace std;

int n, k;
int coin[CMAX];
int answer[MAX];

void Input(){
    cin>>n>>k;
    for(int i=0; i<n; i++){
        cin>>coin[i];
    }
    memset(answer, 0, MAX);
    answer[0]=1;
}

void Solution(){
    for(int i=0; i<n; i++){
        for(int j=coin[i]; j<=k; j++){
            if(j-coin[i]>=0)
                answer[j]+=answer[j-coin[i]];
        }
    }
    cout<<answer[k]<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    Solution();
    return 0;
}
