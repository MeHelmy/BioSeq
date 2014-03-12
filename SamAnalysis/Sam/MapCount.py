'''
Created on Dec 9, 2013

@author: medhat

This module input is a SAM file will count the number of mapped reads 
Algorithm
check if -F parameter != 4
if so 
add the read to dictionary as a key and the value is number of time it was repeated
and in other dictionary add the read to dictionary as a key and the value is length of sequence was mapped
'''

import sys , getopt

def main(argv):
    inputFile = ''

    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print 'MapCount.py -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'MapCount.py -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg
            mapRead , lengthOfMappedReads = countReads(inputFile)
            dictCount(mapRead , lengthOfMappedReads)         
    
    
def is_empty(any_structure):
    if any_structure:
        #print('Structure is not empty.')
        return False
    else:
        #print('Structure is empty.')
        return True
    
# input sam file return dictionary of reads name as a key and number of occurrence as a value
def countReads(samFile):
    if samFile:
        mappedReads={}
        lengthMappedReads={}
        samData=open(samFile,'r')
        for line in samData: 
            if not line.startswith("@"):
                colum=line.split('\t')
                if not int(colum[1]) == 4:  #means that it was aligned
                    if colum[0] not in mappedReads:
                        mappedReads[colum[0]]=1 
                        lengthMappedReads[colum[0]]= int(len(colum[9]))
                    else:
                        mappedReads[colum[0]] = int(mappedReads[colum[0]])+1
        return mappedReads , seqCount(lengthMappedReads)
                         
                        
# input dictionary output text file of the count of the dictionary and print of name and value
def dictCount(mapRead , lengthOfMappedReads):
    if not is_empty(mapRead) and not is_empty(lengthOfMappedReads):
        fo = open('mappedReads.txt','a')
        fo.write("Number of mapped reads is ==> "+str(len(mapRead.keys()))+" <== \n ======================== \n")
        fo.write("Count of mapped reads is ==> "+str(lengthOfMappedReads)+" <== \n ======================== \n")
        for key , value in mapRead.iteritems():
            fo.write(key+"\t"+str(value)+"\n")
        fo.close()
        
def seqCount(countDictionary):
    if not is_empty(countDictionary):
        countOfSequence =0
        for key , value in countDictionary.iteritems():
            countOfSequence+=value
    return countOfSequence        
        
            
        
       
        
if __name__ == "__main__":
    main(sys.argv[1:])         
        
    