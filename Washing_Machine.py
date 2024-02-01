#Program for automatic washing machine
import time #time delay for each rotation
SWITCH=str(input("Enter '1' for start:"));
if(SWITCH=="1"):
    a=int(0);
    b=int(0);
    c=int(0);
    d=int(0);
    e=int(0);
    t=int(input("Set Time In Minutes: ")); #defines the number of cycles and time taken to complete the process
    e=t*60;
while(d<e):
    if(a==b):
        c=0;
        a=a+1;
        print("Motor Rotating Clockwise...");
        while(a>c):
            c=c+1;
            z=2  #time taken for each rotation
            time.sleep(z)
            print(c,"rotation complete");
            d=d+2; # ASSUME MACHINE RUNS AT 30 RPM           
    if(a>b):
        c=0;
        b=b+1;
        print("Motor Rotating Anti-clockwise...");
        
        
        while(b>c):
            c=c+1;
            z=2  #time taken for each rotation
            time.sleep(z)
            print(c,"rotation complete");
            d=d+2; # ASSUME MACHINE RUNS AT 30 RPM
print(".....Process Complete.....");            
                
                
