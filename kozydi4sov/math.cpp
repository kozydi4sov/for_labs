#include<iostream>
#include<math.h>

#define f(x) (pow(x,2)-1) 

using namespace std;
int main()
{
    double a,b,n;
    cout << "a = " ;
    cin >> a ;
    cout << "b = ";
    cin >> b ;
    cout << "n = ";
    cin >> n ;
    double deltax = (b - a)/n;
    cout << "delta x = " << deltax << endl;
    double gt = 0;
    for(float i = a; i <= b; i+=deltax){
        if(i == a or i == b){
            gt+=f(i);
        }else{
            gt+=2*f(i);
        }
    }
    double t = deltax*0.5*gt;
    cout << "Trapezoidal rule T = " << t << endl;
    double gs = 0;
    double u = deltax;
    double d = a;
    for(int i = 1; i <= n+1; i++){
        if(d == a or d == b){
            gs+=f(d);
        }else if (i%2 == 0){
            gs+=4*f(d);
        }else if(i%2 == 1){
            gs+=2*f(d);
        }
        d+=deltax;
    }
    double s = gs*deltax/3;
    cout << "Simpson's rule S = " << s;
    return 0;
}