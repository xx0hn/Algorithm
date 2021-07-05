/*
 문제
 다솜이는 0과 1로만 이루어진 문자열 S를 가지고 있다. 다솜이는 이 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 한다. 다솜이가 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다. 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.

 예를 들어 S=0001100 일 때,

 전체를 뒤집으면 1110011이 된다.
 4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 2번 만에 모두 같은 숫자로 만들 수 있다.
 하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다.

 문자열 S가 주어졌을 때, 다솜이가 해야하는 행동의 최소 횟수를 출력하시오.

 입력
 첫째 줄에 문자열 S가 주어진다. S의 길이는 100만보다 작다.

 출력
 첫째 줄에 다솜이가 해야하는 행동의 최소 횟수를 출력한다.
 */
#include <iostream>
#include <string>
#define MAX 1000001
using namespace std;

string S;
int cnt=0;
int cnt0=0, cnt1=0;

void Input(){
    cin>>S;
}

int Solution(){
    for(int i=0; i<S.length(); i++){
        if(S[i]=='0'){
            if(S[i]!=S[i+1])
                cnt0++;
        }
        else if(S[i]=='1'){
            if(S[i]!=S[i+1])
                cnt1++;
        }
    }
    if(cnt0>cnt1){
        return cnt1;
    }
    else
        return cnt0;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    cout<<Solution()<<endl;
    return 0;
}

