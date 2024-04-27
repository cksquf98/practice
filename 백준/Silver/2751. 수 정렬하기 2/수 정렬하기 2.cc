#include<iostream>
#include<list>

using namespace std;
int main(int argc, char const *argv[])
{
    list <int> l;
    
    int N;
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        int num;
        cin >> num;

        l.push_back(num);
    }
    
    l.sort();
  
    for (int j = 0; j < N; j++)
    {
        cout << l.front() << '\n';
        l.pop_front();
    }
    

    return 0;
}
