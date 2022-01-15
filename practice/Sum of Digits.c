#include<stdio.h>
int main()
{
  	int t,i;
   	scanf("%d",&t);
   	for(i=0;i<t;i++)
   	{
   		int n,sum=0; 
   		scanf("%d",&n);
   		while(n!=0)
   		{
	   		sum+=n%10; n/=10;
   		}
    	printf("%d\n",sum);
    }
}
