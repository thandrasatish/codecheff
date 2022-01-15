import java.util.*;
class Satish
{
    public static void main(String[] args)
    {
        int n,i,a,b,c;
        Scanner s=new Scanner(System.in);
        n=s.nextInt();
        for(i=0;i<n;i++)
        {
            a=s.nextInt();
            b=s.nextInt();
            c=s.nextInt();
            if(a+b+c==180)
            {
                System.out.println("YES");
            }
            else
            {
                System.out.println("NO");
            }
        }
        
    }
}
