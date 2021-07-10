/*
 문제
 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

 Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

 X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

 입력
 첫째 줄에 N이 주어진다.

 둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

 출력
 첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.
 */
#include <iostream>
#include <algorithm>
#include <vector>
#define MAX 1000001
using namespace std;

int n;
vector<int> x;
vector<int> x2;
int cnt=0;
int result[MAX];

void Input(){
    int a;
    cin>>n;
    for(int i=0; i<n; i++){
        cin>>a;
        x.push_back(a);
        x2.push_back(a);
    }
}

void Solution(){
    sort(x2.begin(), x2.end());
    x2.erase(unique(x2.begin(), x2.end()), x2.end());
    for(int i=0; i<n; i++){
        result[i]=lower_bound(x2.begin(), x2.end(), x[i])-x2.begin();
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    Solution();
    for(int i=0; i<n; i++){
        cout<<result[i]<<" ";
    }
    return 0;
}
