#include<iostream>
#include<stack>
using namespace std;

int main(int argc, char const *argv[])
{
    cin.tie(0);
    cout.tie(0);

    stack <int> speak;

    int K;
    cin >> K;

    long int sum = 0;
    
    for (int i = 0; i < K; i++)
    {
        int num;
        cin >> num;
        if(num == 0)
        {
            sum -= speak.top();
            speak.pop();
        }
        else
        {
            sum += num;
            speak.push(num);
        }
    }
    
   cout << sum;
   return 0;
}