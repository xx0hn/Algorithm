/*
 문제
 N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

 입력
 첫째 줄에 N과 K가 주어진다. (1 ≤ K < N ≤ 500,000)

 둘째 줄에 N자리 숫자가 주어진다. 이 수는 0으로 시작하지 않는다.

 출력
 입력으로 주어진 숫자에서 K개를 지웠을 때 얻을 수 있는 가장 큰 수를 출력한다.
 */
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int n, k;
string num;
vector<char> orig;
vector<char> result;

void Input(){
    cin>>n>>k;
    cin>>num;
    for(int i=0; i<n; i++){
        orig.push_back(num[i]);
    }
}

void Solution(){
    int idx=0;
    while(idx!=num.size()){
        while(k!=0&&!result.empty()&&result.back()<orig[idx]){
            result.pop_back();
            k--;
        }
        result.push_back(orig[idx]);
        idx++;
    }
    while(k--){
        result.pop_back();
    }
    for(int i=0; i<result.size(); i++){
        cout<<result[i];
    }
    cout<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    Solution();
    return 0;
}
