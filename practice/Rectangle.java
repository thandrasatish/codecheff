import java.util.*;
class codecheff
{
    public static void main(String[] args)
    {
        int n,i,a,b,c,d;
        Scanner s=new Scanner(System.in);
        n=s.nextInt();
        for(i=0;i<n;i++)
        {
            a=s.nextInt();
            b=s.nextInt();
            c=s.nextInt();
            d=s.nextInt();
            if(a==d && b==c || a==b && c==d || a==c && b==d)
            System.out.println("YES");
            else
            System.out.println("NO");
        }
        
    }
}
