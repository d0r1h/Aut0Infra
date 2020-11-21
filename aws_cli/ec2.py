def ec2():
	import os
	os.system('clear')
	print('Welcome to Ec2 Service')
	print('''
	1. Instances    
	2. EBS (Elastic Block Store)   
	3. Security 
	''')
	ch1 = input('Enter the choice ')
	
	if int(ch1) == 1:
		os.system('clear')
		print('Available Instances Running or Dead\n')
		os.system("aws ec2 describe-instances --query 'Reservations[*].Instances[*].{Instance:InstanceId, State:State.Name, IP:PublicIpAddress, Name:Tags[0].Value }' --output table")
		print('1. Start an instances','2. Stop an instances','3. Terminate an instances','4. Launch a New Ec2 instance' ,sep='\n')
		
		ch2 = input('\nEnter your choice ')
		if int(ch2) == 1:
			instance_id = input('Enter the instance id')
			os.system('aws ec2 start-instances --instance-id {}'.format(instance_id))
		elif int(ch2) == 2:
			instance_id  = input('Enter the instance id')
			os.system('aws ec2 stop-instances --instance-id {}'.format(instance_id))
		elif int(ch2) == 3:
			instance_id = input('Enter the instance id')
			os.system('aws ec2 terminate-instances --instance-ids {}'.format(instance_id))
		elif int(ch2) == 4:
			print('\nAvailable Security group')
			os.system("aws ec2 describe-security-groups --query 'SecurityGroups[*].[GroupId]' --output text")
			print('\nAvailable Key Value')
			os.system("aws ec2 describe-key-pairs --query 'KeyPairs[*].KeyName' --output text")
			security_group  = input('\nEnter Security group id ')
			key_name = input('Enter the key value ')
			print('Launching a new instance....')
			os.system(" aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --count 1  --subnet-id subnet-ca7c75a2  --security-group-ids {} --key-name {} ".format(security_group,key_name))
					
	
	elif int(ch1) == 2:
		os.system('clear')
		print('\nAvailable Volumes')
		os.system("aws ec2 describe-volumes --query 'Volumes[*].[VolumeId, AvailabilityZone, State]' --output text")
		ch2 = input('\nWant to create a new volume : yes or no ')
		if ch2 == 'yes':
			zone = input('Enter availablity zone ')
			vsize = input('Enter the size of volume ')
			os.system("aws ec2 create-volume --availability-zone {} --size {}".format(zone,vsize))
		elif ch2 == 'no':
			ec2()
		
		
	elif int(ch1) == 3:
		os.system('clear')
		print(""" 
		1. Security Groups
		2. Key Pairs	
		""")
		ch2 = input('Enter your choice ')
		if int(ch2) == 1:
			print('\nAvailanle Security Groups')
			os.system("aws ec2 describe-security-groups --query 'SecurityGroups[*].[GroupId]' --output text")
			ch3 = input('\nWant to create a new Security Group : yes or no ')
			if ch3 == 'yes':
				group_name = input('Enter security group name ')
				group_description = input('Enter security group description ')
				os.system('aws ec2 create-security-group  --group-name {} --description {}'.format(group_name,group_description))
			elif ch3 == 'no':
				print('')
		elif int(ch2) == 2:
			print('\nAvailable Key Pairs')
			os.system("aws ec2 describe-key-pairs --query 'KeyPairs[*].KeyName' --output text")
			ch3 = input('\nWant to create a new Key Pair : yes or no ')
			if ch3 == 'yes':
				key_name = input('Enter Key name ') 
				key_file_name = input('Enter file name to store key in .pem format ')
				os.system('aws ec2 create-key-pair --key-name {} > {}.pem'.format(key_name, key_file_name))
			elif ch3 == 'no':
				print('')
				
