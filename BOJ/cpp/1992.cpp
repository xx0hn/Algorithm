#include <iostream>
#include <algorithm>
#include <cstring>
#define MAX 65
#define endl "\n"
using namespace std;

int n;
int Map[MAX][MAX];
string s;

void Input(){
    cin>>n;
    memset(Map, 0, sizeof(Map));
    for(int i=0; i<n; i++){
        cin>>s;
        for(int j=0; j<n; j++){
            Map[i][j]=s[j]-'0';
        }
    }
}

void divCon(int ns, int ms, int ne, int me){
    int check=Map[ns][ms];
    for(int i=ns; i<ne; i++){
        for(int j=ms; j<me; j++){
            if(check==0&&Map[i][j]==1){
                check=2;
            }
            else if(check==1&&Map[i][j]==0){
                check=2;
            }
            
            if(check==2){
                cout<<"(";
                divCon(ns, ms, (ns+ne)/2, (ms+me)/2);
                divCon(ns, (ms+me)/2, (ns+ne)/2, me);
                divCon((ns+ne)/2, ms, ne, (ms+me)/2);
                divCon((ns+ne)/2, (ms+me)/2, ne, me);
                cout<<")";
                return;
            }
        }
    }
    cout<<check;
    return;
}

void Solve(){
    Input();
    divCon(0, 0, n, n);
    cout<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    Solve();
    return 0;
}
