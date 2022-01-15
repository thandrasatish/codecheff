import java.util.*;
class MyClass {
    public static void main(String args[])
    {
        int n;
      Scanner s=new Scanner(System.in);
      n=s.nextInt();
      if(n%4==0)
      {
          n=n+1;
      }
      else
      {
          n=n-1;
      }
      System.out.println(n);
     
    }
}
