/*
 문제
 N개의 정수가 주어진다. 이때, N개의 정수를 오름차순으로 정렬하는 프로그램을 작성하시오. 같은 정수는 한 번만 출력한다.

 입력
 첫째 줄에 수의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째에는 숫자가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다.

 출력
 첫째 줄에 수를 오름차순으로 정렬한 결과를 출력한다. 이때, 같은 수는 한 번만 출력한다.
 */
#include <iostream>
#include <algorithm>
#include <vector>
#define MAX 100001
#define CHKMAX 1001
using namespace std;

int n;
vector<int> arr;
bool chk[CHKMAX]={false};
bool mchk[CHKMAX]={false};

void Input(){
    cin>>n;
    for(int i=0; i<n; i++){
        int a;
        cin>>a;
        if(a>=0){
            if(!chk[a]){
                arr.push_back(a);
                chk[a]=true;
            }
        }
        else{
            if(!mchk[(-1)*a]){
                arr.push_back(a);
                mchk[(-1)*a]=true;
            }
        }
    }
}

void Solution(){
    sort(arr.begin(), arr.end());
    for(int i=0; i<arr.size(); i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    Solution();
    return 0;
}
