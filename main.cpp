#include <iostream>
#include <random>
#include <windows.h>

using namespace std;

void move_cur(int x, int y){
    printf("\033[%d;%dH",y,x);
}

int main()
{
    random_device dv;
    
    mt19937 gen(dv());
    uniform_int_distribution<> xdist(0,65);
    uniform_int_distribution<> ydist(0,25);
    int count=0;
    while(true){
        if(count <150) break;
        move_cur(xdist, ydist);
        cout << "*";
        Sleep(1000);
        cout++;
    }
    getchar();

    return 0;
}
