#include <iostream>
#include <algorithm>
#include <math.h>
using namespace std;

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    unsigned int M, N;
    cin >> M >> N;

    for (unsigned int i = M; i <= N; i++)
    {
        if (i < 2)
        {
            continue;
        }
        else
        {
            int sq = sqrt(i);
            bool flag = true;
            for (int j = 2; j <= sq; j++)
            {   
                if (i % j == 0)
                {
                    flag = false;
                    break;
                }
            }

            if (flag)
                cout << i << '\n';
        }
    }
    return 0;
}