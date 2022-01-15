import java.util.*;
import java.util.Arrays;
class Codechef
{
	public static void main (String[] args)
	{
		int n,i,j;
		Scanner s=new Scanner(System.in);
		n=s.nextInt();
		int a[]=new int[n];
		for(i=0;i<n;i++)
		{
		    a[i]=s.nextInt();
		}
		 Arrays.sort(a);
		 for(i=0;i<n;i++)
		{
		   System.out.println(a[i]);
		}
		 
	}
}
