//
//  main.cpp
//  practice.cpp
//
//  Created by 황승환 on 2020/05/06.
//  Copyright © 2020 황승환. All rights reserved.
//

/*
 문제
 해빈이는 패션에 매우 민감해서 한번 입었던 옷들의 조합을 절대 다시 입지 않는다. 예를 들어 오늘 해빈이가 안경, 코트, 상의, 신발을 입었다면, 다음날은 바지를 추가로 입거나 안경대신 렌즈를 착용하거나 해야한다. 해빈이가 가진 의상들이 주어졌을때 과연 해빈이는 알몸이 아닌 상태로 며칠동안 밖에 돌아다닐 수 있을까?

 입력
 첫째 줄에 테스트 케이스가 주어진다. 테스트 케이스는 최대 100이다.

 각 테스트 케이스의 첫째 줄에는 해빈이가 가진 의상의 수 n(0 ≤ n ≤ 30)이 주어진다.
 다음 n개에는 해빈이가 가진 의상의 이름과 의상의 종류가 공백으로 구분되어 주어진다. 같은 종류의 의상은 하나만 입을 수 있다.
 모든 문자열은 1이상 20이하의 알파벳 소문자로 이루어져있으며 같은 이름을 가진 의상은 존재하지 않는다.

 출력
 각 테스트 케이스에 대해 해빈이가 알몸이 아닌 상태로 의상을 입을 수 있는 경우를 출력하시오.
 */
#include <iostream>
#include <map>
#define endl "\n"
using namespace std;

int t, n ,i, j, mul;
string temp, key;
map<string, int> m;
pair<map<string, int>::iterator, bool> pr;

void Solve(){
    cin>>t;
    for(i=0; i<t; i++){
        m.clear();
        mul=1;
        cin>>n;
        for(j=0; j<n; j++){
            cin>>temp>>key;
            pr=m.insert(pair<string, int>(key, 1));
            if(!pr.second)
                m[key]++;
        }
        for(map<string, int>::iterator it=m.begin(); it!=m.end(); it++){
            mul*=(it->second+1);
        }
        cout<<mul-1<<endl;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    Solve();
    return 0;
}
