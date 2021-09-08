/*
문제

N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

    N개의 자연수 중에서 M개를 고른 수열
    같은 수를 여러 번 골라도 된다.

####입력####

첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 7)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

####출력####

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

제한시간: 1초
문제 출저:https://www.acmicpc.net/problem/15665
*/
#include <iostream>
#include <algorithm>
#include <vector>
#define MAX 8
using namespace std;

int n, m, a;
vector<int> arr;
int result[MAX];
bool num_chk[10001];

void Input(){
    cin>>n>>m;
    for(int i=0; i<n; i++){
        cin>>a;
        if(!num_chk[a]){
            arr.push_back(a);
            num_chk[a]=true;
        }
    }
    sort(arr.begin(), arr.end());
}

void DFS(int cnt){
    if(cnt==m){
        for(int i=0; i<m; i++){
            cout<<result[i]<<" ";
        }
        cout<<"\n";
        return;
    }
    for(int i=0; i<arr.size(); i++){
        result[cnt]=arr[i];
        DFS(cnt+1);
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    DFS(0);
    return 0;
}
