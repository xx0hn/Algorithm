/*
 문제
 체스판은 8*8크기이고, 검정 칸과 하얀 칸이 번갈아가면서 색칠되어 있다. 가장 왼쪽 위칸 (0,0)은 하얀색이다. 체스판의 상태가 주어졌을 때, 하얀 칸 위에 말이 몇 개 있는지 출력하는 프로그램을 작성하시오.

 입력
 첫째 줄부터 8개의 줄에 체스판의 상태가 주어진다. ‘.’은 빈 칸이고, ‘F’는 위에 말이 있는 칸이다.

 출력
 첫째 줄에 문제의 정답을 출력한다.
 */
#include <iostream>
#define MAX 9
using namespace std;

char board[MAX][MAX];
int cnt=0;

void Input(){
    for(int i=0; i<8; i++){
        for(int j=0; j<8; j++){
            cin>>board[i][j];
        }
    }
}

void Solution(){
    for(int i=0; i<8; i++){
        if(i%2==0){
            for(int j=0; j<8; j++){
                if(j%2==0&&board[i][j]=='F'){
                    cnt++;
                }
            }
        }
        else{
            for(int j=0; j<8; j++){
                if(j%2==1&&board[i][j]=='F'){
                    cnt++;
                }
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    Solution();
    cout<<cnt<<endl;
    return 0;
}
