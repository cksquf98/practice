#include<iostream>
#include<queue>
using namespace std;

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    queue <int> cards;

    // 1. 맨 위 카드 버리기
    // 2. 다음으로 맨 위 카드를 맨 뒤로 보냄
    int N;
    cin >> N;

    if(N == 1)
    {
        cout << 1;
        return 0;
    }

    for (int i = 1; i <= N; i++)
    {
        cards.push(i);
    }

    while(1)
    {
        cards.pop();
        if(cards.size() == 1)   break;

        int top = cards.front();
        cards.push(top);
        cards.pop();
    }
    
    cout << cards.front();
}