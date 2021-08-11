/*
 문제
 크기가 N×M인 배열이 있을 때, 배열을 돌려보려고 한다. 배열은 다음과 같이 반시계 방향으로 돌려야 한다.

 A[1][1] ← A[1][2] ← A[1][3] ← A[1][4] ← A[1][5]
    ↓                                       ↑
 A[2][1]   A[2][2] ← A[2][3] ← A[2][4]   A[2][5]
    ↓         ↓                   ↑         ↑
 A[3][1]   A[3][2] → A[3][3] → A[3][4]   A[3][5]
    ↓                                       ↑
 A[4][1] → A[4][2] → A[4][3] → A[4][4] → A[4][5]
 예를 들어, 아래와 같은 배열을 2번 회전시키면 다음과 같이 변하게 된다.

 1 2 3 4       2 3 4 8       3 4 8 6
 5 6 7 8       1 7 7 6       2 7 8 2
 9 8 7 6   →   5 6 8 2   →   1 7 6 3
 5 4 3 2       9 5 4 3       5 9 5 4
  <시작>         <회전1>        <회전2>
 배열과 정수 R이 주어졌을 때, 배열을 R번 회전시킨 결과를 구해보자.

 입력
 첫째 줄에 배열의 크기 N, M과 수행해야 하는 회전의 수 R이 주어진다.

 둘째 줄부터 N개의 줄에 배열 A의 원소 Aij가 주어진다.

 출력
 입력으로 주어진 배열을 R번 회전시킨 결과를 출력한다.
 */
#include <iostream>
#define MAX 301
using namespace std;

int n,m,r;
int arr[MAX][MAX];
int result[MAX][MAX];

void Input(){
    cin>>n>>m>>r;
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            cin>>arr[i][j];
        }
    }
}

void Solution(){
    while(r--){
        int y1=0, x1=0;
        int y2=0, x2=m-1;
        int y3=n-1, x3=m-1;
        int y4=n-1, x4=0;
        while(y1<y4&&x1<x2){
            int temp=arr[y1][x1];
            for(int i=x1; i<x2; i++){
                arr[y1][i] = arr[y1][i+1];
            }
            for(int i=y2; i<y3; i++){
                arr[i][x2] = arr[i+1][x2];
            }
            for(int i=x3; i>x4; i--){
                arr[y3][i] = arr[y3][i-1];
            }
            for(int i=y4; i>y1; i--){
                arr[i][x4] = arr[i-1][x4];
            }
            arr[y1+1][x4] = temp;
            y1++;
            x1++;
            y2++;
            x2--;
            y3--;
            x3--;
            y4--;
            x4++;
        }
    }
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            cout<<arr[i][j]<<" ";
        }
        cout<<endl;
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
