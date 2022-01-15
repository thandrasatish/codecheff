#include<stdio.h>
int main()
{
    int n,i,a,b,j;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d %d\n",&a,&b);
        for(j=0;j<a;j++)
        {
          b=b*(b+1)/2;
        }
       
        printf("%d\n",b);
    }
}
