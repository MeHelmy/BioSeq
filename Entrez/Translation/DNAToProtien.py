'''
Created on Mar 28, 2014

@author: medhat
'''
from Bio.Seq import Seq, translate
from Bio.Alphabet import IUPAC
import os  ,sys , getopt 

def main(argv):
    scriptName = os.path.basename(__file__)
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print scriptName + ' -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print scriptName + ' -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg
        elif opt in ("-o", "--ofile"):
            outputFile = arg
    loopDirectory(inputFile, outputFile)        

#Read all the files in directory and process them one by one
def loopDirectory(directory,resultDirectory):
    
    print("Reading from directory ==> " + directory)
    for fn in os.listdir(directory):
        print("#===============***===================>  New Record  <===============***===================#")    
        if os.path.isfile(os.path.join(directory,fn)):
            # call method to process the file
            print("Reading from file ==> " + fn)
            fn = directory+fn
            processFasta(fn, resultDirectory)
        else:
            print("Sorry "+fn+" Is not a file")
            
def processFasta(fastaFile,resultDirectory):
    print("Writing to directory #==> " + resultDirectory)
    sequence = readFastaAsString(fastaFile)
    coding_dna = Seq(sequence, IUPAC.unambiguous_dna)
    baseFile = os.path.basename(fastaFile)
    fo = open(resultDirectory+baseFile,'w')
    t = translate(coding_dna)
    fo.write(str(t))
    fo.close()
    
def readFastaAsString(fastaFile):
    fo = open(fastaFile)
    fo.next()
    sequence = ''
    for line in fo:
        line = line.strip()
        sequence = sequence + line
    return sequence         
             
if __name__ == "__main__":
    main(sys.argv[1:])  