'''
Created on Mar 10, 2014

@author: medhat
'''
import sys , getopt

#===============================================================================
# def main(argv):
#     inputFile = ''
# 
#     try:
#         opts, args = getopt.getopt(argv,"hi:",["ifile="])
#     except getopt.GetoptError:
#         print 'ExonLength.py -i <inputfile>'
#         sys.exit(2)
#     for opt, arg in opts:
#         if opt == '-h':
#             print 'ExonLength.py -i <inputfile>'
#             sys.exit()
#         elif opt in ("-i", "--ifile"):
#             inputFile = arg
#             extractData(inputFile)
#===============================================================================
# function take file as input and extract data based on a column and write it to output file
def extractData(inputFile):
    if inputFile:
        fileData =  open(inputFile, 'r')
        fo = open('extractedData.txt','a')
        genIdFile = open('GenIds.txt' ,'a')
        header = extractHeader(inputFile)
        fo.write(header)
        fileData.next()
        for line in fileData:
            lineColumns = line.split('\t')
            if (float(lineColumns[10]) < 0) :
                fo.write(line)
                genIdFile.write(str(lineColumns[0])+'\n')
        fo.close()
        genIdFile.close()        
 
def extractHeader(inFile):
    with open(inFile, 'r') as f:
        first_line = f.readline()
        return first_line 
    
extractData('/home/medhat/Downloads/Samples/merge_test/merged_seq_report_sorted.txt')                     