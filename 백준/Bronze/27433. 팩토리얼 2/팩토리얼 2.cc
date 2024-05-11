#include<iostream>
using namespace std;
long long int fac(long long int num)
{
    if(num == 0)
        return 1;
    return num*fac(num-1);
}
int main(int argc, char const *argv[])
{
    int N;
    cin >> N;
    cout << fac(N);
    return 0;
}