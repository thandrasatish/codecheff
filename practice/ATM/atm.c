#include <stdio.h>
int main(void) 
{
int x;
float y;
scanf("%d%f",&x,&y);
if(x<=(y-.50) && x%5==0)
{
printf("%.2f",(y-x-.50));
}
else
printf("%.2f",y);
return 0;
}

