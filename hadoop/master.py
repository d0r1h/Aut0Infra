def master():

	import os
	
	os.system('clear')
	print('Welcome to the master program')
	
	print(''' 
	1. Setting up the Hadoop program
	2. Setting up system as Master 
	''')
	
	ch1 = input('Enter the choice from menu ')
	
	if int(ch1) == 1:
		os.system('rpm -ivh jdk-8u171-linux-x64.rpm -y')
		os.system('rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force -y')
		
				
	elif int(ch1) == 2:
		os.chdir('/')
		folder_name = input('Enter the dir name to create ')
		os.system('mkdir {}'.format(folder_name))
		os.chdir('/etc/hadoop')
		hdfs_config = open('hdfs-site.xml', w)
		hdfs_config.write('''<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>{}</value>\n</property>\n</configuration>'''.format(folder_name))
		hdfs_config.close()
		
		core_site_config = open('core-site.xml', w)
		ip = input('Enter master node IP ')
		port = input('Enter the port no. ')
		core_site_config.write(''' \n<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:{}</value>\n</property>\n</configuration\n'''.format(ip,port))
		core_site_config.close()
		
		os.system('hadoop namenode -format ')
		os.system('hadoop-daemon.sh start namenode ')
		os.system('jps')
		
		
		
		
		
		
		
