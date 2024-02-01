while(1):
    a=int(input("Enter a number: "));
    n=int(2);
    x=int(0);
    if(a>2):
        x=a-1;
    elif(a==0):
        print("The given number",a,"is neither prime nor composite");
    elif(a<0):
        print("The given number",a,"is negative");
    while(x>n):  #checking the all possibile divisor
        if(a%n==0):
            print("The given number",a,"is not a prime number");
            print("because",a,"is divisible by",n); #display result 1
            n=x+1;
        n=n+1;
    if(n==x or a==1 or a==2 ):
        print("The given number",a,"is a prime number"); #display the result 2
        n=x+1;

            
            
        
        
        
        
        
