#include<iostream>
using namespace std;
int Uclid(int a, int b)
{
    int rest = 0;
    if(a > b)
    {   
        while(b > 0)
        {
            rest = a % b;
            if(rest == 0)   return b;

            a = b;
            b = rest;
        }
    }
    else
    {
        while(a > 0)
        {
            rest = b % a;
            if(rest == 0)   return a;

            b = a;
            a = rest;
        }
    }
}
int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);


    int A_top, A_bottom;
    int B_top, B_bottom;

    cin >> A_top >> A_bottom;
    cin >> B_top >> B_bottom;

    int res_top, res_bottom;
    res_top = A_top * B_bottom + B_top * A_bottom;
    res_bottom = A_bottom * B_bottom;

    int maxDivisor = Uclid(res_top, res_bottom);
    res_top /= maxDivisor;
    res_bottom /= maxDivisor;

    cout << res_top << " " << res_bottom;

    return 0;
}