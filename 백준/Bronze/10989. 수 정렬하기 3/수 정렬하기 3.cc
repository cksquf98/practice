//카운팅 정렬로 이 메모리가 나오나..???
//와 나 이런 방법이 있었다니-_-;;

#include<iostream>
#include<list>
using namespace std;

int arr[10001] = {0};

int main(int argc, char const *argv[])
{
    cin.tie(0);
    cout.tie(0);
    int N;
    cin >> N;

    // 숫자 개수 카운트
    for(int i = 0 ; i < N; i++){
        int a;
        cin >> a;
        arr[a] += 1;
    }

    // 각 숫자를 개수만큼 출력해주기
    for(int i = 1 ; i <= 10000; i++)
        for (int j = 0; j < arr[i]; j++)
            cout << i << "\n";
}