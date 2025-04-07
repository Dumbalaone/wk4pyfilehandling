
with open("Exist.txt","w") as file: 
    file.write("HELLO WORLD\n")

with open("Exist.txt" ,"r") as file:
    print(file.read())
    
with open("Exist.txt","r") as infile, open("New.txt","w") as outfile:
    for line in infile:
        modified_line = line.lower()
        outfile.write(modified_line)  
    
    
    
    