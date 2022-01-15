import java.util.*;
class Satish
{
    public static void main(String[] args)
    {
        long n,i,m,r;
        Scanner s=new Scanner(System.in);
        n=s.nextLong();
        for(i=1;i<=n;i++)
        {
            m=s.nextLong();
            long c=0;
           while(m!=0)
           {
            r=m%10;
            if(r==4)
            {
                c=c+1;
            }
            m=m/10;
           }
        
             System.out.println(c);
        }
    }
}
