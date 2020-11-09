# Author : Pawan Trivedi -- Docker
#          Aravind       -- AWS  
#          Shudha        -- Hadoop


from dockerscript import *
from awsscript import *
from hadoop1 import *
import os

while True:
    os.system('clear')
    print('This Automation Script')
    
    print(''' 
	1. Docker
	2. AWS
	3. Hadoop
	4. Exit 		
	''')
    choice = input('Make a selceion from ')

    if int(choice) == 1:
	    docker()

    elif int(choice) == 2:
	    aws()

    elif int(choice) == 3:
	    hadoop()
    
    elif int(choice) == 4:
        exit()    
	    
    input('Enter to continue...')



