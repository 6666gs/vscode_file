#include <iostream>
using namespace std;
struct test
{
    int number;
    char t;

    test(int a,char b)
    {
        number = a;
        t = b;
    }
    void print()
    {
        std::cout << number << " " << t << endl;
    }
};

int main()
{
    test the_test(1,'a');
    the_test.print();
    return 0;
}