#include <iostream>
#include <string>
#include <time.h>
#include <windows.h> 
#define random(x) (rand()%x)
using namespace std;
struct id 
{
    string name;
    int age;
    char level;
    int rank;
};
id randpo(void);
int main()
{
srand((int)time(0));
    int a;      //aΪ����
    cin >> a;     //��������a
    id * p = new id[a];
    for (int i = 0; i < a;i++)
    {
        p[i] = randpo();             //Ϊ��i�������������Ϣ
    }

for (int i = 0; i < a;i++)
    {
        cout << i<<"    "<<"age:"<<p[i].age;       //�����Ϣ
        cout << "    "
             << "name:" << p[i].name
             << "    "
             << "rank:" << p[i].rank
             << "    "
             << "level:" << p[i].level<<endl;



    }
    delete[] p;
    system("pause");


}



id randpo(void)
{
    id a;
    
    

    string firstname[22] = {"��",
                              "Ǯ",
                              "��", "��", "��", "��", "֣", "��", "��", "��","��","Ī","ī","��","��","��","��","����","˹","ǧ","��","��"};
    string seconname[16] = {"��", "��", "��", "��", "��", "��", "��", "ˮ", "��", "ʱ", "��", "ѩ", "ɴ", "Ÿ", "ǧ", "ε"};
    string thirdname[25] = {"��", "��", "��", "��", "��", "��", "��", "ˮ", "��", "ʱ", "��", "ѩ", "ɴ", "Ÿ", "ǧ", "ε"
    ,"��","��","Ȼ","Ƚ","��","��","˹","��","η"};
    string le = "ABCD";
    a.name = firstname[random(21)] + seconname[random(16)] + thirdname[random(25)];
    a.age = random(25);
    a.level = le[random(4)];
    a.rank = random(1000);
    return a;
}