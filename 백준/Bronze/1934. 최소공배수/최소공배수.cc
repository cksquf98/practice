//최소공배수
//최대공약수 == 1 : 걍 두 수 곱한게 최소공배수
//최대공약수 있으면 최대공약수의 배수에서 최소공배수 찾기 -----> 시간초과



/******* 최대공약수 : 유클리드 호제법을 사용해야 한다는군

    1. 큰 수를 작은 수로 나눈다.

    2. 나누는 수를 나머지로 계속 나눈다.

    3. 나머지가 0이 나오면 나누는 수가 최대공약수이다.
 
 
******* 최소공배수 : 두 자연수 곱 / 최대공약수   

https://dimenchoi.tistory.com/46
*/


#include<iostream>
using namespace std;

int Uclid(int A, int B)
{   
    int rest = 0;
    if(A > B)
    {
        while(B > 0)
        {
            rest = A % B;
            if(A % B == 0)  return B;
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
            if(B % A == 0) return A;;
            B = A;
            A = rest;
        }
        return rest;
    }
}
int main(int argc, char const *argv[])
{
    cin.tie(0);
    cout.tie(0);

    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        int A,B;
        cin >> A >> B;

        int minDivisor = Uclid(A,B);
        int maxMultiple = (A*B) / minDivisor;
        
        cout << maxMultiple << '\n';
    }

    return 0;
}