/*
 문제
 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

 입력
 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

 출력
 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
 */
#include <iostream>
#include <queue>
#include <cstring>
#define MAX 1001
using namespace std;

int n, m, v;
int graph[MAX][MAX];
bool visited[MAX];
queue<int> q;
int a,b;

void Input(){
    cin>>n>>m>>v;
    for(int i=0; i<m; i++){
        cin>>a>>b;
        graph[a][b]=1;
        graph[b][a]=1;
    }
}

void Initialize(){
    for(int i=0; i<=n; i++){
        visited[i]=0;
    }
}

void DFS(int v){
    visited[v]=1;
    cout<<v<<" ";
    for(int i=1; i<=n; i++){
        if(graph[v][i]==1 && visited[i]==0){
            DFS(i);
        }
    }
}

void BFS(int v){
    q.push(v);
    visited[v]=1;
    
    while(!q.empty()){
        v=q.front();
        q.pop();
        cout<<v<<" ";
        
        for(int j=1; j<=n; j++){
            if(graph[v][j]==1 && visited[j]==0){
                q.push(j);
                visited[j]=1;
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    Initialize();
    DFS(v);
    cout<<endl;
    Initialize();
    BFS(v);
    return 0;
}
