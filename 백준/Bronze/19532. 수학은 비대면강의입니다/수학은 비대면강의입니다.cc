#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    cin.tie(0);
    cout.tie(0);
    
    int a,b,c,d,e,f;
    cin >> a >> b >> c >> d >> e >> f;

    int x,y;
    
    y = (d*c - a*f) / (d*b - a*e);
    // x = (c - b*y) / a; 이러면 a가 0인 경우 문제가 생김
    x = (c*e - b*f) / (a*e - b*d);

    cout << x << " " << y;
    return 0; 
}