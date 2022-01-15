import java.util.*;
class Codechef
{
	public static void main (String[] args) 
	{
	    int i,n,sum,m,l;
		Scanner s=new Scanner(System.in);
		n=s.nextInt();
		for(i=0;i<n;i++)
		{
		    m=s.nextInt();
		    l=m%10;
		    while(m>=10)
		    {
		        m=m/10;
		    }
		    sum=l+m;
		    System.out.println(sum);
		}
	}
}
