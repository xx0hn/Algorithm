/*
 문제
 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

 입력
 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 영어 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.

  

 듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

 출력
 듣보잡의 수와 그 명단을 사전순으로 출력한다.
 
 ----이진탐색
 */
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#define MAX 500001
using namespace std;

int n, m;
vector<string> Dlist;
vector<string> Blist;
vector<string> DBname;
string name;

void Input(){
    cin>>n>>m;
    for(int i=0; i<n; i++){
        cin>>name;
        Dlist.push_back(name);
    }
    for(int j=0; j<m; j++){
        cin>>name;
        Blist.push_back(name);
    }
}

bool IsDB(int low, int high, string name){
    if(low>high)
        return false;
    else{
        int mid=(low+high)/2;
        if(Dlist[mid]==name){
            return true;
        }
        else if(Dlist[mid]>name){
            return IsDB(low, mid-1, name);
        }
        else
            return IsDB(mid+1, high, name);
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    sort(Dlist.begin(), Dlist.end());
    sort(Blist.begin(), Blist.end());
    for(int i=0; i<m; i++){
        if(IsDB(0, Dlist.size()-1, Blist[i])){
            DBname.push_back(Blist[i]);
        }
    }
    sort(DBname.begin(), DBname.end());
    cout<<DBname.size()<<endl;
    for(int i=0; i<DBname.size(); i++){
        cout<<DBname[i]<<endl;
    }
    return 0;
}
