/*
 
 휴게소 세우기

 산하는 유료 고속도로를 가지고 있다. 산하는 현재 고속도로에 휴게소를 N개 가지고 있는데, 휴게소의 위치는 고속도로의 시작으로부터 얼만큼 떨어져 있는지로 주어진다.

 산하는 지금 휴게소를 M개 더 세우려고 한다.

 산하는 이미 휴게소가 있는 곳에 휴게소를 또 세울 수 없고, 고속도로의 끝에도 휴게소를 세울 수 없다. 휴게소는 정수 위치에만 세울 수 있다.

 산하는 이 고속도로를 이용할 때, 모든 휴게소를 방문한다. 산하는 휴게소를 M개 더 지어서 휴게소가 없는 구간의 길이의 최댓값을 최소로 하려고 한다. (반드시 M개를 모두 지어야 한다.)

 예를 들어, 고속도로의 길이가 1000이고, 현재 휴게소가 {200, 701, 800}에 있고, 휴게소를 1개 더 세우려고 한다고 해보자.

 일단, 지금 이 고속도로를 타고 달릴 때, 휴게소가 없는 구간의 최댓값은 200~701구간인 501이다. 하지만, 새로운 휴게소를 451구간에 짓게 되면, 최대가 251이 되어서 최소가 된다.

 ####입력####

 첫째 줄에 현재 휴게소의 개수 N, 더 지으려고 하는 휴게소의 개수 M, 고속도로의 길이 L이 주어진다. N은 100보다 작거나 같으며, M도 100보다 작거나 같다.
 L은 100보다 크거나 같고, 1000보다 작거나 같은 정수이다. 모든 휴게소의 위치는 중복되지 않으며, N+M은 L보다 작다. 둘째 줄에, 휴게소의 위치가 공백을 사이에 두고 주어진다.

 ####출력####

 첫째 줄에 M개의 휴게소를 짓고 난 후에 휴게소가 없는 구간의 최댓값의 최솟값을 출력한다.

 제한시간 2초

 문제 출저: https://www.acmicpc.net/problem/1477
 */
#include <iostream>
#include <algorithm>
#define MAX 101
using namespace std;

int n, m, l;
int point[MAX];
int dis[MAX];

void Input(){
    cin>>n>>m>>l;
    for(int i=0; i<n; i++){
        cin>>point[i];
    }
    sort(point, point+n);
}

void GetDistance(){
    dis[0]=point[0];
    for(int i=1; i<n; i++){
        dis[i]=point[i]-point[i-1];
    }
    dis[n]=l-point[n-1];
}

int BinarySearch(){
    int front=1;
    int back=l-1;
    while(front<back-1){
        int mid=(front+back)/2;
        int cnt=0;
        for(int i=0; i<=n; i++){
            if(dis[i]>mid){
                if(dis[i]%mid==0){
                    cnt+=dis[i]/mid-1;
                }
                else{
                    cnt+=dis[i]/mid;
                }
            }
        }
        if(m<cnt){
            front=mid;
        }
        else{
            back=mid;
        }
    }
    return back;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    GetDistance();
    cout<<BinarySearch()<<endl;
    return 0;
}
