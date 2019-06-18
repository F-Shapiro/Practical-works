#include <iostream>

using std::cout;
using std::endl;

int main()
{
int start = 97;

for(char i = 'a'; i <= 'z'; i++)
{
cout « i « " " « start « endl;
start++;
}

return 0;
}