	
def hadoop():	
	import os
	os.system("tput setaf 3")
	print("\t\t\t\tpikachu welcomes you...")
	os.system("tput setaf 7")
	print("\t\t\t\t--------------------------")

	def core():
		nn_ip = input('enter namenode ip and hadoop port eg. hdfs://1.2.3.4:9000:')
		print(nn_ip)
		os.system('echo \<configuration\> >> core-site.xml')
		os.system('echo \<property\> >> core.site.xml')
		os.system("echo \<name\>fs.default.name\<\/name\> >> core.site.xml")
		os.system("echo \<value\>{}\<\/value\> >> core.site.xml".format(nn_ip))
		os.system('echo \<\/property\> >> core.site.xml')
		os.system("echo \<\/configuration\> >> core-site.xml")
		os.system("scp core-site.xml {}:/etc/hadoop/core.site.xml".format(ip))
		os.system("rpm -rf core-site.xml")
		os.system("cp cp.xml core-site.xml")

	def hdfs():
		dndir=input('enter any directory name you want too create for datanode:')
		print(dndir)
		os.system('echo \<configuration\> >> hdfs-site.xml')
		os.system('echo \<property\> >> hdfs.site.xml')
		os.system("echo \<name\>dfs.default.name\<\/name\> >> hdfs.site.xml")
		os.system("echo \<value\>{}\<\/value\> >> hdfs.site.xml".format(dndir))
		os.system('echo \<\/property\> >> hdfs.site.xml')
		os.system("echo \<\/configuration\> >> hdfs-site.xml")
		os.system("scp hdfs-site.xml {}:/etc/hadoop/hdfs.site.xml".format(ip))
		os.system("rpm -rf hdfs-site.xml")
		os.system("cp hd.xml hdfs-site.xml")		
	def data():
		dir=input('enter any directory name where java and hadoop file resides:')
		print(dir) 
		os.system("ssh {} rpm -i {}/jdk-8u171-linux-x64.rpm".format(ip,dir))
		os.system("ssh {} rpm -i {}\/hadoop-1.2.1-1.x86_64.rpm --force".format(ip,dir))
		core()
		hdfs()
		os.system("ssh {} hadoop-daemon.sh start datanod".format(ip))
		os.system("ssh {} jps".format(ip))		
	 
	r = input('HOE U WANT TO LOGIN AS?(LOCL/REMOTE)')
	print(r)
	print("\n\n")
	print("""
		press 1: data
		press 2: cal
		press 3: configure_data_node
		press 4: create_new_user
		press 5: partitioning
		press 6:hadoop -ls
		""") 
	if r == "local":
		i = input("enter ur choice")
		print(i)
		if i==1:
			os.system("ssh {} data".format(ip))
		elif i==2:
			os.system("cal")
		elif i==3:
			print("hello")
			data()
		else:
			os.system("hadoop dfsadmin -report")
		
	else:
		ip = input('enter remote ip:')
		print(ip)
		q = input("enter ur choice")
		print(q)
		if q==1:
			print("hello")
			os.system('ssh root@{} date'.format(ip))
		elif q==2:
			os.system("cal")
		elif q==3:
			data()
		else:
			os.system("hadoop dfsadmin -report")























