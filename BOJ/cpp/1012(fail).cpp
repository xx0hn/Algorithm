/*
 문제
 차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다. 농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에, 한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다. 이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다. 특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다. 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.

 한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다. 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다. 예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다. 0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.

 1    1    0    0    0    0    0    0    0    0
 0    1    0    0    0    0    0    0    0    0
 0    0    0    0    1    0    0    0    0    0
 0    0    0    0    1    0    0    0    0    0
 0    0    1    1    0    0    0    1    1    1
 0    0    0    0    1    0    0    1    1    1
 입력
 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.

 출력
 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.
 */
#include <iostream>
#define MAX 51
using namespace std;


int t, m, n, k;
int ground[MAX][MAX];
bool check[MAX][MAX];
int dx[]={0,0,-1,1};
int dy[]={1,-1,0,0};
int a,b;
int cnt;

void Init(){
    cnt=0;
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            ground[i][j]=0;
            check[i][j]=false;
        }
    }
}

void Input(){
    cin>>m>>n>>k;
    for(int l=0; l<k; l++){
        cin>>a>>b;
        if((a>=0&&a<=m)&&(b>=0&&b<=n)){
            ground[b][a]=1;
        }
    }
}

void DFS(int x, int y){
    check[x][y]=true;
    for(int i=0; i<4; i++){
        int nx=x+dx[i];
        int ny=y+dy[i];
        if(0<=nx&&nx<n && 0<=ny&&ny<m){
            if(ground[nx][ny]==1 && !check[nx][ny]){
                check[nx][ny]=true;
                DFS(nx, ny);
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin>>t;
    for(int i=0; i<t; i++){
        Init();
        Input();
        for(int j=0; j<n; j++){
            for(int l=0; l<m; l++){
                if(ground[j][l]==1 && !check[j][l]){
                    DFS(j, l);
                    cnt++;
                }
            }
        }
        cout<<cnt<<endl;
    }
    return 0;
}
