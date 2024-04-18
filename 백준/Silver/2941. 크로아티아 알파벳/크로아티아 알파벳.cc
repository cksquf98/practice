#include<iostream>
using namespace std;

  
int main(int argc, char const *argv[])
{
    //크로아티아 알파벳이 발견되면 길이가 1인 다른 문자열로 변경해부리기
    cin.tie(0);
    cout.tie(0);

    string s;
    cin >> s;

    string needToCheck[8] = {"c=","c-","dz=","d-","lj","nj", "s=", "z="};  

    int index;
    for (int i = 0; i < 8; i++)
    {
        while(1)
        {
            index = s.find(needToCheck[i]);
            if(index == -1) break;

            s.replace(index, needToCheck[i].size(), "A");
        }
    }
    
    cout << s.length();
    return 0;
}