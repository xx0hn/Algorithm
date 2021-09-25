/*
 문제

 bryan은 PPAP를 좋아한다. bryan은 어떻게 하면 사람들에게 PPAP를 전파할 수 있을까 고민하던 중 PPAP 문자열이라는 것을 고안하게 되었다.

 PPAP 문자열은 문자열 P에서 시작하여, 문자열 내의 P를 PPAP로 바꾸는 과정을 반복하여 만들 수 있는 문자열로 정의된다. 정확하게는 다음과 같이 정의된다.

     P는 PPAP 문자열이다.
     PPAP 문자열에서 P 하나를 PPAP로 바꾼 문자열은 PPAP 문자열이다.

 예를 들어 PPAP는 PPAP 문자열이다. 또한, PPAP의 두 번째 P를 PPAP로 바꾼 PPPAPAP 역시 PPAP 문자열이다.

 문자열이 주어졌을 때, 이 문자열이 PPAP 문자열인지 아닌지를 알려주는 프로그램을 작성하여라.

 ####입력####

 첫 번째 줄에 문자열이 주어진다. 문자열은 대문자 알파벳 P와 A로만 이루어져 있으며, 문자열의 길이는 1 이상 1,000,000 이하이다.

 ####출력####

 첫 번째 줄에 주어진 문자열이 PPAP 문자열이면 PPAP를, 아닌 경우 NP를 출력한다.
 
 문제 출처:https://www.acmicpc.net/problem/16120
 */
#include <iostream>
#include <string>
#include <vector>
using namespace std;

string ppap;
vector<int> st;

void Input(){
    cin>>ppap;
}

bool Solution(){
    if(ppap.size()==1&&ppap.front()=='P'){
        st.push_back('P');
    }
    else{
        for(int i=0; i<ppap.size(); i++){
            if(ppap[i]=='P'){
                st.push_back('P');
            }
            else if(st.size()>=2&&ppap[i+1]=='P'){
                st.pop_back();
                st.pop_back();
            }
            else{
                return false;
            }
        }
    }
    if(st.size()==1)
        return true;
    else
        return false;
}

void Solve(){
    if(Solution())
        cout<<"PPAP"<<endl;
    else
        cout<<"NP"<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    Solve();
    return 0;
}
