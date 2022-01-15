import java.util.*;
class Satish{
    public static void main(String[] args)
    {
        int n,i,j;
        Scanner s= new Scanner(System.in);
        n=s.nextInt();
        int a[]=new int[n];
        for(i=0;i<n;i++)
        {
            a[i]=s.nextInt();
        }
        for(i=0;i<n;i++)
        {
            if(a[i]<10)
            System.out.println("Thanks for helping Chef!");
            else
            System.out.println("-1");
        }
        
    }
}
