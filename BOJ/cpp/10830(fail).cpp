/*
 문제
 크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오. 수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.

 입력
 첫째 줄에 행렬의 크기 N과 B가 주어진다. (2 ≤ N ≤  5, 1 ≤ B ≤ 100,000,000,000)

 둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다. 행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다.

 출력
 첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다.
 */
#include <iostream>
#define MAX 6
using namespace std;

int n, b;
long long a[MAX][MAX];
long long c[MAX][MAX];
long long result[MAX][MAX];

void Input(){
    cin>>n>>b;
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cin>>a[i][j];
        }
        result[i][i]=1;
    }
}

void Solution(long long a[MAX][MAX], long long b[MAX][MAX]){
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            c[i][j]=0;
            for(int k=0; k<n; k++){
                c[i][j]+=a[i][k]*b[k][j];
            }
            c[i][j]%=1000;
        }
    }
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            a[i][j]=c[i][j];
        }
    }
}

void Solve(){
    while(b>0){
        if(b%2==1){
            Solution(result, a);
        }
        Solution(a, a);
        b/=2;
    }
}

void Print(){
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cout<<result[i][j]<<" ";
        }
        cout<<endl;
    }
}

int main(){
    Input();
    Solve();
    Print();
    return 0;
}
