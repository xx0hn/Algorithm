/*
 문제
 수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다.

 김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다.

 참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)

 수강신청 대충한 게 찔리면, 선생님을 도와드리자!

 입력
 첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)

 이후 N개의 줄에 Si, Ti가 주어진다. (1 ≤ Si < Ti ≤ 109)

 출력
 강의실의 개수를 출력하라.
 */
#include <iostream>
#include <queue>
#include <algorithm>
#define MAX 200001
using namespace std;

int n;
int a, b;
pair<int, int> p[MAX];
priority_queue<int, vector<int>, greater<int>> pq;
int classroom=0;

void Input(){
    cin>>n;
    for(int i=0; i<n; i++){
        cin>>p[i].first>>p[i].second;
    }
}

void Solution(){
    sort(p, p+n);
    pq.push(p[0].second);
    for(int i=1; i<n; i++){
        if(pq.top()<=p[i].first){
            pq.pop();
            pq.push(p[i].second);
        }
        else{
            pq.push(p[i].second);
        }
    }
    classroom=(int)pq.size();
    cout<<classroom<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    Solution();
    return 0;
}

