/*
 문제
 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

 입력
 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

 출력
 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.
 */
#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 500001
using namespace std;

int n;
int m;
int k;

void Solution(){
    cin>>n;
    vector<int> own(n);
    for(int i=0; i<n; i++){
        cin>>own[i];
    }
    sort(own.begin(), own.end());
    cin>>m;
    vector<int> have(m);
    for(int i=0; i<m; i++){
        have[i]=0;
    }
    for(int i=0; i<m; i++){
        cin>>k;
        auto upper=upper_bound(own.begin(), own.end(), k);
        auto lower=lower_bound(own.begin(), own.end(), k);
        have[i]=upper-lower;
    }
    for(int i=0; i<m; i++){
        cout<<have[i]<<" ";
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Solution();
    cout<<endl;
    return 0;
}
