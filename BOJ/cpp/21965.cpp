/*
 문제
 드높은 남산 위에 우뚝 선

 (중략)

 세워라 반석 위에

 선린의 터를

 어떤 수열 가 산이라는 것은, 수열이 어떤 지점 이전까지는 증가하다가, 해당 지점 이후부터는 감소하는 것을 의미한다. 다시 말해, 인 에 대해 이고 인 에 대해 를 만족하는  이하의 자연수 가 존재한다는 것을 의미한다.

 예를 들어 1 2 3 4 2는 4번째 수까지는 증가하는 수열이고, 4번째 수 이후로는 감소하는 수열이므로 산이다(). 1 2 3 4 5 역시 산이다(). 하지만 1 2 2 3 1은 산이 아니다.

 입력으로 주어지는 수열이 산인지 산이 아닌지 판별하는 프로그램을 작성하자.

 입력
 첫 번째 줄에는 수열의 길이 이 주어진다.

 두 번째 줄에는 이 공백으로 구분되어 주어진다.

 출력
 입력으로 주어진 수열 가 산이면 "YES"를, 산이 아니면 "NO"를 출력한다.
 */
#include <iostream>
#include <string>
#define MAX 100001
using namespace std;

int n;
int arr[MAX];

void Input(){
    cin>>n;
    for(int i=0; i<n; i++){
        cin>>arr[i];
    }
}

string Solution(){
    int max=0;
    int idx=0;
    for(int i=0; i<n; i++){
        if(max<arr[i]){
            max=arr[i];
            idx=i;
        }
    }
    for(int i=1; i<=idx; i++){
        if(arr[i]==arr[i-1]){
            return "NO";
        }
    }
    for(int i=idx+1; i<n-1; i++){
        if(!(arr[i]>arr[i+1])){
            return "NO";
        }
    }
    return "YES";
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    cout<<Solution()<<endl;
    return 0;
}
