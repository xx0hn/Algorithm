/* 문제

 연속한 소수 p와 p+n이 있을 때, 그 사이에 있는 n-1개의 합성수(소수나 1이 아닌 양의 정수)는 길이가 n인 소수 사이 수열라고 부른다.

 양의 정수 k가 주어졌을 때, k를 포함하는 소수 사이 수열의 길이를 구하는 프로그램을 작성하시오. k를 포함하는 소수 사이 수열이 없을 때는 길이가 0이다.

 예를 들어, 소수 23과 29의 소수 사이 수열은 {24, 25, 26, 27, 28}이고, 길이는 6이다.

 #######입력#######

 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 테스트 케이스는 한 줄로 이루어져 있고, 한 줄에 정수 k가 주어진다. 각각의 정수는 1보다 크고, 100000번째 소수(1299709)와 작거나 같다.

 #######출력#######

 각각의 테스트 케이스에 대해서 k가 합성수라면 k를 포함하는 소수 사이 수열의 길이를 출력한다. 그렇지 않으면 0을 출력한다.
 */
#include <iostream>
#include <vector>
#define MAX 1299709+1
using namespace std;

int n;
int a;
vector<int> prime;
bool check[MAX];

void Input(){
    cin>>a;
}

void check_Prime(){
    for(int i=2; i<=MAX; i++){
        if(check[i]) continue;
        for(int j=i+i; j<MAX; j+=i){
            check[j]=true;
        }
    }
}

void get_Prime(){
    for(int i=2; i<=MAX; i++){
        if(!check[i]){
            prime.push_back(i);
        }
    }
}

int BinarySearch(int key){
    int front = 2;
    int back = prime.size()-1;
    while(front<=back){
        int mid = (front+back)/2;
        if(prime[mid]>=key){
            back = mid - 1;
        }
        else{
            front = mid + 1;
        }
    }
    return front;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin>>n;
    check_Prime();
    get_Prime();
    for(int i=0; i<n; i++){
        Input();
        if(!check[a]){
            cout<<0<<endl;
        }
        else{
            int idx = BinarySearch(a);
            int result =prime[idx]-prime[idx-1];
            cout<<result<<endl;
        }
    }
}
