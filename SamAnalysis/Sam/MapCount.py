'''
Created on Dec 9, 2013

@author: medhat

This module input is a SAM file will count the number of mapped reads 
Algorithm
check if -F parameter != 4
if so 
add the read to dictionary as a key and the value is number of time it was repeated
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
            mapRead = countReads(inputFile)
            dictCount(mapRead)         
    
    
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
        samData=open(samFile,'r')
        for line in samData: 
            if not line.startswith("@"):
                colum=line.split('\t')
                if not int(colum[1]) == 4:  #means that it was aligned
                    if colum[0] not in mappedReads:
                        mappedReads[colum[0]]=1
                    else:
                        mappedReads[colum[0]] = int(mappedReads[colum[0]])+1
        return mappedReads
                         
                        
# input dictionary output text file of the count of the dictionary and print of name and value
def dictCount(resultDictionary):
    if not is_empty(resultDictionary):
        fo = open('mappedReads.txt','a')
        fo.write("Number of mapped reads is ==> "+str(len(resultDictionary.keys()))+" <== \n ======================== \n")
        for key , value in resultDictionary.iteritems():
            fo.write(key+"\t"+str(value)+"\n")
        fo.close()
        
if __name__ == "__main__":
    main(sys.argv[1:])         
        
    