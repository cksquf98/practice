#include <iostream>
#include<algorithm>

using namespace std;

int fibo(int num)
{
    if(num == 0)    return 0;
    else if(num == 1)    return 1;
    else    return fibo(num-2) + fibo(num-1); 
}

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int num;
    cin >> num;
    cout << fibo(num);
}