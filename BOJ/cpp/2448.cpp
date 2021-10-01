/*
 문제

 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

 ####입력####

 첫째 줄에 N이 주어진다. N은 항상 3×2k 수이다. (3, 6, 12, 24, 48, ...) (0 ≤ k ≤ 10, k는 정수)

 ####출력####

 첫째 줄부터 N번째 줄까지 별을 출력한다.

 예제 입력

 24

 예제 출력

                        *
                       * *
                      *****
                     *     *
                    * *   * *
                   ***** *****
                  *           *
                 * *         * *
                *****       *****
               *     *     *     *
              * *   * *   * *   * *
             ***** ***** ***** *****
            *                       *
           * *                     * *
          *****                   *****
         *     *                 *     *
        * *   * *               * *   * *
       ***** *****             ***** *****
      *           *           *           *
     * *         * *         * *         * *
    *****       *****       *****       *****
   *     *     *     *     *     *     *     *
  * *   * *   * *   * *   * *   * *   * *   * *
 ***** ***** ***** ***** ***** ***** ***** *****

 출처: https://www.acmicpc.net/problem/2448
 */
#include <iostream>
#define MAX 2*(3072+1)
using namespace std;

int n;
char star[MAX/2][MAX];

void Input(){
    cin>>n;
    for(int i=0; i<n+1; i++){
        for(int j=0; j<2*n; j++){
            star[i][j]=' ';
        }
    }
}

void Solution(int h, int y, int x){
    if(h==3){
        star[y][x]='*';
        star[y+1][x-1]='*';
        star[y+1][x+1]='*';
        for(int i=x-2; i<x+3; i++){
            star[y+2][i]='*';
        }
        return;
    }
    else{
        int nh=h/2;
        Solution(nh, y, x);
        Solution(nh, y+nh, x-nh);
        Solution(nh, y+nh, x+nh);
    }
}

void Solve(){
    for(int i=0;i<n;i++){
        for(int j=0; j<2*n-1; j++){
            cout<<star[i][j];
        }
        cout<<endl;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    Input();
    Solution(n, 0, n-1);
    Solve();
    return 0;
}
