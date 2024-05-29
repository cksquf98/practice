#include <iostream>
#include <vector>
#include <deque>

using namespace std;
int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    int N;
    cin >> N;

    vector <int> selector;
    deque <int> dq;

    for (int i = 0; i < N; i++)
    {
        int QueueOrStack;
        cin >> QueueOrStack;
        selector.push_back(QueueOrStack);
    }
    
    for (int j = 0; j < N; j++)
    {
        int num;
        cin >> num;
        if(selector[j]==0)  dq.push_back(num);
    }

    int M;
    cin >> M;
    for (int k = 0; k < M; k++)
    {
        int num;
        cin >> num;

        //0이면 기존꺼가 나가고 1이면 들어올라는 애가 나가니까
        if(dq.empty())  cout << num << ' ';
        else
        {
            cout << dq.back() << ' ';
            dq.pop_back();
            dq.push_front(num);
        }
    }
    return 0;
}