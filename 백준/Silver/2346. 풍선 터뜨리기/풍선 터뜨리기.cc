// 덱
// 오와 이거 어렵당

#include <iostream>
#include <deque>
#include <map>
using namespace std;
int main(int argc, char const *argv[])
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    deque <pair<int,int>> dq;
    int N;

    cin >> N;
    for (int i = 1; i <= N; i++)
    {
        int move;
        cin >> move;
        
        dq.push_back(make_pair(move, i));
    }
    
    
    //규칙: 맨 앞 (1)부터 시작
    int move = dq.front().first;
    int index = dq.front().second;
    dq.pop_front();
    cout << 1 << ' ';

    while(dq.size() != 1)
    {
        if(move > 0) // 양수 뒤로 넣고 pop front로 찾음
        {
            for (int m = 0; m < move-1; m++)
            {
                dq.push_back(dq.front());
                dq.pop_front();
            }
            
            move = dq.front().first;
            index = dq.front().second;
            dq.pop_front();

        }
        else //음수면 뒤로 넣고 pop back으로 찾음
        {
            for (int m = move; m <-1; m++)
            {
                dq.push_front(dq.back());
                dq.pop_back();
            }
            
            move = dq.back().first;
            index = dq.back().second;
            dq.pop_back();
        }
        
        cout << index << ' ';
    }
    cout << dq.front().second;
    return 0;
}