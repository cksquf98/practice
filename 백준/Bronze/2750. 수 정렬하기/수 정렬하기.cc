#include<iostream>
using namespace std;


int arr[1000] = {0,};

void sorting(int N)
{
    for (int i = 0; i < N; i++)
    {
        for (int j = i+1; j < N; j++)
        {
            int tmp = arr[i];
            if(arr[i] > arr[j])
            {
                arr[i] = arr[j];
                arr[j] = tmp;
            }
        }
    }
    
}
int main(int argc, char const *argv[])
{
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N;

   
    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }
    
    sorting(N);

    for (int k = 0; k < N; k++)
    {
        cout << arr[k] << '\n';
    }
}