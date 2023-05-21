#include <iostream>
#include <fstream>
#include <cstring>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string>
#include "windows.h"
using namespace std;

class conteyner {
public:
	//box==conteyner
    double mas;//main mas storage
	void open_f(){//for first boxes
		if (mas ==1){
		mas=mas-1;
		reset_f();	
		}else if(mas>1){
			mas=mas-1;
		}else{//if 0
			reset_f();
			mas=mas-1;
		}	
	}
		void open_l(){//for last boxes
		if (mas ==9){
		mas=mas+1;
		reset_l();	
		}else if(mas<1){
			mas=mas+1;
		}else{//if 10
			reset_l();
			mas=mas+1;
		}	
	}
	void reset_f(){
		mas=10;
	}
	void reset_l(){
		mas=0;
	}	
	void set(int a){
		mas=a;
	}
	double get(){
		return mas;
	}
     
    	
};



class cifdat {
public:
    double mass;//second mass storage
    bool check(int a){
    	return mass==a;
	}
	void set(int a){//set for cifdat, not for conteyner
		mass=a;
	}
	double get(conteyner b){
    	return b.get();
	}
	
    
};

class conveer {
public:
    int conv_pos[7];//6,7-boxes output
    int get(int a){
    	return conv_pos[a];
	}
	void set(int b,int a){
    	conv_pos[b]=a;
	}
	void move(){
		
	int evom_0=conv_pos[0];
	int evom_1=conv_pos[1];
	int evom_2=conv_pos[2];
	int evom_3=conv_pos[3];
	int evom_4=conv_pos[4];
	int evom_5=conv_pos[5];
	int evom_6=conv_pos[6];
	int evom_7=conv_pos[7];
	conv_pos[0]=evom_6;
	conv_pos[2]=evom_7;
	conv_pos[6]=0;
	conv_pos[7]=0;
	conv_pos[1]=evom_0;
	conv_pos[3]=evom_2;
	conv_pos[4]=max(evom_1,evom_3);
	conv_pos[5]=evom_4;
	
	}
    
};

 class andat {
public:
    double position,data;//position - dat plase,data - is active or not
    bool check(conveer a){
    	return a.get(position);
	}
	void set(int a){
		data=a;
	}
	void set_pos(int a){
		position=a;
	}
	void update(conveer a){
		data=a.get(position);
	}
    double get(){
    	return data;
	}
    
};

  class mech{
  
  	public:
  		void start(){
  			//mark detail
		  };
 

    
};
int main() {
	fstream f;
	f.open("hello_in.txt");
	setlocale(LC_ALL, "Russian");
	int in_massiv[13];  
	string line,outline,outoutline; 
	conveer q1,q2;
	conteyner k1,k2,k3,k4,c1,c2;
	cifdat a1,a2,a3,a4,m1,m2;
	andat d1,d2,d3,d4,d5,d6,i1,i2;
	mech p1,p2;
	  if (f.is_open())//in
    {
    int c,d,b;
 	cout<<"input: ";
    for(int i=0;i<=13;i++){
      	f>>c;
      	in_massiv[i]=c;
      	cout<<in_massiv[i]<<" ";
	  }
	  cout<<endl;
    }
  
    f.close(); 
    //установка датчиков
    d1.set_pos(0);//d - first box dat 
	 d2.set_pos(2);
	 d3.set_pos(0);
	 d4.set_pos(2);
	 d5.set_pos(5);//(5,6) - last box dat
	 d6.set_pos(5);
	 i1.set_pos(4);//i - mech dat
	 i2.set_pos(4);
    //установка значений в датчики
    
     a1.set(in_massiv[0]);//a - mass in dat
	 a2.set(in_massiv[1]);
	 a3.set(in_massiv[2]);
	 a4.set(in_massiv[3]);
	 k1.set(in_massiv[0]);//k - mas in box
	 k2.set(in_massiv[1]);
	 k3.set(in_massiv[2]);
	 k4.set(in_massiv[3]);
	 m1.set(in_massiv[4]);//m - mass out dat
	 m2.set(in_massiv[5]);
	 c1.set(in_massiv[4]);//c - mass out box
	 c2.set(in_massiv[5]);
	 d1.set(in_massiv[6]);//d - first box dat 
	 d2.set(in_massiv[7]);
	 d3.set(in_massiv[8]);
	 d4.set(in_massiv[9]);
	 d5.set(in_massiv[10]);//(5,6) - last box dat
	 d6.set(in_massiv[11]);
	 i1.set(in_massiv[12]);//i - mech dat
	 i2.set(in_massiv[13]);
	 q1.set(0,d1.get());
	 q1.set(2,d2.get());
	 q1.set(4,i1.get());
	 q1.set(5,d5.get());
	 q1.set(1,0);
	 q1.set(3,0);
	 q2.set(0,d1.get());
	 q2.set(2,d2.get());
	 q2.set(4,i1.get());
	 q2.set(5,d5.get());
	 q2.set(1,0);
	 q1.set(3,0);
	 q2.set(6,0);
	 q1.set(6,0);
	 q2.set(7,0);
	 q1.set(7,0);
	 
	 
	 
	 
	 
	
	 for(int i=0;i<10;i++){
	 	ofstream out;          // поток для записи
    out.open("hello_out.txt");
	 cout<<endl;
	 outline=" ";
	 
	 cout<<" 6-"<<q1.get(6)<<" 0-"<<q1.get(0)<<" 1-"<<q1.get(1)<<" 7-"<<q1.get(7)<<" 2-"<<q1.get(2)<<" 3-"<<q1.get(3)<<" 4-"<<q1.get(4)<<" 5-"<<q1.get(5)<<"//";//conveer.move() chek
	 d1.update(q1);//d - first box dat 
	 d2.update(q1);
	 d3.update(q2);
	 d4.update(q2);
	 d5.update(q1);//(5,6) - last box dat
	 d6.update(q2);
	 i1.update(q1);//i - mech dat
	 i2.update(q2);
	 
	//first boxes
	if(k1.get()==10)
	
	 if(d1.get()==0 and d2.get()==0){
	 	outline=outline+"k1.open,  ";
	 	k1.open_f();
	 	q1.set(6,1);
	 }else if(d1.get()==1 and d2.get()==1){
	 	outline=outline+"error collision,  ";
	 	cout<<"error collision q1,  ";
	 	out <<"error collision q1,  ";
	 	exit(0);
	 }else if(d1.get()==0 and d2.get()==1){
	 	outline=outline+"k1.open,  ";
	 	k1.open_f();
	 	q1.set(6,1);
	 }else if(d1.get()==1 and d2.get()==0){
	 	outline=outline+"k2.open,  ";
	 	k2.open_f();
	 	q1.set(7,1);
	 }else{
	 	outline=outline+"error wrong input,  ";
	 	cout<<"error wrong input, ";
	 	out <<"error wrong input, ";
	 	exit(0);
	 }
	 d1.update(q1);//d - first box dat 
	 d2.update(q1);
	 d3.update(q2);
	 d4.update(q2);
	 d5.update(q1);//(5,6) - last box dat
	 d6.update(q2);
	 i1.update(q1);//i - mech dat
	 i2.update(q2);
	 cout<<" 6-"<<q1.get(6)<<" 0-"<<q1.get(0)<<" 1-"<<q1.get(1)<<" 7-"<<q1.get(7)<<" 2-"<<q1.get(2)<<" 3-"<<q1.get(3)<<" 4-"<<q1.get(4)<<" 5-"<<q1.get(5)<<"//";//conveer.move() chek
	 //mech
	if(i1.get()==1){
	 	outline=outline+"p1.start,  ";
	 	p1.start();
	 }else if(i1.get()==0){

	 }else{
	 	cout<<"error wrong input, ";
	 	out <<"error wrong input, ";
	 	exit(0);
	 }
	 //last box
	 if(d5.get()==1){
	 	outline=outline+"c1.open_l,  ";
	 	c1.open_l();
	 }else if(d5.get()==0){
	 	
	 }else{
	 	cout<<"error wrong input, ";
	 	out <<"error wrong input, ";
	 	exit(0);
	 }
	 //q2
	  
	//first boxes
	 if(d3.get()==0 and d4.get()==0){
	 	outline=outline+"k3.open,  ";
	 	k3.open_f();
	 	q2.set(6,1);
	 }else if(d3.get()==1 and d4.get()==1){
	 	outline=outline+"error collision,  ";
	 	cout<<"error collision q2,  ";
	 	out <<"error collision q2,  ";
	 	exit(0);
	 }else if(d3.get()==0 and d4.get()==1){
	 	outline=outline+"k3.open,  ";
	 	k3.open_f();
	 	q2.set(6,1);
	 }else if(d3.get()==1 and d4.get()==0){
	 	outline=outline+"k4.open,  ";
	 	k4.open_f();
	 	q2.set(7,1);
	 }else{
	 	outline=outline+"error wrong input,  ";
	 }
	 d1.update(q1);//d - first box dat 
	 d2.update(q1);
	 d3.update(q2);
	 d4.update(q2);
	 d5.update(q1);//(5,6) - last box dat
	 d6.update(q2);
	 i1.update(q1);//i - mech dat
	 i2.update(q2);
	 cout<<"q2 "<<" 6-"<<q2.get(6)<<" 0-"<<q2.get(0)<<" 1-"<<q2.get(1)<<" 7-"<<q2.get(7)<<" 2-"<<q2.get(2)<<" 3-"<<q2.get(3)<<" 4-"<<q2.get(4)<<" 5-"<<q2.get(5)<<"//";//conveer.move() chek
	 //mech
	if(i2.get()==1){
	 	outline=outline+"p1.start,  ";
	 	p1.start();
	 }else if(i2.get()==0){
	 	
	 }else{
	 	cout<<"error wrong input, ";
	 	out <<"error wrong input, ";
	 	exit(0);
	 }
	 //last box
	 if(d6.get()==1){
	 	outline=outline+"c1.open_l,  ";
	 	c1.open_l();
	 }else if(d6.get()==0){
	 	
	 }else{
	 	cout<<"error wrong input, ";
	 	out <<"error wrong input, ";
	 	exit(0);
	 }
	
	

	
	
    if (out.is_open())
    {
        cout <<"output: "<< outline<< endl;
         out <<"output: "<< outoutline << endl;
    }
    out.close(); 
    outoutline=outoutline+outline+"endl";
    Sleep(1000);
    q1.move();
    q2.move();
}
ofstream out;          // поток для записи
    out.open("hello_out.txt");
 if (out.is_open())
    {
    	 out <<"output: "<< outoutline << endl;
    }
out.close(); 
    return 0;
}
