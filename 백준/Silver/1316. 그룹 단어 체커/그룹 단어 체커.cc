#include<iostream>
#include<vector>
#include <algorithm>
using namespace std;
int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(0);
	cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N;

    int groupWord = 0;
    for (int i = 0; i < N; i++)
    {
        string s;
        cin >> s;
        
        vector <char> V;
        V.push_back(s[0]);

        for (int j = 1; j < s.length(); j++)
        {
            
            if(find(V.begin(),V.end(),s[j]) == V.end()) 
            //<algorithm> find함수: 범위 내에 찾고자 하는 값이 없다면 end() 반환, 시간복잡도 O(n)
            {
                V.push_back(s[j]);    
                continue;
            }
            else
            {
                if(V.back() == s[j])
                    continue;
                else
                {   
                    V.clear(); 
                    break;
                }
            }
        }
        if(!V.empty())
            groupWord+=1;
    }
    cout << groupWord;
}