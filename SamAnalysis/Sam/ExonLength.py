'''
Created on Jan 7, 2014

@author: medhat
script to count the exons from GTF file
'''
import sys , getopt

def main(argv):
    inputFile = ''

    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print 'ExonLength.py -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'ExonLength.py -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg
            lengthOfExonReads = countExons(inputFile)
            dictCount(lengthOfExonReads)         
    
def is_empty(any_structure):
    if any_structure:
        #print('Structure is not empty.')
        return False
    else:
        #print('Structure is empty.')
        return True
    
# input GTF file return List of exon length for each line.
def countExons(GTF):
    if GTF:
        lengthExonReads=[]
        GTFData=open(GTF,'r')
        for line in GTFData: 
                colum=line.split('\t')
                if str(colum[2]) == "exon":  #means that it was aligned
                        lengthExonReads.append( int(colum[4]) - int(colum[3]))
        return seqCount(lengthExonReads)
                         
                        
# input List output text file of the count of the accumulated element of list
def dictCount(lengthExonReads):
    if not is_empty(lengthExonReads):
        fo = open('ExonReads.txt','a')
        fo.write("Count of Exon reads is ==> "+str(lengthExonReads)+" <== \n ======================== \n")
        fo.close()
#count the list element.        
def seqCount(countDictionary):
    if not is_empty(countDictionary):
        countOfSequence =0
        for value in countDictionary:
            countOfSequence+=value
    return countOfSequence  

if __name__ == "__main__":
    main(sys.argv[1:])      
