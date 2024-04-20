// 명령 처리 프로그램
// 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
// 2: 스택에 정수가 있다면 맨 위의 정수를 빼서, 출력한다. 없다면 -1을 대신 출력한다.
// 3: 스택에 들어있는 정수의 개수를 출력한다.
// 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
// 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.

#include<iostream>
#include<stack>

using namespace std;

int main(int argc, char const *argv[])
{
    cin.tie(0);
    cout.tie(0);

    int line;
    cin >> line;


    stack <int> s;

    for (int i = 0; i < line; i++)
    {
        string command;
        cin >> command;

        if(command == "1")
        {
            int num;
            cin >> num;
            s.push(num);
        }
        else if(command == "2")
        {
            if(s.empty())
            {
                cout << -1 << '\n';
                continue;
            }
            cout << s.top() << '\n';
            s.pop();
        }
        else if(command == "3")
        {
            cout << s.size() << '\n';
        }
        else if(command == "4")
        {
            if(s.empty())   cout << 1 << '\n';
            else            cout<< 0 << '\n';
        }
        else if(command == "5")
        {
            if(!s.empty())  cout << s.top() << '\n';
            else            cout << -1 << '\n';
        }
    }
    return 0;
}