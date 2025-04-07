filename = input("Enter a file name: ")

try:
    with open(filename,encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
        print(f'Sorry, the file {filename} does not exist')
except PermissionError:
    print(f'Sorry, the file {filename} exists but cannot be read')        
else:
       print(f'the file {filename} was found') 
