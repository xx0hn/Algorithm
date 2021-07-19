/*
 문제
 수 N개 A1, A2, ..., AN이 주어진다. A를 오름차순 정렬했을 때, 앞에서부터 K번째 있는 수를 구하는 프로그램을 작성하시오.

 입력
 첫째 줄에 N(1 ≤ N ≤ 5,000,000)과 K (1 ≤ K ≤ N)이 주어진다.

 둘째에는 A1, A2, ..., AN이 주어진다. (-109 ≤ Ai ≤ 109)

 출력
 A를 정렬했을 때, 앞에서부터 K번째 있는 수를 출력한다.
 */
#include <iostream>
#include <algorithm>
#include <vector>
#define MAX 5000001
using namespace std;

int n, k;
int a[MAX];
vector<int> result;

void Input(){
    cin>>n>>k;
    for(int i=0; i<n; i++){
        cin>>a[i];
        result.push_back(a[i]);
    }
    sort(result.begin(), result.end());
}

int Solution(int k){
    return result[k-1];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
   /* for(int i=0; i<n; i++){
        cout<<result[i]<<" ";
    }
    */
    cout<<Solution(k)<<endl;
    return 0;
}
