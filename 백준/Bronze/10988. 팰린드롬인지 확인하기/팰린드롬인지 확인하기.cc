#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    cin.tie(0);
    cout.tie(0);

    string s;
    cin >> s;

    int len = s.length();
    int i = 0;
    bool flag = true;

    while(flag)
    {
        if(s[i] != s[len-i-1])
            flag = false;
        if(i > len/2)
            break;
        i++;
    } 
    cout << flag;
    return 0;
}