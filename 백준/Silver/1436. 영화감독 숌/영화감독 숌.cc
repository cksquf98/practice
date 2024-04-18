// 종말의 수란 어떤 수에 6이 적어도 3개 이상 연속으로 들어가는 수를 말한다. 
// 제일 작은 종말의 수는 666이고, 그 다음으로 큰 수는 1666, 2666, 3666, .... 
// 숌이 만든 N번째 영화의 제목에 들어간 수를 출력하는 프로그램을 작성하시오. 

#include<iostream>
#include<string>
using namespace std;
int main(int argc, char const *argv[])
{
    cin.tie(0);
    cout.tie(0);

    unsigned int N,count;
    cin >> N;
    
    
    count = 0;
    string s;
    for (int i = 666; ; i++)
    {
        s = to_string(i);
        if(s.find("666") == string::npos) continue;
        else count++;

        if(count == N) 
        {
            cout << i;
            break;
        }
    }
}