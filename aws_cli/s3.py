def s3():
	import os
	os.system('clear')
	print('Welcome to S3 Service')
	print('''
	1. Create an S3 bucket    
	2. Delete the Bucket   
	3. List Available Buckets 
	''')
	
	ch1 = input('Enter the choice ')
	
	if int(ch1) == 1:
		os.system('clear')
		bucket_name = input(' \n To create a new bucket \n Enter the bucket name ') 
		region = input('Enter region name ')
		os.system("aws s3api create-bucket --bucket {0} --region {1} --create-bucket-configuration LocationConstraint={1} ".format(bucket_name,region))
		print()
	
	elif int(ch1) == 2:
		os.system('clear')
		print('Available Buckets are ...')
		os.system('aws s3api list-buckets --output table')
		bucket_name = input('\n Enter the bucket name ')
		print("\n Deleteing {} bucket ...".format(bucket_name))
		os.system("aws s3api delete-bucket --bucket {}".format(bucket_name))
		print('Done !')
		
		
	elif int(ch1) == 3:
		print('Available Buckets are ...')
		os.system('aws s3api list-buckets --output table')
	
	
