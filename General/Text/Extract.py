'''
Created on Mar 10, 2014

@author: medhat
'''
import sys , getopt ,re

def main(argv):
    inputFile = ''
    
    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile="])
    except getopt.GetoptError:
        print 'Extract.py -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'Extract.py -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg
            extractData(inputFile)
             
 # function take file as input and extract data based on a column and write it to output file
def extractData(inputFile):
    print(inputFile)
    if inputFile:
        fileData = open(inputFile, 'r')
        fo = open('extractedData.txt','w')
        genIdFile = open('GenIds.bed' ,'w')
        header = extractHeader(inputFile)
        fo.write(header)
        fileData.next()
        for line in fileData:
            lineColumns = line.split('\t')
            if (float(lineColumns[14]) < 0) :
                fo.write(line)
                #genIdFile.write(str(lineColumns[0]) + '\t' + str(lineColumns[2]) + '\t' + str(lineColumns[3])+ '\t' + str(lineColumns[4])+'\n')
                direction = lineColumns[5]
                direction = direction.strip()
                fastaName = str(lineColumns[0])
                if direction == '+':
                    fastaName=fastaName +'\t1\t+'
                else:
                    fastaName=fastaName +'\t1\t-'
                
                genIdFile.write(str(re.findall(r'\d+',lineColumns[2])[0]) + '\t' + str(lineColumns[3]) + '\t' + str(lineColumns[4])+ '\t' + fastaName +'\n')
                
        fo.close()
        genIdFile.close()        
 
def extractHeader(inFile):
    with open(inFile, 'r') as f:
        first_line = f.readline()
        return first_line 

if __name__ == "__main__":
    main(sys.argv[1:])     
#extractData("/home/medhat/Samples/merge_test/merged_seq_report_sorted.txt")
