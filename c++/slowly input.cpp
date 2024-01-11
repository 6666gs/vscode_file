#include <iostream>
#include <string>
#include <stdlib.h>
#include <windows.h>
int main()
{

    using namespace std;
    string a;
    const int time = 500;
    const int fast = 50;
    int index = 0;
    int i = 0;

    string k = "please input your password:____________"; // content that you want to display one by one
    while (k[index] != '\0')
    {
        cout << k[index++];
        Sleep(fast);
    }

    string o = "____________"; // content you want to delete
    Sleep(time);
    for (i = 0; i < o.size(); i++) // ï¿½ï¿½ï¿½ï¿½
    {

        cout << "\b \b";
        Sleep(fast);
    }
    cin >> a;
    if (a == "yun") // ï¿½ï¿½ï¿½ï¿½È¶ï¿?
    {
        for (i = 0; i < 3; i++) // ï¿½ï¿½ï¿½ï¿½
        {

            cout << "` ";
            Sleep(time);
        }
        for (i = 0; i < 6; i++)
        {

            cout << "\b \b";
        }
        for (i = 0; i < 3; i++)
        {

            cout << "` ";
            Sleep(time);
        }
        for (int i = 0; i < 6; i++)
        {

            cout << "\b \b";
        }
        Sleep(time + 500);
        cout << "right,gut~" << endl;
    }
    else
    {
        cout << "wrong!\n";
        return 0;
    }

    system("pause");
}