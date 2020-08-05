//
//  main.cpp
//  practice.cpp
//
//  Created by 황승환 on 2020/05/06.
//  Copyright © 2020 황승환. All rights reserved.
//

/*
 문제
 4 × 3 = 12이다.

 이 식을 통해 다음과 같은 사실을 알 수 있다.

 3은 12의 약수이고, 12는 3의 배수이다.

 4도 12의 약수이고, 12는 4의 배수이다.

 두 수가 주어졌을 때, 다음 3가지 중 어떤 관계인지 구하는 프로그램을 작성하시오.

 첫 번째 숫자가 두 번째 숫자의 약수이다.
 첫 번째 숫자가 두 번째 숫자의 배수이다.
 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.
 입력
 입력은 여러 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 10,000이 넘지않는 두 자연수로 이루어져 있다. 마지막 줄에는 0이 2개 주어진다. 두 수가 같은 경우는 없다.

 출력
 각 테스트 케이스마다 첫 번째 숫자가 두 번째 숫자의 약수라면 factor를, 배수라면 multiple을, 둘 다 아니라면 neither를 출력한다.
 */
#include <iostream>
#include <algorithm>
#define endl "\n"
using namespace std;

pair<int, int> Num;

void Solution()
{
    for(int i=0; ; i++)
    {
        cin>>Num.first>>Num.second;
        if(Num.first==0&&Num.second==0)
            break;
        
        if(Num.second%Num.first==0)
            cout<<"factor"<<endl;
        else if(Num.first%Num.second==0)
            cout<<"multiple"<<endl;
        else
            cout<<"neither"<<endl;
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    Solution();
    return 0;
}
