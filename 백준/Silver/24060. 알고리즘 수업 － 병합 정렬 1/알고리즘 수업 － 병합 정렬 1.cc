#include <iostream>
using namespace std;

int count = 0;
int result = -1;    //아... result를 저장하는 전역변수에 담으면 될걸!!! 함수 반환으로 해결하려다가 푸는데 오래걸림
unsigned long int len, K;

void Combine(int left, int right, int *arr)
{
    int mid = (left + right) / 2;

    int sortedArr[right - left + 1] = {0,};
    int i,j,k;

    i = left; j = mid+1; k = 0;

    while(i <= mid && j <= right)
    {
        if(arr[i] <= arr[j])    
        {
            sortedArr[k++] = arr[i++];
        }
        else
        {
            sortedArr[k++] = arr[j++];
        }
    }

    if(i > mid)
    {
        for (int p = j; p <= right; p++)
        {
            sortedArr[k++] = arr[j++];
        }
    }
    else
    {
        for (int q = i; q <= mid; q++)
        {
            sortedArr[k++] = arr[i++];
        }
        
    }


     // 새로운 리스트를 원래 리스트로 복사
    i = left; k = 0;
    while(i <= right)
    {
        count++;

        if(count == K)
        {
            result = sortedArr[k];
        }

        arr[i++] = sortedArr[k++];
    }
}
void MergeSort(int left, int right, int *arr)
{
    if (left < right)
    {
        int mid = (left + right) / 2;

        MergeSort(left, mid, arr);
        MergeSort(mid + 1, right, arr);

        Combine(left, right, arr);
    }
}

int main(int argc, char const *argv[])
{

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> len >> K;

    int arr[len+1] = {0,};

    for (int i = 0; i < len; i++)
    {
        cin >> arr[i];
    }
    
    MergeSort(0, len-1, arr);

    cout << result;
     
    return 0;
}
