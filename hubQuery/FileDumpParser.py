#FileDumpParser
import csv
import os, zipfile, sys
import codecs

og = os.getcwd()
def unzip(file):
	cwd = os.path.join(og, "ZipFIles")
	print(cwd)

	os.chdir(cwd) # change directory from working dir to dir with files

	if(zipfile.is_zipfile(file)):
		with zipfile.ZipFile(file,"r") as zip_ref:
			zip_ref.extractall(cwd)
			zip_ref.close() # close file
			os.remove(file) # delete zipped file
	else:
		print(file, "is not an existing Zipfile!")

def parseCSV(file):
	#file = "CVSFiles/"+ file
	cwd = os.path.join(og, "CSVFiles")
	print(cwd)

	os.chdir(cwd)
	addy_List = []
	noAddyList = []
	with open(file, 'rb') as csv_file:
		#csv_reader = csv.reader(csv_file, delimiter=',',)
		csv_reader = csv.reader(x.replace('\0', '') for x in csv_file)
		line_count = 0
		for row in csv_reader:
			if(row == []):
				print(addy_List)
				print("\n\nNO ADDR LIST \n\n\n\n")
				print(noAddyList)
				return 1
			#print(line_count)
			if line_count == 0:
				print('Column names are {", ".join(row)}')
			elif row[3] != "Rejected":
				if(row[4] != ""):
					tl = [row[0], row[4]]
					addy_List.append(tl)
				else:
					tl = [row[0]]
					noAddyList.append(tl)
			line_count += 1

parseCSV("candidates.csv")
unzip("Test1.zip")