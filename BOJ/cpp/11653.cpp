//
//  main.cpp
//  practice.cpp
//
//  Created by 황승환 on 2020/05/06.
//  Copyright © 2020 황승환. All rights reserved.
//

/*
 문제
 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

 입력
 첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

 출력
 N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다.
 */
#include <iostream>
#define endl "\n"
#define MAX 10000000+1
using namespace std;

int n;
int answer=2;

void Input(){
    cin>>n;
}

void Solution(){
    while(n!=1){
        if(n%answer==0){
            n=n/answer;
            cout<<answer<<endl;
        }
        else if(n%answer!=0){
            answer++;
        }
    }
}

void Solve(){
    Input();
    Solution();
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
