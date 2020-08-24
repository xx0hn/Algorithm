//
//  main.cpp
//  practice.cpp
//
//  Created by 황승환 on 2020/05/06.
//  Copyright © 2020 황승환. All rights reserved.
//

/*
 문제
 선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다. AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.

 함수 R은 배열에 있는 숫자의 순서를 뒤집는 함수이고, D는 첫 번째 숫자를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.

 함수는 조합해서 한 번에 사용할 수 있다. 예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 숫자를 버리는 함수이다.

 배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.

 입력
 첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 최대 100이다.

 각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다. p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.

 다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. (0 ≤ n ≤ 100,000)

 다음 줄에는 [x1,...,xn]과 같은 형태로 배열에 들어있는 수가 주어진다. (1 ≤ xi ≤ 100)

 전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다.

 출력
 각 테스트 케이스에 대해서, 입력으로 주어진 정수 배열에 함수를 수행한 결과를 출력한다. 만약, 에러가 발생한 경우에는 error를 출력한다.
 */
#include <iostream>
#define endl "\n"
#define MAX 100001
using namespace std;

int n, start_idx, end_idx, cur_idx;
int arr[MAX];
bool order;
char p_arr[MAX];
char inp_arr[MAX*3+99999+2];

template<typename T>
int my_strlen(T *A){
    int i=0;
    while(A[i]!=0)
        i++;
    return i;
}

void Initialize(){
    for(int i=0; i<MAX; i++){
        p_arr[i]='\0';
        arr[i]=0;
    }
    for(int i=0; i<MAX+99999+2; i++){
        inp_arr[i]='\0';
    }
    start_idx=0;
    cur_idx=0;
    order=true;
}

void Input(){
    cin>>p_arr>>n>>inp_arr;
    int len=my_strlen(inp_arr);
    int idx=0;
    for(int i=0; i<len; i++){
        if(inp_arr[i]!='['&&inp_arr[i]!=']'&&inp_arr[i]!=','){
            int j=i;
            int x=0;
            while(inp_arr[j]!='['&&inp_arr[j]!=']'&&inp_arr[j]!=','){
                x=x+(inp_arr[j]-'0');
                x=x*10;
                j++;
                i++;
            }
            x=x/10;
            arr[idx++]=x;
        }
    }
    end_idx=idx-1;
}

void Solution(){
    bool Flag=true;
    int len=my_strlen(p_arr);
    int size=my_strlen(arr);
    
    for(int i=0; i<len; i++){
        if(p_arr[i]=='R'){
            if(order==true){
                order=false;
                cur_idx=end_idx;
            }
            else{
                order=true;
                cur_idx=start_idx;
            }
        }
        else{
            if(size==0){
                Flag=false;
                cout<<"error"<<endl;
            }
            if(order==true){
                start_idx++;
                cur_idx=start_idx;
                size--;
            }
            else{
                end_idx--;
                cur_idx=end_idx;
                size--;
            }
        }
    }
    if(Flag==true){
        cout<<"[";
        if(order==true){
            for(int i=start_idx; i<=end_idx; i++){
                if(i!=end_idx)
                    cout<<arr[i]<<",";
                else
                    cout<<arr[i];
            }
        }
        else{
            for(int i=end_idx; i>=start_idx; i--){
                if(i!=start_idx)
                    cout<<arr[i]<<",";
                else
                    cout<<arr[i];
            }
        }
        cout<<"]"<<endl;
    }
}

void Solve(){
    int tc;
    cin>>tc;
    for(int i=1; i<=tc; i++){
        Initialize();
        Input();
        Solution();
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    Solve();
    return 0;
}
