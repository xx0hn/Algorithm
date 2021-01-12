/*
 문제
 N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

 입력
 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

 출력
 M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
 */
#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 100001
using namespace std;

int n, m, num;
vector<int> a;
vector<int> b;

void Input(){
    cin>>n;
    for(int i=0; i<n; i++){
        cin>>num;
        a.push_back(num);
    }
    cin>>m;
    for(int i=0; i<m; i++){
        cin>>num;
        b.push_back(num);
    }
}
int binarySearch(int low, int high, int target){
    if(low>high){
        return 0;
    }
    else{
        int mid=(low+high)/2;
        if(a[mid]==target){
            return 1;
        }
        else if(a[mid]>target){
            return binarySearch(low, mid-1, target);
        }
        else{
            return binarySearch(mid+1, high, target);
        }
    }
}
void Solution(){
    sort(a.begin(), a.end());
    for(int i=0; i<m; i++){
        cout<<binarySearch(0, n-1, b[i])<<"\n";
    }
}
int main(){
    cin.tie(0);
    Input();
    Solution();
    return 0;
}
