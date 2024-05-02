#include<iostream>
#include<set>
using namespace std;
int main(int argc, char const *argv[])
{
    cin.tie(0);
    cout.tie(0);
    int N;
    cin >> N;

    set <int> s;

    for (int i = 0; i < N; i++)
    {
        int num;
        cin >> num;
        s.insert(num);
    }
    
    int M;
    cin >> M;
    for (int k = 0; k < M; k++)
    {
        int num;
        cin >> num;
        
        if(s.find(num) != s.end())     cout<< 1 << " ";
        else    cout << 0 << " ";
    }
    
    return 0;
}