//
//  main.cpp
//  practice.cpp
//
//  Created by 황승환 on 2020/05/06.
//  Copyright © 2020 황승환. All rights reserved.
//

/*
 문제
 세준이는 양수와 +, -, 그리고 괄호를 가지고 길이가 최대 50인 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

 입력
 첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다.

 출력
 첫째 줄에 정답을 출력한다.
 */
#include <iostream>
#include <cstring>
#include <cstdlib>
#define endl "\n"
#define MAX 50+1
using namespace std;

char s1[MAX];
char s2[MAX][MAX];

void Input(){
    cin>>s1;
}

int tok1st(){
    int idx=0;
    char *tok=strtok(s1, "-");
    while(tok!=NULL){
        strcpy(s2[idx], tok);
        tok=strtok(NULL, "-");
        idx++;
    }
    return idx;
}

int tok2nd(int idx){
    int result=0;
    for(int i=0; i<idx; i++){
        int sum=0;
        char *tok=strtok(s2[i], "+");
        while(tok!=NULL){
            sum+=atoi(tok);
            tok=strtok(NULL, "+");
        }
        if(i==0) result+=sum;
        else result-=sum;
    }
    return result;
}

void Solution()
{
    cout<<tok2nd(tok1st())<<endl;
}

void Solve()
{
    Input();
    Solution();
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    Solve();
    return 0;
}
