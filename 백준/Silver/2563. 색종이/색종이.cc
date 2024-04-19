#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    cin.tie(0);
    cout.tie(0);
    
    int paper[101][101] = {0,};

    int num;
    cin >> num;
    while(num)
    {
        num--;
        int x,y;
        int x_end, y_end;

        cin >> x >> y;
        
        x_end = x+10;
        y_end = y+10;
        if(x_end > 100) x_end = 100;
        if(y_end > 100) y_end = 100;

        for(int i = x; i < x_end; i++)
        {
            for(int j = y; j < y_end; j++)
            {
                paper[i][j] = 1;
            }
        }

    }
    int blackPaper = 0;
    for(int i = 0; i <= 100; i++)
        {
            for(int j = 0; j <= 100; j++)
            {
                blackPaper += paper[i][j];
            }
        } 
    cout << blackPaper; 
}