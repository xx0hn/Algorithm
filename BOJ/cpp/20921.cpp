/*
 문제

 신수동 최고의 인싸 환주는 오늘도 인기가 많다. 그 인기는 정말 대단해서 대나무숲에서는 매일 환주의 이름이 쏟아진다.

 환주에게는 그 인기의 비결이 있었는데, 바로 자신이 원하는 두 명을 그렇고 그런 사이로 만들 수 있는 것이다!

 환주가 그렇고 그런 사이를 만드는 방법은 다음과 같다.

     1번 사람부터 N번 사람까지 N명을 일렬로 세운다.
     모든 사람에게 1부터 N까지 양의 정수 중 하나가 적힌 쪽지를 나눠준다. 쪽지에 적힌 정수는 중복되지 않는다.
         서로 다른 두 사람을 골랐을 때, 왼쪽에 있는 사람이 오른쪽에 있는 사람보다 쪽지에 적힌 정수가 더 크다면, 이 두 사람은 그렇고 그런 사이가 된다.
         놀랍게도 한 사람이 여러 사람과 그렇고 그런 사이일 수도 있다.

 21세기의 큐피드 환주는 썸과 연애 상담이 너무 많이 와서 힘들다. 그래서 환주는 한 번에 여러 개의 그렇고 그런 사이를 만들려 한다. 하지만 너무 많이 만들면 미풍양속에 저해되고, 너무 적게 만들면 솔로들이 많아지기 때문에, 정확히

 K개의 그렇고 그런 사이를 만들려 한다.

 환주는 저 멀리서 달려오는 N명의 친구들을 보았다. 재빨리 K개의 그렇고 그런 사이를 만들어 주지 않으면, 저들은 환주의 안티팬이 될지도 모른다!

 ###입력####

 정수 N, K가 주어진다. (2≤N≤4242, 0≤K≤N(N-1)/2)

 ####출력####
  
 N개의 정수 v1, v2, ..., vN을 공백 단위로 출력한다.

 vi는 i번째 사람이 받은 쪽지에 적힌 정수를 의미하고, 정확히 K개의 그렇고 그런 사이가 만들어져야 한다.

 정확히 K개의 그렇고 그런 사이를 만들 방법은 항상 존재하고, 만약 여러 가지 방법이 있다면 그중 하나를 출력한다.
 */
#include <iostream>
#include <cstring>
#define MAX 4243
using namespace std;

int n, k;
int v[MAX];
bool visited[MAX];

void Input(){
    cin>>n>>k;
    memset(v, 0, sizeof(v));
    memset(visited, false, sizeof(visited));
}

void Solution(){
    int end=n;
    int idx=1;
    while(k){
        if(k>=end-1){
            k-=(end-1);
            v[idx]=end;
            idx++;
            visited[end]=true;
        }
        end--;
    }
    int num=1;
    for(int i=1; i<=n; i++){
        if(v[i]!=0) continue;
        while(visited[num])
            num++;
        v[i]=num++;
    }
}

void Solve(){
    for(int i=1; i<=n; i++){
        cout<<v[i]<<" ";
    }
    cout<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    Solution();
    Solve();
    return 0;
}
