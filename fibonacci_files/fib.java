class fib {
    public static int fib(int n) {
       if(2 > n)
            return 1;
        else
            return fib(n-1)+fib(n-2);

    }

    public static void main(String[] args) {


        for(int i=1;i<41;i++){
            
            System.out.println(i + ". fibonacci:" + fib(i));
            
        }


    }
}
