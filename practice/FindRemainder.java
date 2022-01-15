import java.util.*;
public class Main
{
    public static void main(String[] args)
    {
        int n,i,a,b,c=0;
        Scanner s = new Scanner(System.in);
        n=s.nextInt();
        for(i=0;i<n;i++)
        {
            a=s.nextInt();
            b=s.nextInt();
            c=a%b;
            System.out.println(c);
        }
        
    }
}
