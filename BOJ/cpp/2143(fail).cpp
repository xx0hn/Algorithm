/*
 두 배열의 합

 한 배열 A[1], A[2], …, A[n]에 대해서, 부 배열은 A[i], A[i+1], …, A[j-1], A[j] (단, 1 ≤ i ≤ j ≤ n)을 말한다.

 이러한 부 배열의 합은 A[i]+…+A[j]를 의미한다. 각 원소가 정수인 두 배열 A[1], …, A[n]과 B[1], …, B[m]이 주어졌을 때,

 A의 부 배열의 합에 B의 부 배열의 합을 더해서 T가 되는 모든 부 배열 쌍의 개수를 구하는 프로그램을 작성하시오.

 예를 들어 A = {1, 3, 1, 2}, B = {1, 3, 2}, T=5인 경우, 부 배열 쌍의 개수는 다음의 7가지 경우가 있다.

 T(=5) = A[1] + B[1] + B[2]
       = A[1] + A[2] + B[1]
       = A[2] + B[3]
       = A[2] + A[3] + B[1]
       = A[3] + B[1] + B[2]
       = A[3] + A[4] + B[3]
       = A[4] + B[2]

 ####입력####

 첫째 줄에 T(-1,000,000,000 ≤ T ≤ 1,000,000,000)가 주어진다. 다음 줄에는 n(1 ≤ n ≤ 1,000)이 주어지고,
 그 다음 줄에 n개의 정수로 A[1], …, A[n]이 주어진다. 다음 줄에는 m(1 ≤ m ≤ 1,000)이 주어지고,
 그 다음 줄에 m개의 정수로 B[1], …, B[m]이 주어진다. 각각의 배열 원소는 절댓값이 1,000,000을 넘지 않는 정수이다.

 ####출력####

 첫째 줄에 답을 출력한다. 가능한 경우가 한 가지도 없을 경우에는 0을 출력한다.

 제한시간: 2초

 문제 출저: https://www.acmicpc.net/problem/2143
 */
#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 1001
using namespace std;

long long t;
int n, m;
int a[MAX], b[MAX];
vector<long long> asum, bsum;
long long cnt=0;

void Input(){
    cin>>t>>n;
    for(int i=0; i<n; i++){
        cin>>a[i];
    }
    cin>>m;
    for(int j=0; j<m; j++){
        cin>>b[j];
    }
}

void GetSum(){
    for(int i=0; i<n; i++){
        int sum=0;
        for(int j=i; j<n; j++){
            sum+=a[j];
            asum.push_back(sum);
        }
    }
    sort(asum.begin(), asum.end());
    for(int i=0; i<m; i++){
        int sum=0;
        for(int j=i; j<m; j++){
            sum+=b[j];
            bsum.push_back(sum);
        }
    }
}

void BinarySearch(long long vb){
    long long front=0;
    long long back=asum.size()-1;
    long long ub=-1;
    long long lb=-1;
    while(front<=back){
        long long mid=(front+back)/2;
        if(asum[mid]+vb>=t){
            if(asum[mid]+vb==t){
                lb=mid;
            }
            back=mid-1;
        }
        else if(asum[mid]+vb<t){
            front=mid+1;
        }
    }
    front=0, back=asum.size()-1;
    while(front<=back){
        long long mid=(front+back)/2;
        if(asum[mid]+vb>t){
            back=mid-1;
        }
        else if(asum[mid]+vb<=t){
            if(asum[mid]+vb==t){
                ub=mid;
            }
            front=mid+1;
        }
    }
    if(ub!=-1&&lb!=-1){
        cnt+=(ub-lb+1);
    }
}

void Solution(){
    for(int i=0; i<bsum.size(); i++){
        BinarySearch(bsum[i]);
    }
    cout<<cnt<<endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    GetSum();
    Solution();
    return 0;
}
