n=1
while(n<2): #create 1 file
    m=str(n)
    z=".dll"
    f="file_" # Specify the file name
    file_name =f+m+z
    with open(file_name, 'w') as file: # Open the file in write mode ('w')     
        file.write("Hello, this is an example file.\n")   # Write content to the file
        file.write("You can add more lines if you want.")
    print(f"File '{file_name}' has been created and saved.") #diplay the location of files, especially the default location is location of this programme
    n=n+1