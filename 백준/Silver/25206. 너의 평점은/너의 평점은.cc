#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    cin.tie(0);
    cout.tie(0);

    float totalGradeNum = 0.0;
    float totalPoint = 0.0;

    for (int i = 0; i < 20; i++)
    {
        string subject;
        float point; //학점
        string grade;

        cin >> subject >> point >> grade;
        float currentGrade = 0.0;
        if(grade[1]=='+') 
        {
            currentGrade += 0.5;
        }
        switch (grade[0])
        {
            case 'A':
        {
            totalPoint += point;
            currentGrade += 4.0; 
            totalGradeNum += currentGrade * point;
            break;
        }
            case 'B':
        {
            totalPoint += point;
            currentGrade += 3.0; 
            totalGradeNum += currentGrade * point;
            break;
        }
            case 'C':
        {
            totalPoint += point;
            currentGrade += 2.0; 
            totalGradeNum += currentGrade * point;
            break;
        }
            case 'D':
        {
            totalPoint += point;
            currentGrade += 1.0; 
            totalGradeNum += currentGrade * point;
            break;
        }
        case 'F':
        {
            totalPoint += point;
            break;
        }
        }
    }
    double res = totalGradeNum / totalPoint;
    cout << res;
}