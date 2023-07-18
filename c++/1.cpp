#include <iostream>
#include <string>
#include <time.h>
#define random(x) (rand()%x)
int main()
{
    using namespace std;
    srand((int)time(0));
    enum ahk
    {
        red,green,orange,yellow
    };
    ahk band;
    band = red;
    cout << band<<endl;
    int c = random(10);
    int b = random(10);
    int a = random(10);
    cout <<c<<endl<<a<<endl<<b<<endl;
    system("pause");
    return 0;
}