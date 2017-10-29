import os
import nltk
import csv
pathname =  os.getcwd() #returns the current working directory of the process
mypath = pathname + '/linedata' #replace '/Data' with the folder containing actual chats


def get_no_of_characters(msg):
	number = 0
	for i in range(len(msg)):
		if msg[i] != ' ':
			number = number + 1
	return number


def get_low_ratio(msg):
	low = sum([int(c.islower()) for c in msg])
	return float(low)/len(msg)


def get_no_of_words(msg):
	str = ''.join(e for e in msg if e.isalnum() or e == ' ')
	tokens = nltk.word_tokenize(str)
	return len(tokens)


def get_avrg_word_length(msg):
	str = ''.join(e for e in msg if e.isalnum() or e == ' ')
	if len(str) == 0:
	        return 0
	tokens = nltk.word_tokenize(str)
	total = 0
	for i in range(len(tokens)):
		total += len(tokens[i])


	return float(total)/len(tokens)



files = []
for (dirpath, dirnames, filenames) in os.walk(mypath):#generate filenames in a directory tree
    files.extend(filenames)
    break

for filename in files:
	inppath = mypath + '/' + filename

	with open(inppath) as f:
    		content = f.readlines()


	outpath = pathname + "/lexical/" + "lexical" + str(filename) 
	outf = open(outpath,"w+")
        outf.write("Serial_No\tMessage_length\tlow_ratio\tno_of_words\tavg_word_length\n")
        
	content = [x.strip() for x in content] 

	for i in range(len(content)):
	        print content[i]
	        if "(file attached)" in content[i]:
	                outf.write(str(i+1) + "\t" +str(0) + "\t"+ str(0) + "\t" + str(0) + "\t" + str(0) + "\n")
	                continue
		message_length = get_no_of_characters(content[i])
		low_ratio = get_low_ratio(content[i])
		no_of_words = get_no_of_words(content[i])
		avg_word_length = get_avrg_word_length(content[i])
		
		
		
		print message_length,low_ratio,no_of_words,avg_word_length
		outf.write(str(i+1) + "\t"+ str(message_length) + "\t" + str(low_ratio) + "\t" + str(no_of_words) + "\t" + str(avg_word_length) + "\n")
		
	f.close()

