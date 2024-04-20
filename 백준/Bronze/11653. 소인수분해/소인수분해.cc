// 출력
// 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
// N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.

#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    int N;
    cin >> N;

    while (N > 1)
    {
        for (int i = 2; i <= N; i++)    //소인수 분해 용도의 반복문
        {
            if (N % i == 0)
            {
                cout << i << "\n";
                N = N / i;
                break; //다시 2부터 시작하기 위해 => 4,6...등등의 합성수로 for문이 넘어가지 않게 됨
            } 
        }
    }
    return 0;
}