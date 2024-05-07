// n 입력 :  1 -> 3 -> 7 -> 13
// 간격의 최대공약수!!!!!!!!!!

#include<iostream>
#include<vector>
using namespace std;
int maxDivisor(int a, int b)
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
        while (a > 0)
        {
            rest = b % a;
            if(rest == 0)   return a;
            b = a;
            a = rest;
        }
        return a;
    }

}
int main(int argc, char const *argv[])
{
    int N;
    cin >> N;
    vector <int> inputs;

    for (int i = 0; i < N; i++)
    {
        int num;
        cin >> num;
        inputs.push_back(num);
    }

    

    int iv1 = inputs[1] - inputs[0];
    int divisor = iv1;


    int inputs_size = inputs.size();

    for(int j = 1; j < inputs_size-1; j++)
    {
        int iv2 = inputs[j+1] - inputs[j];
        divisor = maxDivisor(divisor, iv2);
    } 

    int count = inputs[inputs_size-1]/divisor - inputs[0]/divisor +1 - N;

    cout << count;

    return 0;
}