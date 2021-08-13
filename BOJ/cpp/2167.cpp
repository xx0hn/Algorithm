/*
 문제
 2차원 배열이 주어졌을 때 (i, j) 위치부터 (x, y) 위치까지에 저장되어 있는 수들의 합을 구하는 프로그램을 작성하시오. 배열의 (i, j) 위치는 i행 j열을 나타낸다.

 입력
 첫째 줄에 배열의 크기 N, M(1 ≤ N, M ≤ 300)이 주어진다. 다음 N개의 줄에는 M개의 정수로 배열이 주어진다. 배열에 포함되어 있는 수는 절댓값이 10,000보다 작거나 같은 정수이다. 그 다음 줄에는 합을 구할 부분의 개수 K(1 ≤ K ≤ 10,000)가 주어진다. 다음 K개의 줄에는 네 개의 정수로 i, j, x, y가 주어진다(i ≤ x, j ≤ y).

 출력
 K개의 줄에 순서대로 배열의 합을 출력한다. 배열의 합은 231-1보다 작거나 같다.
 */
#include <iostream>
#define MAX 301
using namespace std;

int n, m;
int arr[MAX][MAX];
int k;
int i,j,x,y;

void Input(){
    cin>>n>>m;
    for(int i=1; i<=n; i++){
        for(int j=1; j<=m; j++){
            cin>>arr[i][j];
        }
    }
    cin>>k;
}

void Solution(){
    int sum=0;
    for(int l=i; l<=x; l++){
        for(int k=j; k<=y; k++){
            sum+=arr[l][k];
        }
    }
    cout<<sum<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    for(int h=0; h<k; h++){
        cin>>i>>j>>x>>y;
        Solution();
    }
    return 0;
}
