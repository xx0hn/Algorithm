//
//  main.cpp
//  practice.cpp
//
//  Created by 황승환 on 2020/05/06.
//  Copyright © 2020 황승환. All rights reserved.
//

/*
 문제
 N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1의 세 값 중 하나가 저장되어 있다. 우리는 이 행렬을 적절한 크기로 자르려고 하는데, 이때 다음의 규칙에 따라 자르려고 한다.

 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
 (1)이 아닌 경우에는 종이를 같은 크기의 9개의 종이로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
 이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.

 입력
 첫째 줄에 N(1≤N≤3^7, N은 3^k 꼴)이 주어진다. 다음 N개의 줄에는 N개의 정수로 행렬이 주어진다.

 출력
 첫째 줄에 -1로만 채워진 종이의 개수를, 둘째 줄에 0으로만 채워진 종이의 개수를, 셋째 줄에 1로만 채워진 종이의 개수를 출력한다.
 */
#include <iostream>
#include <algorithm>
#include <cstring>
#define MAX 2188
#define endl "\n"
using namespace std;

int n;
int Map[MAX][MAX];
int c[3];

void Input(){
    cin>>n;
    memset(Map, 0, sizeof(Map));
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cin>>Map[i][j];
        }
    }
}

void divCon(int n, int m, int x){
    int check=Map[n][m];
    for(int i=n; i<n+x; i++){
        for(int j=m; j<m+x; j++){
            if(check==-1&&Map[i][j]!=-1){
                check=2;
            }
            else if(check==0&&Map[i][j]!=0){
                check=2;
            }
            else if(check==1&&Map[i][j]!=1){
                check=2;
            }
            if(check==2){
                int div=x/3;
                divCon(n, m, div);
                divCon(n+div, m, div);
                divCon(n+div*2, m, div);
                
                divCon(n, m+div, div);
                divCon(n+div, m+div, div);
                divCon(n+div*2, m+div, div);
                
                divCon(n, m+div*2, div);
                divCon(n+div, m+div*2, div);
                divCon(n+div*2, m+div*2, div);
                return;
            }
        }
    }
    if(check==-1)
        c[0]++;
    else if(check==0)
        c[1]++;
    else if(check==1)
        c[2]++;
    return;
}

void Solve(){
    Input();
    divCon(0, 0, n);
    for(int i=0; i<3; i++){
        cout<<c[i]<<endl;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    Solve();
    return 0;
}
