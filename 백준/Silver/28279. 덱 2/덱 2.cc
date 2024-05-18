// 덱

#include <iostream>
#include <deque>
using namespace std;
int main(int argc, char const *argv[])
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    deque <int> dq;

    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        char s;
        cin >> s;

        switch (s)
        {
        case '1':
        {
            int X;
            cin >> X;

            dq.push_front(X);
            break;
        }
        case '2':
        {
            int X;
            cin >> X;

            dq.push_back(X);
            break;
        }
        case '3':
        {
            if(dq.empty())  cout << -1 << '\n';
            else
            {
                cout << dq.front() << '\n';
                dq.pop_front();
            }
            break;
        }
        case '4':
        {
            if(dq.empty())  cout << -1 << '\n';
            else
            {
                cout << dq.back() << '\n';
                dq.pop_back();
            }
            break;
        }
        case '5':
        {
            cout << dq.size() << '\n';
            break;
        }
        case '6':
        {
            cout << dq.empty() << '\n';
            break;
        }
        case '7':
        {
            if(dq.empty())  cout << -1 << '\n';
            else    cout << dq.front() << '\n';
            
            break;
        }
        case '8':
        {
            if(dq.empty())  cout << -1 << '\n';
            else    cout << dq.back() << '\n';
            
            break;
        }
        }
    }

    return 0;
}