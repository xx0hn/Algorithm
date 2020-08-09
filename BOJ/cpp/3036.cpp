//
//  main.cpp
//  practice.cpp
//
//  Created by 황승환 on 2020/05/06.
//  Copyright © 2020 황승환. All rights reserved.
//

/*
 문제
 상근이는 창고에서 링 N개를 발견했다. 상근이는 각각의 링이 앞에 있는 링과 뒤에 있는 링과 접하도록 바닥에 내려놓았다.



 상근이는 첫 번째 링을 돌리기 시작했고, 나머지 링도 같이 돌아간다는 사실을 발견했다. 나머지 링은 첫 번째 링 보다 빠르게 돌아가기도 했고, 느리게 돌아가기도 했다. 이렇게 링을 돌리다 보니 첫 번째 링을 한 바퀴 돌리면, 나머지 링은 몇 바퀴 도는지 궁금해졌다.

 링의 반지름이 주어진다. 이때, 첫 번째 링을 한 바퀴 돌리면, 나머지 링은 몇 바퀴 돌아가는지 구하는 프로그램을 작성하시오.

 입력
 첫째 줄에 링의 개수 N이 주어진다. (3 ≤ N ≤ 100)

 다음 줄에는 링의 반지름이 상근이가 바닥에 놓은 순서대로 주어진다. 반지름은 1과 1000를 포함하는 사이의 자연수이다.

 출력
 출력은 총 N-1줄을 해야 한다. 첫 번째 링을 제외한 각각의 링에 대해서, 첫 번째 링을 한 바퀴 돌리면 그 링은 몇 바퀴 도는지 기약 분수 형태 A/B로 출력한다.
 */
#include <iostream>
#define MAX 100+1
#define endl "\n"
using namespace std;

int n;
int Ring[MAX];
int Standard;
int son[MAX], mom[MAX];
int k;

int gcd(int a, int b){
    int c;
    while(b!=0){
        c=a%b;
        a=b;
        b=c;
    }
    return a;
}

void Input(){
    cin>>n;
    for(int i=0; i<n; i++){
        cin>>Ring[i];
    }
}

void Solution(){
    Standard=Ring[0];
    for(int i=1; i<n; i++){
        if(Standard>Ring[i]){
            k=gcd(Standard, Ring[i]);
        }
        else{
            k=gcd(Ring[i], Standard);
        }
        cout<<Standard/k<<"/"<<Ring[i]/k<<endl;
    }
}

void Solve(){
    Input();
    Solution();
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    Solve();
    return 0;
}
