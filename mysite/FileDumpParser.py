#FileDumpParser
import csv
import os, zipfile, sys, io
import codecs
class FileDumpParser:

	def __init__(self):
		self.og = os.getcwd()

	def unzip(self, file):
		cwd = os.path.join(self.og, "ZipFIles")
		print(cwd)

		os.chdir(cwd) # change directory from working dir to dir with files

		if(zipfile.is_zipfile(file)):
			with zipfile.ZipFile(file,"r") as zip_ref:
				zip_ref.extractall(cwd)
				zip_ref.close() # close file
				os.remove(file) # delete zipped file
		else:
			print(file, "is not an existing Zipfile!")

	def parseCSV(self, file):
		#file = "CVSFiles/"+ file
		#cwd = os.path.join(self.og, "mysite/CSVFiles")
		#print(cwd)

		#os.chdir(cwd)
		addy_List = []
		noAddyList = []
		decoded_file = file.read().decode('utf-16')
		io_string = io.StringIO(decoded_file)
		line_count=0;
		for row in csv.reader(io_string, delimiter=',', quotechar='|'):
			if(row == []):
				print(addy_List)
				print("\n\nNO ADDR LIST \n\n\n\n")
				print(noAddyList)
				ret = [addy_List, noAddyList]
				return ret
			print(line_count)
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
			
		print(addy_List)
		print("\n\nNO ADDR LIST \n\n\n\n")
		print(noAddyList)
		ret = [addy_List, noAddyList]
		return ret


#TEST Cases
#heheheheh "bigdumper" .... much funny
#
#
#bigdumper = FileDumpParser()
#bigdumper.parseCSV("candidates.csv")
#bigdumper.unzip("Test1.zip")
#
#