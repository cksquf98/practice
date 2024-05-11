#include<iostream>
#include<stack>
using namespace std;
// 6
// 3 2 1 4 5 6
// 이 케이스 생각해보기

int stackCheck(stack <int> &waiting, int turn)
{
    if(!(waiting.empty()))
    {
        while(1)   //비어있지 않을 때까지 반복
        {
            if(waiting.empty()) 
                return turn;
            
            if(waiting.top() == turn)
            {   
                turn ++;
                waiting.pop();
            }
            else
            {
                return turn;
            }
        }
    }
    return turn;
}

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    stack <int> waiting;
    int turn = 1;
    int check = waiting.empty();
    int arr[1000] = {0,};
    int N;

    cin >> N;
    for (int j = 0; j < N; j++)
    {
        cin >> arr[j];
    }

    for (int i = 0; i < N; i++)
    {
        int num = arr[i];

        if(turn == num)
        {
            turn++;
            continue;
        }
        else
        {
            turn = stackCheck(waiting, turn);
            if(turn == num)
            {
                turn++;
                continue;
            }
            else
            {
                // cout << "pushing "<< num <<endl;
                waiting.push(num);
            }
        }
        
    }
    turn = stackCheck(waiting, turn);

    if(waiting.empty())  cout << "Nice";
    else     cout << "Sad";
   

    return 0;
}