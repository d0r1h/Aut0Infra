def hadoop():
	import os
	def software():
	    print("\t\tInstalling jdk")
	    os.system("rpm -ivh jdk-8u171-linux-x64.rpm -y")
	    print("\t\tInstalling hadoop")
	    os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force -y")
	    
	def datanode():
	    print("\t\t\tDATANODE SETUP")
	    software()
	    datanode_folder = input("\t\t\tFolder name for datanode:")
	    os.system("rm -rf {}".format(datanode_folder))
	    os.system("mkdir {}".format(datanode_folder))
	    namenode_IP = input("\t\t\tProvide namenode IP: ")
	    namenode_port = input("\t\t\tProvide port number of namenode: ")
	    file_hdfs_dn = open("/etc/hadoop/hdfs-site.xml","w")#opening hdfs-site.xml file
		 #data of hdfs of datanode
	    hdfs_data_dn =  '''<?xml version="1.0"?>
	    <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
	 
	    <!-- Put site-specific property overrides in this file. -->
	    <configuration>
	    <property>
	    <name>dfs.data.dir</name>
	    <value>{}</value>
	    </property>
	    </configuration>\n'''.format(datanode_folder)
	    file_hdfs_dn.write(hdfs_data_dn) #writing the data

	    file_core_dn = open("/etc/hadoop/core-site.xml", "w")#opening core-site.xml file
	    core_data_dn = '''<?xml version="1.0"?>
	    <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
	    <!-- Put site-specific property overrides in this file. -->
	    <configuration>
	    <property>
	    <name>fs.default.name</name>
	    <value>hdfs://{}:{}</value>
	    </property>
	    </configuration>\n'''.format(namenode_IP,namenode_port)
	    file_core_dn.write(core_data_dn) 
	    subprocess.getoutput("hadoop-daemon.sh start datanode")  
	    subprocess.getoutput("jps")
	    print("Datanode Started")

	def namenode():
	    print("\t\t\tNAMENODE SETUP")
	    software()
	    namenode_folder = input("\t\t\tFolder name for namenode:")
	    os.system("rm -rf {}".format(namenode_folder))
	    os.system("mkdir {}".format(namenode_folder))
	    os.system("hadoop namenode --format")
	    namenode_IP = input("\t\t\tProvide namenode IP: ")
	    namenode_port = input("\t\t\tProvide port number of namenode: ")
	    file_hdfs_nn = open("/etc/hadoop/hdfs-site.xml","w")#opening hdfs-site.xml file
		 #data of hdfs of datanode
	    hdfs_data_nn =  '''<?xml version="1.0"?>
	    <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
		 
	    <!-- Put site-specific property overrides in this file. -->
	    <configuration>
	    <property>
	    <name>dfs.name.dir</name>
	    <value>{}</value>
	    </property>
	    </configuration>\n'''.format(namenode_folder)   
	    file_hdfs_nn.write(hdfs_data_nn) #writing the data

	    file_core_nn = open("/etc/hadoop/core-site.xml", "w")#opening core-site.xml file
	    core_data_nn = '''<?xml version="1.0"?>
	    <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
	    <!-- Put site-specific property overrides in this file. -->
	    <configuration>
	    <property>
	    <name>fs.default.name</name>
	    <value>hdfs://{}:{}</value>
	    </property>
	    </configuration>\n'''.format(namenode_IP,namenode_port)
	    file_core_nn.write(core_data_nn)   
	    subprocess.getoutput("hadoop-daemon.sh start namenode")
	    subprocess.getoutput("jps")
	    print("Namenode Started")

	def client():
	    print("\t\t\tCLIENT SETUP")
	    software()
	    namenode_IP = input("\t\t\tProvide namenode IP: ")
	    namenode_port = input("\t\t\tProvide port number of namenode: ")
	    file_core_nn = open("/etc/hadoop/core-site.xml", "w")#opening core-site.xml file
	    core_data_nn = '''<?xml version="1.0"?>
	    <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
	    <!-- Put site-specific property overrides in this file. -->
	    <configuration>
	    <property>
	    <name>fs.default.name</name>
	    <value>hdfs://{}:{}</value>
	    </property>
	    </configuration>\n'''.format(namenode_IP,namenode_port)
	    file_core_nn.write(core_data_nn)

	def putfile():
	    fname=input("\t\tEnter your filename : ")
	    st=subprocess.getouput("hadoop fs -put {} /".format(fname))


	def delfile():
	    fname=input("\t\tEnter your filename : ")
	    st=subprocess.getouput("hadoop fs -rm  /{} ".format(fname))

	def no_of_datanode():
	    st=subprocess.getouput("hadoop dfsadmin report | less")


	def files_on_cluster():
	    st=subprocess.getouput("hadoop fs ls /")

	def read_files_from_cluster():
	    fname=input("\t\tEnter your filename")
	    st=subprocess.getouput("hadoop fs -cat /{}".format(fname))
	    
	    
	while True:
		os.system("clear")
		print("\t\t\tWELCOME TO MY HADOOP MENU")
		print("""
		\t\tPress 0 : To return to main menu
		\t\tPress 1 : To create data node
	    	\t\tPress 2 : To create name node
		\t\tPress 3 : To create client
		\t\tPress 4 : To upload file on cluster
		\t\tPress 5 : To delete file on cluster 
	    	\t\tPress 6 : To see all the datanodes on cluster
	    	\t\tPress 7 : To see all the files on the cluster 
	    	\t\tPress 8 : To read a file from cluster 
		""")
		print("\t\t==================================================")
		ch=int(input("Enter your choice : "))
		if   ch == 1:
		    namenode()
		elif ch == 2:
		    datanode()
		elif ch == 3:
		    client()
		elif ch == 4:
		    putfile()
		elif ch == 5:
		    delfile()
		elif ch == 6:
		    no_of_datanode()
		elif ch == 7:
		    files_on_cluster()
		elif ch == 8:
		    read_files_from_cluster()
		elif ch == 0:
		    print("\t\t\tExit\n")
		    a=False
		else :
		    print("\t\tNot supported")
	
