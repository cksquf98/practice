
#include<iostream>
using namespace std;

//최대 공약수 : 유클리드 호제법으로 구하기
//최소 공배수 = A*B / 최대공약수

int Uclid(long long int A, long long int B)
{
    long int rest = 0;
    if(A > B)
    {
        while(B > 0)
        {
            rest = A % B;
            if(rest == 0) return B;

            A = B;
            B = rest;
        }
        return B;
    }
    else
    {
        while(A > 0)
        {
            rest = B % A;
            if(rest == 0) return A;

            B = A;
            A = rest;
        }
        return A;
    }
}
int main(int argc, char const *argv[])
{
    cin.tie(0);
    cout.tie(0);

    long long int A,B;
    cin >> A >> B;
    long long int maxDivisor = Uclid(A,B);
    long long int minMultiple = (A*B) / maxDivisor;

    cout << minMultiple;
    return 0;
}