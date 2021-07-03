/*
 문제
 N×M크기의 배열로 표현되는 미로가 있다.

 1    0    1    1    1    1
 1    0    1    0    1    0
 1    0    1    0    1    1
 1    1    1    0    1    1
 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

 입력
 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

 출력
 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
 */

#include <iostream>
#include <queue>
#include <string>
#define MAX 101
using namespace std;

string mrr[MAX];
bool check[MAX][MAX];
int cnt[MAX][MAX];

queue<pair<int, int>> Q;
int n,m;

int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};

void Input(){
    cin>>n>>m;
    for(int i=0; i<n; i++){
        cin>>mrr[i];
    }
}

void Init(){
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            check[i][j]=false;
        }
    }
}


void BFS(){
    cnt[0][0]=1;
    Q.push({0, 0});
    check[0][0]=true;
    while(!Q.empty()){
        pair<int, int> curr = Q.front();
        Q.pop();
        for(int k=0; k<4; k++){
            int nx=curr.first+dx[k];
            int ny=curr.second+dy[k];
            
            if(nx<0 || nx>=n || ny<0 || ny>=m){
                continue;
            }
            if(mrr[nx][ny]=='0'||check[nx][ny]){
                continue;
            }
            cnt[nx][ny]=cnt[curr.first][curr.second]+1;
            Q.push({nx, ny});
            check[nx][ny]=true;
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    Init();
    BFS();
    cout<<cnt[n-1][m-1]<<endl;
    return 0;
}

