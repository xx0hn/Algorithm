/*
 문제
 알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 모음(a, e, i, o, u)의 개수를 출력하는 프로그램을 작성하시오.

 입력
 첫째 줄에 단어가 주어진다. 단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며, 알파벳 소문자로만 이루어져 있다.

 출력
 첫째 줄에 모음의 개수를 출력한다.

 */
#include <iostream>
#include <string>
using namespace std;

string S;
int cnt=0;
char m[5]={'a', 'e', 'i', 'o', 'u'};

void Input(){
    cin>>S;
}

int Solution(){
    for(int i=0; i<S.size(); i++){
        for(int j=0; j<5; j++){
            if(S[i]==m[j])
                cnt++;
        }
    }
    return cnt;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    cout<<Solution()<<endl;
    return 0;
}
