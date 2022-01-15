#include <stdio.h>
int main(void) 
{
int n,i,c1=0,c2=0;
int a[10000];
scanf("%d",&n);
for(i=0;i<n;i++)
{
    scanf("%d",&a[i]);
    if(a[i]%2==0)
    c1=c1+1;
    else
    c2=c2+1;
    
}
if(c1>c2)
printf("READY FOR BATTLE");
else
printf("NOT READY");
}

