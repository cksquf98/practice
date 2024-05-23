// EOF : END IF FILE
// 더이상 읽어올 데이터가 없는 상태!!!!!!!!!!!!!!!!

#include <string>
#include <iostream>
#include <cmath>

using namespace std;

string result = "";
void Cantor(int len)
{
    if (len == 1)
    {
        result += "-";
        return;
    }

    int interval = len / 3;
    Cantor(interval);
    for (int i = 0; i < interval; i++)
    {
        result += " ";
    }
    Cantor(interval);
}

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    while(cin >> N)
    {
        int len = pow(3, N);
        int interval = len / 3;
        Cantor(len);

        cout << result << '\n';
        result = "";
    }
    return 0;
}