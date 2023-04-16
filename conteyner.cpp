#include <iostream>
#include <cmath>
#include <windows.h>
using namespace std;


class conteyner {
public:
    double mass;
	void open(){
    	mass--1;
    	
	}
	void reset(){
		mass=10;
	}
    
};

 
int main()
{
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    setlocale(LC_ALL, "Russian");

    return 0;
}
