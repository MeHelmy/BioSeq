'''
Created on Oct 10, 2014

@author: medhat
'''
import re, sys , getopt

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
      print 'BamManuplation.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
            print 'SamCIGAR.py -i <inputfile> -o <outputfile>'
            sys.exit()
      elif opt in ("-i", "--ifile"):
            inputFile = arg
      elif opt in ("-o", "--ofile"):
            outputFile = arg 

def getFile(inputFile):
    if inputFile:
        CIGARstats(inputFile)

def CIGARstats(inputFile):
    f = open(inputFile, 'r')
    for line in f:
        if not line.startswith("@"):
            textArray = re.split(r'\t+', line)
            CIGAR = textArray[5]
            print(CIGAR)
    
     
    if __name__ == "__main__":
     main(sys.argv[1:]) 
 