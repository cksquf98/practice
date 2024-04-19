#include<iostream>
#include<string>
using namespace std;
int cal_3KG(int rest)
{
    if(rest % 3 == 0)   return rest / 3;
    else    return -1;
}

int main(int argc, char const *argv[])
{
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N;

    int bongjiMin = 10000000;

/* 
for문 1번 돌릴 때 -> -5kg 했을 때 3kg 계산 -> 봉지 수 카운트
      2번 돌릴 때 -> -5kg * 2번
      ...

      실패!!!!!!

      3kg 계산하는 함수를 만들어서 for문 돌릴때 호출 -> 최솟값 비교 << 요렇게 해봐야겠다      
*/

    int sugar = N;  
    int bongji = 0;

    if(sugar % 3 == 0)  bongjiMin = sugar / 3;

    for (int i = 1; sugar - i*5 >= 0;) 
    {  
        sugar = sugar - 5*i;   
        bongji = i;     

        int rest = cal_3KG(sugar);
        if (rest == -1)
        {
            sugar = N;
            i++;
        }
        else
        {
            // printf("bongji = %i, rest = %i\n", bongji, rest);
            bongji += rest;
            if(bongji <= bongjiMin)
            {
                bongjiMin = bongji;
                i++;
                sugar = N;
            }
        }
    }
    if (bongjiMin == 10000000) cout << -1;
    else    cout << bongjiMin;
}