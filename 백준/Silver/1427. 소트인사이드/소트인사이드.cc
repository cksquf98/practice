#include<iostream>
#include<list>
#include <string>
using namespace std;
int main(int argc, char const *argv[])
{
    cin.tie(0);
    cout.tie(0);
    
    string N;
    cin >> N;

    list <int> l;

    for (int i = 0; i < N.length(); i++)
    {
        int num = (int)(N[i])-'0';
        l.push_back(num);
    }

    l.sort();
    int size = l.size();

    for (int j = 0; j < size; j++)
    {
        cout << l.back();
        l.pop_back();
    }
    return 0;
}