/*
 문제
 배열 A가 주어졌을 때, N번째 큰 값을 출력하는 프로그램을 작성하시오.

 배열 A의 크기는 항상 10이고, 자연수만 가지고 있다. N은 항상 3이다.

 입력
 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 배열 A의 원소 10개가 공백으로 구분되어 주어진다. 이 원소는 1보다 크거나 같고, 1,000보다 작거나 같은 자연수이다.

 출력
 각 테스트 케이스에 대해 한 줄에 하나씩 배열 A에서 3번째 큰 값을 출력한다.
 */
#include <iostream>
#include <algorithm>
#define MAX 1001
using namespace std;

int t;
int arr[10];

void Input(){
    for(int i=0; i<10; i++){
        cin>>arr[i];
    }
}

bool compare(int a, int b){
    if(a>b)
        return true;
    return false;
}

void Solution(){
    sort(arr, arr+10, compare);
    cout<<arr[2]<<endl;
}

void Solve(){
    cin>>t;
    for(int i=0; i<t; i++){
        Input();
        Solution();
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
