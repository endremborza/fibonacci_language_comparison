#include <iostream>

using namespace std;

int fib(int n)
{
    if(2 > n)
    {
        return 1;
    }
    else
    {
        return fib(n-1)+fib(n-2);
    }

}

int main()
{
    for(int i=1;i<41;i++){
        cout << i << " . fibonacci: " << fib(i) << endl;
    }
    return 0;
}
