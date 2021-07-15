/*
 문제
 창영이는 매일 버스를 이용해 출퇴근을 한다.

 창영이가 사는 도시에는 N개의 버스가 있고, S번 버스에서 E번 버스로 환승하기 위해서는 AS,E원이 필요하다.

 창영이가 출근하기 위해 이용하는 M개의 버스가 환승하는 순서대로 주어지고, 모든 버스끼리의 환승 요금이 주어진다.

 창영이가 한 번 출근하는데 지불해야하는 환승 요금의 합을 구해보자. 최초에 탑승할 때 지불하는 버스 요금은 제외한다.

 입력
 첫째 줄에 도시에 존재하는 버스의 개수 N, 창영이가 이용하는 버스의 개수 M이 주어진다.

 둘째 줄에 창영이가 이용하는 M개 버스의 번호가 순서대로 주어진다. 버스 번호는 중복되지 않는다.

 셋째 줄부터 N개의 줄에 걸쳐 버스의 환승 요금에 대한 정보가 주어진다. S번째 줄의 E번째 수는 AS,E를 의미한다. AS,E는 AE,S와 다를 수 있다.

 출력
 주어진 M개의 버스를 순서대로 환승하며 탑승했을 때 필요한 환승 요금의 총합을 출력한다.
 */
#include <iostream>
#define MAX 101
using namespace std;

int n, m;
int bus[MAX];
int cost[MAX][MAX];
int total=0;

void Input(){
    cin>>n>>m;
    for(int i=1; i<=m; i++){
        cin>>bus[i];
    }
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            cin>>cost[i][j];
        }
    }
}

void Solution(){
    for(int i=1; i<m; i++){
        total+=cost[bus[i]][bus[i+1]];
    }
    cout<<total<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    Solution();
    return 0;
}
