/*
 문제
 N개의 수가 주어졌을 때, 이를 비내림차순으로 정렬하는 프로그램을 작성하시오.

 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

 입력
 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이며, 같은 수가 여러 번 중복될 수도 있다.

 출력
 첫째 줄부터 N개의 줄에 비내림차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
 */
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n;
vector<int> result;

void Input(){
    cin>>n;
    for(int i=0; i<n; i++){
        int a;
        cin>>a;
        result.push_back(a);
    }
}

void Solution(){
    sort(result.begin(), result.end());
    for(int i=0; i<n; i++){
        cout<<result[i]<<"\n";
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    Solution();
    return 0;
}
