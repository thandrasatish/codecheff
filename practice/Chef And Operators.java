import java.util.*;
class Satish{
    public static void main(String[] args)
    {
        int n,i,j;
        Scanner s= new Scanner(System.in);
        n=s.nextInt();
        int a[]=new int[n];
        int b[]=new int[n];
        for(i=0;i<n;i++)
        {
            a[i]=s.nextInt();
            b[i]=s.nextInt();
        }
        for(i=0;i<n;i++)
        {
            if(a[i]>b[i])
            System.out.println(">");
            else if(a[i]<b[i])
            System.out.println("<");
            else
            System.out.println("=");
        }
        
    }
}
