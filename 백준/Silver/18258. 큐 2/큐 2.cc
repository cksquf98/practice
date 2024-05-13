#include<iostream>
#include<queue>
#include<string>
using namespace std;

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    queue <int> q;
    int N;

    cin >> N;
    for (int i = 0; i < N; i++)
    {
        string input;
        cin >> input;

        //C++에서 Switch문에 string은 안된다는 사실을. 이제 알었다.
        if(input == "push")
        {
            int num;
            cin >> num;
            q.push(num);
            continue;
        }
        else if(input == "pop")
        {
            if(q.empty())
            {
                cout << -1 << '\n';
                continue;
            }
            int num = q.front();
            q.pop();
            cout << num << '\n';
        }
        else if(input == "size")
        {
            cout << q.size() << '\n';
        }
        else if(input == "empty")
        {
            cout << q.empty() << '\n';
        }
        else if(input == "front")
        {
            if(q.empty())
            {
                cout << -1 << '\n';
                continue;
            }
            cout << q.front() << '\n';
        }
        else
        {
            if(q.empty())
            {
                cout << -1 << '\n';
                continue;
            }
            cout << q.back() << '\n';
        }
    }
    return 0;
}