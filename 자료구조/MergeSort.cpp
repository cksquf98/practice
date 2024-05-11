#include<iostream>
#include<algorithm>
using namespace std;

void Combine(int left, int mid, int right, int *arr);

void MergeSort(int left, int right, int *arr)
{
    if(left < right)
    {   
        int mid = (left + right) / 2;
        MergeSort(left, mid, arr);
        MergeSort(mid+1, right, arr);

        Combine(left,mid,right, arr);
    }
}

void Combine(int left, int mid, int right, int *arr)
{
    int sortedArr[right - left + 1] = {0,};

    int i,j,k;
    i = left;       //첫번째 분할된 arr의 인덱스
    j = mid + 1;    //두번째 분할된 arr의 인덱스
    k = 0;          //정렬되어 들어갈 배열인 sortedArr 인덱스

    while (i <= mid && j <= right)
    {
        if(arr[i] <= arr[j])                //2개의 리스트의 값들을 처음부터 하나씩 비교
            sortedArr[k++] = arr[i++];      //후위 연산자 주의!

        else
            sortedArr[k++] = arr[j++];
    }
    
    if(i > mid) //첫번째 arr 끝 -> 두번째 arr에 남아있는 애들 통채로 넣으면 됨
    {
        while(j <= right)
        {
            sortedArr[k++] = arr[j++];
        }
    }   
    else    //두번째 arr 끝
    {
        while(i <= mid)
        {
            sortedArr[k++] = arr[i++];
        }
    }
    
    // for (int w = 0; w < sizeof(sortedArr)/sizeof(int); w++)
    // {
    //     cout << sortedArr[w] << " ";
    // }
    // cout << "\n-----------------\n";

    // 새로운 리스트를 원래 리스트로 복사
    i = left; k = 0;
    while(i <= right)
    {
        arr[i++] = sortedArr[k++];
    }
    cout << endl;
}


int main(int argc, char const *argv[])
{
    int arr[] = {5,3,2,4,1,9,7,8,6,10};

    int len = sizeof(arr) / sizeof(int);
    MergeSort(0,len-1, arr);

    cout <<"\nFINAL\n";
    for (int i = 0; i < len; i++)
    {
        cout << arr[i] << " ";
    }
    
    return 0;
}
