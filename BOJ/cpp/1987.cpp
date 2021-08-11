/*
 문제
 세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.

 말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

 좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

 입력
 첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1 ≤ R,C ≤ 20) 둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.

 출력
 첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.
 */

#include <iostream>
#include <string>
#include <vector>
#define MAX 21
using namespace std;

int r,c;
string road;
char field[MAX][MAX];
bool visited[26];
int dy[4]={0,1,0,-1};
int dx[4]={1,0,-1,0};
int result=1;

int Big(int a, int b){
    if(a>b)
        return a;
    return b;
}

void Input(){
    cin>>r>>c;
    for(int i=0; i<r; i++){
        cin>>road;
        for(int j=0; j<c; j++){
            field[i][j]=road[j];
        }
    }
}

void DFS(int y, int x, int cnt){
    result=Big(result, cnt);
    for(int i=0; i<4; i++){
        int ny=y+dy[i];
        int nx=x+dx[i];
        
        if(ny>=0&&nx>=0&&ny<r&&nx<c){
            if(!visited[field[ny][nx]-'A']){
                visited[field[ny][nx]-'A']=true;
                DFS(ny, nx, cnt+1);
                visited[field[ny][nx]-'A']=false;
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    visited[field[0][0]-'A']=true;
    DFS(0,0,1);
    cout<<result<<endl;
    return 0;
}
