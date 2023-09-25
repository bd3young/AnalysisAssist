import os
import datetime
import ipaddress

# function that checks if a directory exists
def DirExists(uPath, currentPath = ''):
    if os.path.exists(uPath + currentPath):
        return True
    else:
        return False

# function that creates a directory in the current path
def CreateDir(uPath, currentPath):
    if DirExists(uPath, currentPath):
        c = len(f'| The Directory {uPath}{currentPath} already exsists |')
        Clear()
        print(f'''{c * '-'}
| The Directory {uPath}{currentPath} already exsists |
{c * '-'}''')
    else:
        c = len(f'| The Directory {uPath}{currentPath} has been created |')
        os.system(f'''cd {uPath} 
            mkdir {currentPath}''')
        Clear()
        print(f'''{c * '-'}
| The Directory {uPath}{currentPath} has been created |
{c * '-'}''')

# function that creates a files within the current path
def CreateFile(uPath, mainPath, currentPath, ip, p = ''):
    c = len(f'| {ip}{currentPath}{(datetime.datetime.now()).strftime("%Y-%m-%d%H:%M:%S")}.txt has been created in the following location {userPath}{mainPath} |')
    print('\nFile is being created please be patient...')
    os.system(f''' cd {uPath}{mainPath}
                    {currentPath.lower()} {p} {ip} > {ip.replace('/', '-' )}{currentPath}{(datetime.datetime.now()).strftime("%Y-%m-%d%H:%M:%S")}.txt''') 
    Clear()
    print(f'''{c * '-'}
| {ip.replace('/', '-' )}{currentPath}{(datetime.datetime.now()).strftime("%Y-%m-%d%H:%M:%S")}.txt has been created in the following location {userPath}{mainPath} |
{c * '-'}''')

# function to ask for user input of an IPAddress and validate it
def IpAddress():
    while True:
        ip = input("Enter the IP Address \n\ninput - ")
        if ip[-2] == '/' or ip[-3] == '/':
            break
        try:
            ipaddress.ip_address(ip)
            break
        except ValueError:
            Clear()
            print('Enter a valid IP Address')
            OptionBanner()
    return ip

# function that clears the screena and adds the name banner
def Clear():
    os.system('clear')
    print('''--------------------------------------------------------------------------------
|    /\\   |\\  |   /\\   |    \\  / /\\  -|- /\\        /\\   /\\  /\\  -|- /\\  --|--  |
|   /--\\  | \\ |  /--\\  |     \\/   /   |   /       /--\\   /   /   |   /    |    |
|  /    \\ |  \\| /    \\ |___  |    \\/ _|_  \\/     /    \\  \\/  \\/ _|_  \\/   |    |
--------------------------------------------------------------------------------
''')
          
# function that creates a option name banner

def OptionBanner():
    c = len(f'| {currentPath} |')
    print(f'''{c * '-'}
| {currentPath} |
{c * '-'}''')

        
# Running Program 
Clear()
while True:
    mainPath = 'AnalysisAssistant'
    userPath = input('''
Input the path to the folder you want your AnalysisAssistant directory in.

    example - /home/user/Desktop/
    
    input - ''')
    if userPath[0] != '/' or userPath[-1] != '/':
        Clear()
        print(f'''---------------------------------------------
| Follow the format provided by the example |
---------------------------------------------''')       
    elif DirExists(userPath):
        CreateDir(userPath, mainPath)  
        break 
    else:
        c = len(f'| {userPath} in not a real Path, look at the example if you need help. |')
        Clear()
        print(f'''{c * '-'}
| {userPath} in not a real Path, look at the example if you need help. |
{c * '-'}''')
        


while True:
    option = input('''
Enter one of the options below by typing the number of the option.

        1 - Ping an IP an IP address and pipe it to a text file
        2 - Nmap scan of a network and pipe it to a text file
        3 - Netstat of an IP address and pipe it to a text file

        Type "quit" if you would like to leave the program
                
        Option - ''')
    if option == "1":
        currentPath = 'Ping'
        count = '-c 6'
        CreateDir(userPath, mainPath + '/' + currentPath)
        OptionBanner()
        ip = IpAddress()
        CreateFile(userPath, mainPath + '/' + currentPath, currentPath, ip, count)
    elif option == "2":
        currentPath = 'Nmap'
        CreateDir(userPath, mainPath + '/' + currentPath) 
        OptionBanner()
        ip = IpAddress()
        CreateFile(userPath, mainPath + '/' + currentPath, currentPath, ip)
    elif option == "3":
        currentPath = 'Netstat'
        CreateDir(userPath, mainPath + '/' + currentPath) 
        OptionBanner()
        ip = IpAddress()
        CreateFile(userPath, mainPath + '/' + currentPath, currentPath, ip)
    elif option == "quit":
        break
    else:
        Clear()
        print('''------------------------
| Enter a Valid Option |
------------------------''')


    

