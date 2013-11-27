'''
Created on 26 Nov 2013

@author: medhat
'''
import re, sys , getopt
totalSequenceLength = 0
nameOfSequence = {}

def main(argv):
    inputFile = ''
    outputFile = ''
    length = 0
    sequenceLength = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:l:",["ifile=","ofile=","length="])
    except getopt.GetoptError:
      print 'BamMan.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'BamMan.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg
        elif opt in ("-o", "--ofile"):
            outputFile = arg 
        elif opt in ("-l", "--length"):
            length = arg 
            if length == 0 or not length:
                length = 18         
    remveSortReadsFromBAM(inputFile, outputFile ,length)
    lengthFileName = outputFile.split(".")[0] 
    calculateSequenceLength(nameOfSequence)
    print totalSequenceLength
    with open(lengthFileName + ".count", "a") as myfile1:
                                myfile1.write(str(totalSequenceLength)) 
                                
    
    
      
def remveSortReadsFromBAM(inputFile , outputFile , length):
            if inputFile:
                f = open(inputFile, 'r')
                for line in f:
                    if not line.startswith("@"):
                        textArray = re.split(r'\t+', line)
                        if len(textArray[9]) >= int(length):
                                sequenceAcumlator(textArray[0], len(textArray[9]))
                                with open(outputFile, "a") as myfile1:
                                    myfile1.write(line)
                                
                    else:
                        with open(outputFile, "a") as myfile2:
                            myfile2.write(line)
                print"finish"          
            else:
                print"bad file"  

def sequenceAcumlator(name,length):
    try:
         global nameOfSequence
         nameOfSequence[name] = length 
    except Exception, e:
        print e
    
def calculateSequenceLength(nameOfSequence):
    global totalSequenceLength
    for key in nameOfSequence:
         totalSequenceLength  += nameOfSequence[key]
                
if __name__ == "__main__":
    main(sys.argv[1:]) 
 