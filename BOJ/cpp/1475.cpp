/*
 문제
 다솜이는 은진이의 옆집에 새로 이사왔다. 다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.

 다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다. 다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오. (6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)

 입력
 첫째 줄에 다솜이의 방 번호 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수 또는 0이다.

 출력
 첫째 줄에 필요한 세트의 개수를 출력한다.


 */
#include <iostream>
#include <string>
using namespace std;

string num;
int arr[10];

void Input(){
    cin>>num;
    for(int i=0; i<10; i++){
        arr[i]=0;
    }
}

void Solution(){
    int cur=0;
    while(cur<=num.size()){
        for(int i=0; i<10; i++){
            if(i==num[cur]-'0'){
                arr[i]++;
            }
        }
        cur++;
    }
    arr[6]=arr[9]=(arr[6]+arr[9]+1)/2;
    int max=0;
    for(int i=0; i<10; i++){
        if(max<arr[i]){
            max=arr[i];
        }
    }
    cout<<max<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    Solution();
    return 0;
}
