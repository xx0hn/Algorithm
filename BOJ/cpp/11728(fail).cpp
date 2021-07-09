/*
 문제
 정렬되어있는 두 배열 A와 B가 주어진다. 두 배열을 합친 다음 정렬해서 출력하는 프로그램을 작성하시오.

 입력
 첫째 줄에 배열 A의 크기 N, 배열 B의 크기 M이 주어진다. (1 ≤ N, M ≤ 1,000,000)

 둘째 줄에는 배열 A의 내용이, 셋째 줄에는 배열 B의 내용이 주어진다. 배열에 들어있는 수는 절댓값이 109보다 작거나 같은 정수이다.

 출력
 첫째 줄에 두 배열을 합친 후 정렬한 결과를 출력한다.
 
 --merge sort
 */
#include <iostream>
#define MAX 1000001
using namespace std;

int n, m;
int a[MAX];
int b[MAX];
int result[2*MAX];
bool check[2*MAX];

void Input(){
    cin>>n>>m;
    for(int i=0; i<n; i++){
        cin>>a[i];
    }
    for(int j=0; j<m; j++){
        cin>>b[j];
        check[j]=false;
    }
}

void Solution(){
    int i=0;
    int j=0;
    int k=0;
    while(i<n&&j<m){
        if(a[i]<b[j]){
            result[k++]=a[i++];
        }
        else
            result[k++]=b[j++];
    }
    while(i<n){
        result[k++]=a[i++];
    }
    while(j<m){
        result[k++]=b[j++];
    }
    for(int l=0; l<n+m; l++){
        cout<<result[l]<<" ";
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
