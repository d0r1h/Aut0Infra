from dockerscript import *
from aws_cli.main_aws import *
from hadoop.main_hadoop import *
import os

while True:
    os.system('clear')
    os.system('tput setaf 4')
    print('''  
           _              _      ___    ___            __                
          / \     _   _  | |_   / _ \  |_ _|  _ __    / _|  _ __    __ _ 
         / _ \   | | | | | __| | | | |  | |  | '_ \  | |_  | '__|  / _` |
        / ___ \  | |_| | | |_  | |_| |  | |  | | | | |  _| | |    | (_| |
       /_/   \_\  \__,_|  \__|  \___/  |___| |_| |_| |_|   |_|     \__,_|
      
    ''')
    os.system('tput setaf 3')
    print(' \t\t\t\t\t + -- -- +=[ Author : Pawan Trivedi ')
    os.system('tput setaf 7')
    
    print(''' 
	1. Docker
	2. AWS
	3. Hadoop
	4. Exit 		
	''')
    choice = input('Make a selection from ')

    if int(choice) == 1:
	    docker()

    elif int(choice) == 2:
	    aws()

    elif int(choice) == 3:
	    hadoop()
    
    elif int(choice) == 4:
        exit()    
	    
    input('Enter to continue...')



