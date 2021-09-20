/*
 문제

 승용이는 트리 모양의 길 위에서 오토바이를 타고 전단지를 돌리려고 한다. 승용이의 목표는 케니소프트에서 출발하여 모든 노드에 전단지를 돌리고, 다시 케니소프트로 돌아오는 것이다.

 승용이는 힘이 좋기 때문에 현재 노드에서 거리가 D 이하인 모든 노드에 전단지를 돌릴 수 있다.

 날씨가 매우 덥기 때문에, 현민이는 최소한만 이동해서 목표를 달성하고 싶다! 승용이를 위해 승용이가 이동해야 하는 총 거리를 구해주자.

 ####입력####

 첫번째 줄에는 노드의 개수 N(1≤N≤100000)과 케니소프트의 위치 S(1≤S≤N), 힘 D(0≤D≤N)이 주어진다.

 두 번째 줄부터 N번째 줄까지, 트리의 간선 정보를 의미하는 두 자연수 x, y가 공백으로 구분되어 주어진다. 이는 x번 노드와 y번 노드가 연결되어 있음을 의미한다.
 (1≤x, y≤N, x≠y)

 주어지는 연결관계는 트리를 구성하며, 모든 간선의 길이는 1이다.

 ####출력####

 승용이가 목표를 완수하기 위해 이동해야 하는 최소 거리를 출력하여라.

 출처: https://www.acmicpc.net/problem/19542
 */
#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 100001
using namespace std;

int n,s,d;
vector<int> road[MAX];
vector<int> depth;
vector<int> maxDepth;
int cnt=0;

void Input(){
    cin>>n>>s>>d;
    for(int i=0; i<n-1; i++){
        int a,b;
        cin>>a>>b;
        road[a].push_back(b);
        road[b].push_back(a);
    }
}

int DFS(int cur){
    int result=depth[cur];
    for(int i=0; i<road[cur].size(); i++){
        int des=road[cur][i];
        if(!depth[des]){
            depth[des]=depth[cur]+1;
            result=max(result, DFS(des));
        }
    }
    maxDepth[cur]=result;
    if(maxDepth[cur]-depth[cur]>=d){
        cnt+=2;
    }
    return result;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    maxDepth=depth=vector<int>(n+1, 0);
    depth[s]=1;
    DFS(s);
    if(cnt-2>=0)
        cout<<cnt-2<<endl;
    else
        cout<<0<<endl;
    return 0;
}
