#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#define MAX 26
using namespace std;

int n;
string a;
int graph[MAX][MAX];
bool visited[MAX][MAX];
int dy[4]={0,1,0,-1};
int dx[4]={1,0,-1,0};
int cnt=0;
vector<int> result;

void Input(){
    cin>>n;
    for(int i=0; i<n; i++){
        cin>>a;
        for(int j=0; j<n; j++){
            graph[i][j]=a[j]-'0';
        }
    }
}

void DFS(int y, int x){
    cnt++;
    visited[y][x]=true;
    for(int i=0; i<4; i++){
        int ny=dy[i]+y;
        int nx=dx[i]+x;
        if((ny>=0&&nx>=0&&ny<n&&nx<n)&&graph[ny][nx]==1&&!visited[ny][nx]){
            DFS(ny,nx);
        }
    }
}

void Solution(){
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(graph[i][j]==1&&!visited[i][j]){
                cnt=0;
                DFS(i, j);
                result.push_back(cnt);
            }
        }
    }
    sort(result.begin(), result.end());
    cout<<result.size()<<endl;
    for(int i=0; i<result.size(); i++){
        cout<<result[i]<<endl;
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
