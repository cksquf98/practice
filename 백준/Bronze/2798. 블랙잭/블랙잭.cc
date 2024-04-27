
#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    cin.tie(0);
    cout.tie(0);

    int N,M;
    cin >> N >> M;

    int ansArr[100] = {0,};
    int sum = 0;
    int ans = 0;

    for (int i = 0; i < N; i++)
    {
        cin >> ansArr[i];
    }
    for (int firstNum = 0; firstNum < N-2; firstNum++)
    {
        for (int secondNum = firstNum+1; secondNum < N-1; secondNum++)
        {
            for (int thirdNum = secondNum+1; thirdNum < N; thirdNum++)
            {
                sum = ansArr[firstNum]+ansArr[secondNum]+ansArr[thirdNum];
                if (sum > ans && sum <= M) 
                {
                    // 세 개의 합을 구할 때 m보단 작되 제일 큰 수를 구하면 된다. 
                    // 브루트 포스로 하나씩 비교해가면서 조건에 맞는 수를 찾으면 된다.
                    ans = sum;
                }
                
            }
        }
    }
    cout << ans;
    return 0;
}