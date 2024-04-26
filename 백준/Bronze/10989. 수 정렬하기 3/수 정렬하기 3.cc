#include<iostream>
using namespace std;


int main(int argc, char const *argv[])
{

    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    int arr[10001] = {0};
    int N;
    cin >> N;

    int maxNum = 0;

    for (int i = 0; i < N; i++)
    {
        int n;
        cin >> n;
        arr[n]++;

        if(maxNum < n)  maxNum = n;
    }
    

    for (int j = 1; j <= maxNum; j++)
    {
        for (int k = 0; k < arr[j]; k++)
        {
            cout << j << '\n';
        }
        
    }
    return 0;
}