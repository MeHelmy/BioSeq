'''
Created on Feb 26, 2014

@author: medhat
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
            writeData(getId(inputFile))
            
def is_empty(any_structure):
    if any_structure:
        #print('Structure is not empty.')
        return False
    else:
        #print('Structure is empty.')
        return True
    
def getId(inputFile):
    if inputFile:
        fileData = open(inputFile,'r')
        data = []
        for line in fileData:
            colum=line.split('\t')
            data.append(colum[7]) 
        return data 

def writeData(data):
    if not is_empty(data):
        fo = open('Ids.txt','a')
        for i in data[1:]:
            fo.write(i+'\n')
        fo.close()         
             
            
if __name__ == "__main__":
    main(sys.argv[1:])              