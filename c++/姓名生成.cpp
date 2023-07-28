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
    int a;      //a为人数
    cin >> a;     //输入人数a
    id * p = new id[a];
    for (int i = 0; i < a;i++)
    {
        p[i] = randpo();             //为第i个人随机生成信息
    }

for (int i = 0; i < a;i++)
    {
        cout << i<<"    "<<"age:"<<p[i].age;       //输出信息
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
    
    

    string firstname[22] = {"赵",
                              "钱",
                              "孙", "李", "周", "吴", "郑", "王", "刘", "孟","妮","莫","墨","帝","月","瑞","秋","明风","斯","千","万","婉"};
    string seconname[16] = {"明", "月", "华", "独", "嫣", "繁", "星", "水", "红", "时", "秋", "雪", "纱", "鸥", "千", "蔚"};
    string thirdname[25] = {"明", "月", "华", "独", "嫣", "繁", "星", "水", "红", "时", "秋", "雪", "纱", "鸥", "千", "蔚"
    ,"涵","如","然","冉","萌","器","斯","帝","畏"};
    string le = "ABCD";
    a.name = firstname[random(21)] + seconname[random(16)] + thirdname[random(25)];
    a.age = random(25);
    a.level = le[random(4)];
    a.rank = random(1000);
    return a;
}