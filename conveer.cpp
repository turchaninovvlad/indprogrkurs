#include <iostream>
#include <cmath>
#include <windows.h>
using namespace std;


class conveer {
public:
    bool p;
    bool check(){
    	return p;
	}
	void on(){
		p=1;
	}
    double off(){
    	p=0;
	}
    
};

 
int main()
{
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    setlocale(LC_ALL, "Russian");

    return 0;
}
