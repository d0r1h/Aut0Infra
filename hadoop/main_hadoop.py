def hadoop():
	
	from hadoop.master import master
	from hadoop.slave import slave
	from hadoop.client import client
	import os
	
	while True:
		os.system('clear')
		print('Welcome To The Hadoop Program')
		print(''' 
		1. Select Client 
		2. Select Master / Name Node
		3. Select Slave / Data Node
		4. Exit
		''' )
		
		choice = input('Enter choice from menu program')
		
		if int(choice) == 1:
			client()
		elif int(choice) == 2:
			master()
		elif int(choice) == 3:
			slave()
		elif int(choice) == 4:
			exit()
			
		input('Enter to continue')
