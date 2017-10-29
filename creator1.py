import numpy 
import os
import datetime as dt
pathname =  os.getcwd() #returns the current working directory of the process
mypath = pathname + '/Data' #replace '/Data' with the folder containing actual chats
files = []
for (dirpath, dirnames, filenames) in os.walk(mypath):#generate filenames in a directory tree
    files.extend(filenames)
    break


print files
number = 0
number1 = -1
for filename in files:
	number = number + 1
	number1 = number1 + 2
	inppath = mypath + '/' + filename
	#print inppath

	with open(inppath) as f:
    		content = f.readlines()

	outpath = pathname + "/corpus/" + str(number)+".txt"
	outpath1 = pathname + "/linedata/" + str(number1) + ".txt"
	outpath2 = pathname + "/linedata/" + str(number1 + 1) + ".txt"
	outf = open(outpath,"w+")

	outf1 = open(outpath1,"w+")
	outf2 = open(outpath2,"w+")
	userid={}
	content = [x.strip() for x in content] 

	for i in range(1,len(content)):
		var = content[i].split(', ')
		if len(var) ==1 :
			continue
		var1 = var[1].split(' - ')
		if len(var1) == 1:
			continue
		var2 = var1[1].split(': ')
		if len(var2) == 1:
			continue

		date = var[0]
		time = var1[0]
		user = var2[0]
		msg = var2[1]

		#print user,msg
		date = date.split('/')
		


		if len(userid) == 0:
			userid[user]=1
		
		if len(userid) == 1 and user not in userid.keys():
			userid[user]=0


		day = int(date[0])
		month = int(date[1])
		year = 2000 + int(date[2])

		flag = 0

		time = time.split(' ')

		meridian = time[1]


		time = time[0].split(':')
		hour = int(time[0])
		minute = int(time[1])


		if meridian == 'AM' and hour == 12:
			hour = 0

		if meridian == 'PM' and hour != 12:
			hour = hour + 12


     



    
		a = dt.datetime(2014,01,01,00,00)
		b = dt.datetime(year,month,day,hour,minute)

		x =  (b-a).total_seconds()
			
		if userid[user] == 0:
			outf1.write(msg + "\n")
		
		if userid[user] == 1:
			outf2.write(msg + "\n")

			
		outf.write(msg + "\t" + str(userid[user]) + "\t"+str(x) + "\n")
	f.close()
	outf.close()



