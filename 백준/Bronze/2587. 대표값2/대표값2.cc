// Array 길이 계산: sizeof(array_name)/sizeof(int,or... type)와 같이 type의 사이즈로 나누어 계산

#include<iostream>
using namespace std;

int input[5] = {0,};
/* 
void setSeat(int num,int index)
{
    int tmp = input[index];       
    input[index] = num;
    for (int k = index+1; k < 5; i++)
    {
        if(input[k] == 0)   
        {
            index[k] = tmp;
            break;
        }
        tmp = input[k];
        input[k] = tmp;
        흠..
    }
    
}
*/

int average()
{
    int sum = 0;
    for (int i = 0; i < 5; i++)
    {
        sum += input[i];
    }
    return sum/5;
}

void sorting()
{
    for (int i = 0; i < 5; i++)
    {
        for (int j = i+1; j < 5; j++)
        {
            int tmp = input[i];
            if(input[i] > input[j])
            {
                input[i] = input[j];
                input[j] = tmp;
            }
        }
    }
    
}

int main(int argc, char const *argv[])
{
    
    // 방법1. 입력 받으면서 값 비교하면서 자리 저장하게 하기
    // 방법2. 입력 다 받고 배열 한방에 정렬하기
    for (int i = 0; i < 5; i++)
    {
        cin >> input[i];
    }
    
    sorting();
        
    cout << average() << '\n' << input[2];
    
    return 0;
}
