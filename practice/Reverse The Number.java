import java.util.*;
class Satish
{
    public static void main(String[] args)
    {
        int n,i,r;
        Scanner s= new Scanner(System.in);
        n=s.nextInt();
        int a[]=new int[n];
        int b[]=new int[n];
        for(i=0;i<n;i++)
        {
            a[i]=s.nextInt();
        }
        for(i=0;i<n;i++)
        {
             while(a[i]!=0)
             {
                r=a[i]%10;
                b[i]=b[i]*10+r;
                a[i]=a[i]/10;
             }
        System.out.println(b[i]);
        }
    }
}
