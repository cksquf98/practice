#include<iostream>
#include<algorithm>
using namespace std;

int arr[] = {5,3,2,4,1,9,7,8,6,10};

int Partition(int left, int right);

void QuickSort(int left, int right)
{
    if(left >= right)   return;

    // 전체 배열에 대한 분할
    int pivot = Partition(left, right);

    QuickSort(left, pivot-1);
    QuickSort(pivot+1, right);
}




/*  Partion 함수
    pivot 기준으로 왼쪽(작은 값)에 있는데 pivot보다 큰 놈과
             오른쪽(큰 값)에 있는데 pivot보다 작은놈 각각 하나씩 찾아서 Swap 
*/
int Partition(int left, int right)
{
    int pivot = arr[left];  //그냥 가장 왼쪽 값을 pivot으로 설정
    int i = left;
    int j = right;

    while(i < j)   
    {
        while (arr[j] > pivot)
        {
            // arr[j]중에 pivot보다 작거나 같은 놈을 찾기 전까지 반복
            j--;
        }

        while(i < j && pivot >= arr[i])
        {
            //arr[i]중에 pivot보다 큰 놈을 찾기 전까지 반복
            i++;
        }
        
        swap(arr[i],arr[j]);
    }

    //pivot보다 작거나 같은 놈이니까 pivot이랑 위치 바꿔
    arr[left] = arr[i];
    arr[i] = pivot;


    //pivot 위치 반환
    return i;
}



int main(int argc, char const *argv[])
{
    int length = sizeof(arr)/sizeof(int);
    QuickSort(0,length-1);

    for (int index = 0; index < length; index++)
    {
        cout << arr[index] << '\n';
    }
    
    return 0;
}
