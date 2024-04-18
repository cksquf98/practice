// 입력
// 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

// 출력
// 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(0);
	cin.tie(NULL);
    int N;
    cin >> N;

    int t = 0;
    for (int i = 0; i < (2*N-1); i++)
    {
        for (int j = 0; j < N-t-1; j++)   // * 찍기 전 공백 출력
        {
            cout << ' ';
        }
        for(int k = N-t; k <= N+t ; k++)    // * 찍는 반복문: N 앞뒤로 t만큼 찍기
        {
            cout << '*';
        }
        for (int j = N+1; j <= N-2; j++)      // * 찍은 후 공백
        {
            cout << ' ';
        }
        cout << "\n";

        if(i<N-1) t++;      // N번째 줄에서 최대 별 개수 찍음 => N번째 줄부터 t 감소시키기
        else    t--;
    }
}