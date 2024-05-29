// 요세푸스 순열
// 큐를 우찌 써야할까나
//(7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

#include<iostream>
#include<queue>
using namespace std;

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N,K;
    int idx;
    queue <int> input;

    cin >> N >> K;

    for (int i = 1; i <= N; i++)
    {
        input.push(i);
    }

    cout << "<";
    while(!(input.empty()))
    {
        if(input.size() == 1)   //마지막 숫자는 쉼표 안붙으니까 따로 처리했음
        {
            cout << input.front();
            input.pop();
            break;
        }

        for (int i = 1; i < K; i++)
        {
            int num = input.front();   //K-1까지 팝팝
            input.pop();

            input.push(num); //뒤로 보내기
        }
        cout << input.front() << ", ";
        input.pop();
    }
    cout << ">";
}