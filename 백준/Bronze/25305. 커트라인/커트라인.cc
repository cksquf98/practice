#include<iostream>
using namespace std;

int input[1000]= {0,};

int main(int argc, char const *argv[])
{
    cin.tie(0);
    cout.tie(0);

    //N개 입력, K번째 원소값 출력
    int N,K;
    cin >> N >> K;
    for (int i = 0; i < N; i++)
    {
        int num;
        cin >> num;
        input[i] = num;

        int prev = i-1;

        while (prev >= 0 && input[prev] < num)
        {
            input[prev+1] = input[prev];
            prev--;
        }
        input[prev+1] = num;
    }


    cout << input[K-1];

    return 0;
    
}