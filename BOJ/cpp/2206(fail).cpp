/*
 문제
 N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

 한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

 맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

 입력
 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

 출력
 첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.
 */
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <string>
#define MAX 1001
using namespace std;

int n,m;
string line;
int graph[MAX][MAX];
bool visited[MAX][MAX][2];
int dy[4]={0,1,0,-1};
int dx[4]={1,0,-1,0};

void Input(){
    cin>>n>>m;
    for(int i=0; i<n; i++){
        cin>>line;
        for(int j=0; j<m; j++){
            graph[i][j]=line[j]-'0';
        }
    }
}

int BFS(){
    queue<pair<pair<int, int>, pair<int, int>>> q;
    q.push(make_pair(make_pair(0, 0), make_pair(0, 1)));
    visited[0][0][0]=true;
    while(!q.empty()){
        int y=q.front().first.first;
        int x=q.front().first.second;
        int block=q.front().second.first;
        int cnt=q.front().second.second;
        q.pop();
        if(y==n-1&&x==m-1)
            return cnt;
        for(int i=0; i<4; i++){
            int ny=dy[i]+y;
            int nx=dx[i]+x;
            if(ny>=0&&nx>=0&&ny<n&&nx<m){
                if(graph[ny][nx]==1&&block==0){
                    visited[ny][nx][block+1]=true;
                    q.push(make_pair(make_pair(ny,nx), make_pair(block+1, cnt+1)));
                }
                else if(graph[ny][nx]==0&&!visited[ny][nx][block]){
                    visited[ny][nx][block]=true;
                    q.push(make_pair(make_pair(ny, nx), make_pair(block, cnt+1)));
                }
            }
        }
    }
    return -1;
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    cout<<BFS()<<endl;
    return 0;
}
