//
//  main.cpp
//  practice.cpp
//
//  Created by 황승환 on 2020/05/06.
//  Copyright © 2020 황승환. All rights reserved.
//

/*
 문제
 N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

 입력
 첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

 출력
 첫째 줄에 구한 0의 개수를 출력한다.
 */
#include <iostream>
#define endl "\n"
using namespace std;

int n;
int num=1;
int cnt=0;

void Input(){
    cin>>n;
}

void Solution(){
    for(int i=1; i<=n; i++){
        if(i%5==0)
            cnt++;
        if(i%25==0)
            cnt++;
        if(i%125==0)
            cnt++;
    }
    cout<<cnt<<endl;
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
