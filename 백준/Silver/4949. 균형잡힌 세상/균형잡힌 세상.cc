#include<iostream>
#include<stack>
#include<string>
using namespace std;
int main(int argc, char const *argv[])
{
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(false); 

    while (1)
    {
        string s;
        stack <char> collect;
        getline(cin,s);

        if(s == ".")  break;

        for (int i = 0; i < s.length(); i++)
        {
            // cout << "char : " << s[i] << '\n';
            switch (s[i])
            {
            case '(':
            case '[':
                collect.push(s[i]);
                break;
            case ')':
                if(collect.empty() || collect.top() != '(')
                {
                    collect.push(s[i]);
                    i = s.length();
                }
                else collect.pop();
                break;
            case ']':
                if(collect.empty()|| collect.top() != '[')
                {
                    collect.push(s[i]);
                    i = s.length();
                }
                else collect.pop();
                break;
            }
        }

        if(collect.empty()) cout << "yes\n";
        else cout << "no\n";
    }
    return 0;
}
