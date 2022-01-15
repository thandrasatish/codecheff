#include<stdio.h>
int main() 
{
    long int n,i,c=0,m,j;
    scanf("%ld",&n);
    for(i=1;i<=n;i++)
    {
        scanf("%ld",&m);
        c=0;
        for(j=1;j<=m;j++)
        {
          if(m%j==0)
          c=c+1;
        }
        if(c==2)
        printf("yes\n");
        else
        printf("no\n");
        
    }
    
}
