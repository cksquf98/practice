// menOfPassion 함수 : 입력값N에 따른 삼중포문
// MenOfPassion(A[], n) {
//     sum <- 0;
//     for i <- 1 to n
//         for j <- 1 to n
//              for k <- 1 to n
//                  sum <- sum + A[i] × A[j] x A[k]; # 코드1 
//     return sum;
// }

#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    cin.tie(0);
    cout.tie(0);
    unsigned long long N;
    cin >> N;

    // MenOfPassion함수 : N^3번 수행되고, 시간복잡도 O(N^3)
    cout << N*N*N << "\n" << 3;
    return 0;
}