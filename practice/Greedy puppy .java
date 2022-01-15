import java.util.*;
class Satish
{
    public static void main(String[] args)
    {
       long n,a,b,r;
       int i,j;
       Scanner s=new Scanner(System.in);
       n=s.nextLong();
       long min=-1;
    for(i=1;i<=n;i++)
    {
        min=-1;
        a=s.nextLong();
        b=s.nextLong();
        for(j=1;j<=b;j++)
        {
            r=a%j;
            if(r>min)
            min=r;
        }
        System.out.println(min);
    }
    }
}
