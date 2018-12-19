# FileDumpParser
import csv
import os
import zipfile
import sys
import io
import glob
import pyap
import docx
import codecs


class FileDumpParser:
    def __init__(self):
        self.og = os.getcwd()
        self.debug = False

    def __init__(self, d):
        self.og = os.getcwd()
        self.debug = d

    def unzip(self, file):
        if(self.debug):
            cwd = os.path.join(self.og, "ZipFIles")
            print(cwd)
        if(os.path.isdir(file.name[:-4])):
            print("directory already exists")
            return "fuck"

        cwd = self.og
        os.chdir(cwd)  # change directory from working dir to dir with files
        ret = ''
        if(zipfile.is_zipfile(file)):
            print("is zip")
            with zipfile.ZipFile(file, "r") as zip_ref:
                ret = zip_ref.extractall(cwd)
                zip_ref.close()  # close file
        else:
            print(file, "is not an existing Zipfile!")
        ret = file.name[:-4]
        return ret

    def parseCSV(self, file):
        # file = "CVSFiles/"+
        if(self.debug):
            cwd = os.path.join(self.og, "mysite/CSVFiles")
            print(cwd)

        # os.chdir(cwd)
        addy_List = []
        noAddyList = []
        decoded_file = file.read().decode('utf-16')
        io_string = io.StringIO(decoded_file)
        line_count = 0
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

    def Address_Search(self, test_address):  # NOT in use
        addresses = pyap.parse(test_address, country='US')
        for address in addresses:
            # shows found address
            print(address)
        # shows address parts
            print(address.as_dict())

    def Docx_to_Text(self, filename):  # not in use
        noaddylist = []
        addylist = []
        if(self.debug):
            #cwd = os.path.join(self.og, "CSVFiles")
            cwd = self.og
            print(cwd)
            print(os.path.isfile(filename))

        doc = docx.Document(filename)
        fullText = []
        store =""
        for para in doc.paragraphs:
            tmp = para.text
            print(str(para.text), "this is teh paragraph")
            store = store + "\n" + tmp

        addresses = []
        addresses = pyap.parse(store, country='US')
        # print(addresses)
        addy = []

        for address in addresses:
            addy.append(str(address))

        if(addy == []):
            print(addy[0], "no addres!")
            tlist = [filename]
            noaddylist.append(file)
        else:
            print(addy[0], "found address with name", filename)
            tlist = [filename, addy[0]]
            addylist.append(tlist)

        ret = [addylist, noaddylist]
        print(ret, "= ret")
        return ret
    def read_through_folder(self, filename):
        ret = []
        if(self.debug):
            cwd = os.path.join(self.og, "CSVFiles")

        print(filename, " is path?: ",os.path.isdir(filename))
        cwd = os.path.join(self.og, filename)
        os.chdir(cwd)
        print(cwd)

        for file in glob.glob('*.txt'):
            ret.append(file)

        return ret
        
    def Text_to_String(self, filename):
        ret = []
        noaddylist = []
        addylist = []
        if(self.debug):
            cwd = os.path.join(self.og, "CSVFiles")

        print(os.path.isdir(filename))
        print(filename)
        cwd = os.path.join(self.og, filename)
        os.chdir(cwd)
        print(cwd)

        for file in glob.glob('*.txt'):
            temp = open(file, 'r').read().strip()
            addresses = []
            addresses = pyap.parse(temp, country='US')
            # print(addresses)
            addy = []

            for address in addresses:
                addy.append(str(address))

            if(addy == []):
                print(addy[0], "no addres!")
                tlist = [file]
                noaddylist.append(file)
            else:
                print(addy[0], "found address with name", file)
                tlist = [file, addy[0]]
                addylist.append(tlist)

            os.remove(file)
        ret = [addylist, noaddylist]
        print(ret, "= ret")
        cwd = os.chdir("../")
        print(cwd)

        os.rmdir(filename)
        return ret

    # TEST Cases
    # heheheheh "bigdumper" .... much funny
bigdumper = FileDumpParser(True)
print("Testing...\n")
print(bigdumper.Docx_to_Text("test1.docx"))
# print(bigdumper.unzip("Test1.zip"))
#bigdumper.Address_Search( bigdumper.Text_to_Sting("test1.txt"))
