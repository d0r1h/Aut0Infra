def aws():


	from aws_cli.ec2 import ec2
	from aws_cli.s3 import s3
	import os



	def awscli():
		os.system('aws configure')

			
	while True:
		os.system('clear')
		print('Welcome to aws cli program')
			
		print(''' 
		1. Configure AWS Cli : First time user
		2. EC2 Service
		3. S3 Service
		4. Exit
		''')
			
		choice = input('Enter the choice from menu program ')
		if int(choice) == 1:
			awscli()
		elif int(choice) == 2:
			ec2()
		elif int(choice) == 3:
			s3()
		elif int(choice) == 4:
			exit()
				
				
			
		input('\nEnter to continue ')

