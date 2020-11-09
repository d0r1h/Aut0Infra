
def aws():
	import os
	 


	print("\t\t\t Welcome to Amazon Web Services")
	os.system("aws configure")

	def key_pair():
		key_name = input("Enter key name you want to create")
		os.system("aws ec2 create-key-pair --key-name {}".format(key_name))

	def ec2():
		while True:
			print("""
			1. Launch the ec2 instance
			2. Start the ec2 instance
			3. Stop the ec2 instance
			4. Terminate the ec2 instance
			5. Go to menu
			""")

		
			i = int(input("What do you want to do: "))
			print(i)
			if i==1:
				launch_ec2()
			elif i==2:
				start_ec2()
			elif i==3:
				stop_ec2()
			elif i==4:
				terminate_ec2()
			else:
				menu()



	def ebs():
		while True:
			print("""
			1. Create the EBD Storage
			2. Attach EBS
			3. Detach EBS
			4. Delete EBS
			5. Go to menu 
			""")

		
			i = int(input("What do you want to do: "))
			print(i)
			if i==1:
				create_ebs()
			elif i==2:
				attach_ebs()
			elif i==3:
				detach_ebs()
			elif i==4:
				delete_ebs()
			else:
				menu()
			

			
	def s3():
		while True:
			print("""
			1. Create the S3 Bucket
			2. Delete the bucket
			3. Go to menu
			""")

		
			i = int(input("Enter ur choice : "))
			print(i)
			if i==1:
				create_bucket()
			elif i==2:
				delete_bucket()
			else:
				menu()  
	 

	def launch_ec2():
		ami_id = input('Enter the AMI id ')
		instance_type = input('Enter the instance type ')
		number_instance = int(input('Enter the number of instances you want to launch '))
		security_group = input('Enter the security group ')
		keyname = input('Enter the key name: ')
		os.system('aws ec2 run-instances --image-id {} --instance-type {} --number {} --security-group {} --key-name {}'.format(ami_id,instance_type,number_instance,security_group,keyname))


	def start_ec2():
		ami_id = input("Enter ami-id: ")
		os.system("aws ec2 start-instances --image-id {}".format(ami_id))
		
	def stop_ec2():
		ami_id = input("Enter ami-id: ")
		os.system("aws ec2 stop-instances --image-id {}".format(ami_id))

	def terminate_ec2():
		ami_id = input("Enter ami-id: ")
		os.system("aws ec2 terminate-instances --image-id {}".format(ami_id))


	def create_ebs():
		type = input("Enter the volume type: ")
		size = input("Enter the volume size: ")
		zone = input("Enter the availability zone: ")
		os.system("aws ec2 create-volume --volume-type {} --size {} --availability-zone {}".format(type,size,zone))

	def attach_ebs():
		instance_id = input("Enter the instance id: ")
		volume = input("Enter the volume id: ")
		device = input("Enter the device name: ")
		os.system("aws ec2 attach-volume --instance-id {} --volume-id {} --device-name {}".format(instance_id,volume,device))


	def detach_ebs():
		volume = input("Enter the volume id: ")
		os.system("aws ec2 detach-volume --volume-id {}".format(volume))

	def delete_ebs():
		volume = input("Enter the volume id: ")
		os.system("aws ec2 delete-volume --volume-id {}".format(volume))


	def create_bucket():
		s3_name = input("Enter the bucket name: ")
		s3_region = input("Enter the region: ")
		os.system("aws s3api create-bucket --bucket {} --region {} ={}".format(s3_name,s3_region))

	def delete_bucket():
		s3_name = input("Enter the bucket name: ")
		s3_region = input("Enter the region: ")
		os.system("aws s3api delete-bucket --bucket {} --region {}".format(s3_name,s3_region))


	def menu():
		while True:
			print("\n \n")
			print("""
			Select the service:
				1. Create a key-pair
				2. EC2 
				3. EBS
				4. S3 
			""")

		
			i = int(input("Enter ur choice : "))
			print(i)
			if i==1:
				key_pair()
			elif i==2:
				ec2()
			elif i==3:
				ebs()
			elif i==4:
				s3()
			else:
				exit()


	while True:
			print("\n \n")
			print("""
			Select the service:
				1. Create a key-pair
				2. EC2 
				3. EBS
				4. S3 
			""")

		
			i = int(input("Enter ur choice : "))
			print(i)
			if i==1:
				key_pair()
			elif i==2:
				ec2()
			elif i==3:
				ebs()
			elif i==4:
				s3()
			else:
				exit()
				

