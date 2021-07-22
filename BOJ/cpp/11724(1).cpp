/*
 문제
 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

 입력
 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

 출력
 첫째 줄에 연결 요소의 개수를 출력한다.
 */
#include <iostream>
#include <vector>
#include <queue>
#define MAX 1001
using namespace std;

int n, m;
vector<int> arr[MAX];
int cnt=0;
bool visited[MAX];

void Input(){
    cin>>n>>m;
    for(int i=0; i<m; i++){
        int u,v;
        cin>>u>>v;
        arr[u].push_back(v);
        arr[v].push_back(u);
    }
}

void BFS(int v){
    queue<int> q;
    visited[v]=true;
    q.push(v);
    while(!q.empty()){
        int cur=q.front();
        q.pop();
        for(int i=0; i<arr[cur].size(); i++){
            int next=arr[cur][i];
            if(!visited[next]){
                visited[next]=true;
                q.push(next);
            }
        }
    }
}

void Solution(){
    for(int i=1; i<=n; i++){
        if(!visited[i]){
            BFS(i);
            cnt++;
        }
    }
    cout<<cnt<<endl;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    Solution();
    return 0;
}
