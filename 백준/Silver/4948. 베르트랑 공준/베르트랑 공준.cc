#include<cmath>
#include<iostream>
using namespace std;
bool Prime(int num)
{   
    if(num < 2) return false;

    int sq = sqrt(num);
    for (int i = 2; i <= sq; i++)
    {
        if(num % i == 0)    return false; 
    }
    
    return true;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    while(1)
    {
        int N;
        int count = 0;

        cin >> N;
        if (N == 0)
        {
            break;
        }

        for(int i = N+1; i <= 2*N; i++)
        {
            if(Prime(i))
            {
                //소수 맞음
                // cout << i << " ";
                count++;
            }
            else    continue;
        }
        cout << count << '\n';
    }
}